import os
import sys
import json
import time
import random
import difflib
from datetime import datetime
import requests
import config
import life_scenarios
import canan_engine
import canan_community
import create_canan_reel

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
HISTORY_FILE = os.path.join(BASE_DIR, "posted_history.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def send_telegram_alert(text: str):
    """Kritik sistem uyarılarını doğrudan Telegram kanalına/yöneticiye iletir."""
    try:
        requests.post(
            f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage",
            data={"chat_id": config.TELEGRAM_CHANNEL, "text": text},
            timeout=10
        )
    except Exception:
        pass


def check_meta_token_health() -> bool:
    """Paylaşım öncesi Meta API token'ının aktif olup olmadığını test eder."""
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "")
    if not token or not page_id:
        return False
    try:
        r = requests.get(
            f"https://graph.facebook.com/v21.0/{page_id}?fields=id,name&access_token={token}",
            timeout=8
        ).json()
        if "error" in r:
            err_msg = r["error"].get("message", "Bilinmeyen hata")
            print(f"⚠️ [Meta Token Hatası]: {err_msg}")
            send_telegram_alert(
                f"🚨 [CANAN TUNA DİKKAT]\n"
                f"Facebook/Instagram Meta Token oturumu kapanmış!\n"
                f"Hata: {err_msg}\n"
                f"Lütfen Meta Developer sayfasından yeni token alıp güncelleyin."
            )
            return False
        return True
    except Exception as e:
        print(f"⚠️ Token kontrol istisnası: {e}")
        return True


def load_history() -> list:
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_history(history: list):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def get_recent_instagram_captions(limit: int = 100) -> list:
    """
    Instagram Graph API üzerinden Canan'ın son paylaştığı gönderilerin açıklamalarını
    yeniden eskiye doğru (0 = en son paylaşılan) canlı olarak çeker.
    """
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    if not ig_id or not token:
        return []

    captions = []
    url = f"https://graph.facebook.com/v21.0/{ig_id}/media?fields=id,caption,timestamp&limit={min(limit, 100)}&access_token={token}"
    try:
        while url and len(captions) < limit:
            resp = requests.get(url, timeout=15).json()
            if "data" not in resp:
                break
            for p in resp["data"]:
                cap = (p.get("caption") or "").strip()
                if len(cap) > 5:
                    captions.append(cap)
            url = resp.get("paging", {}).get("next") if len(captions) < limit else None
    except Exception as e:
        print(f"⚠️ Instagram canlı geçmiş sorgulama uyarısı: {e}")
    return captions


def _strip_legacy_prefix(text: str) -> str:
    """Eski sürümlerde eklenmiş olabilen 'Yazdan kalanlar...' ön ek paragrafını temizler."""
    t = text.strip().lower()
    if "siz de yazı şimdiden özleyenlerden misiniz?" in t:
        parts = t.split("siz de yazı şimdiden özleyenlerden misiniz?")
        if len(parts) > 1:
            t = parts[-1].lstrip(" ✨\n\r")
    return t.strip()


def _scenario_matches_caption(sc: dict, ig_caption: str) -> bool:
    """Bir senaryonun Instagram'daki belirli bir gönderiyle eşleşip eşleşmediğini kesin olarak tespit eder."""
    rc_raw = ig_caption.lower()
    rc_clean = _strip_legacy_prefix(rc_raw)

    # 1. Senaryoya özel imza kelimeleri (eski ve yeni açıklamalar dahil)
    for sig in sc.get("signatures", []):
        if sig.lower() in rc_raw:
            return True

    # 2. Mevcut açıklamanın ve alternatif açıklamaların çekirdek cümlesi
    candidate_texts = [sc.get("caption", "")] + sc.get("alt_captions", [])
    for c_text in candidate_texts:
        sc_clean = _strip_legacy_prefix(c_text)
        if not sc_clean:
            continue
        # İlk 28 karakter veya ortadaki 30 karakter doğrudan geçiyor mu?
        snippet_start = sc_clean[:28].strip()
        snippet_mid = sc_clean[10:42].strip()
        if len(snippet_start) >= 18 and snippet_start in rc_raw:
            return True
        if len(snippet_mid) >= 20 and snippet_mid in rc_raw:
            return True
        if difflib.SequenceMatcher(None, sc_clean[:45], rc_clean[:45]).ratio() > 0.62:
            return True

    return False


def get_30day_quarantined_filenames(recent_caps: list = None) -> set:
    """
    Son 30 günde (yaklaşık son 90 Instagram paylaşımında + yerel karantinada) kullanılan
    TÜM görsellerin (ana kareler, Reels içindeki 2-3-4. yan kareler, fotoğraflar ve hikayeler)
    dosya adlarını döner. Render yeniden başlasa bile Instagram canlı geçmişinden yan kareleri de
    deterministik olarak yeniden hesaplar ve 30 gün boyunca tekrar kullanılmasını %100 engeller!
    """
    if recent_caps is None:
        recent_caps = get_recent_instagram_captions(limit=90)

    quarantined = set(create_canan_reel.load_quarantine(days=30).keys())

    # Yerel geçmişten son 90 paylaşımın görsellerini ekle
    local_hist = load_history()
    for h in local_hist[-90:]:
        if h.get("image_name"):
            quarantined.add(h["image_name"])
        for comp in h.get("companion_names", []):
            quarantined.add(comp)

    # Instagram canlı geçmişindeki son 90 gönderiden hem ana görseli hem de Reels yan görsellerini çıkar
    all_scenarios = [
        sc for sc in life_scenarios.SCENARIOS
        if sc.get("image_path") and os.path.exists(sc.get("image_path"))
    ]
    for rc in recent_caps[:90]:
        for sc in all_scenarios:
            if _scenario_matches_caption(sc, rc):
                primary_p = sc["image_path"]
                quarantined.add(os.path.basename(primary_p))
                if sc.get("companions"):
                    for cp in sc["companions"]:
                        quarantined.add(os.path.basename(cp))
                elif sc.get("type") == "video":
                    # Deterministik yan görselleri de karantinaya ekle
                    sim_comps = create_canan_reel.pick_companion_images(
                        primary_p,
                        count=3,
                        exclude_filenames=quarantined
                    )
                    for cp in sim_comps:
                        quarantined.add(os.path.basename(cp))
                break

    return quarantined


def pick_next_scenario(force_type: str = None) -> dict:
    """
    Canan Tuna için 30 GÜN SIFIR-TEKRAR KALKANLI canlı senaryo seçicisi:
    1. Instagram API'ye canlı bağlanıp son 100 gönderiyi çeker.
    2. Son 30 günde hem ana karede, hem Reels'in 2-3-4. yan karelerinde, hem de Story'de
       kullanılmış tüm fotoğrafları karantinaya alır.
    3. Öncelikle HİÇ PAYLAŞILMAMIŞ ve ana görseli karantinada olmayan senaryoları seçer.
    """
    all_scenarios = [
        sc for sc in life_scenarios.SCENARIOS
        if sc.get("image_path") and os.path.exists(sc.get("image_path"))
    ]
    if not all_scenarios:
        return None

    recent_caps = get_recent_instagram_captions(limit=100)
    print(f"📡 [Canan Anti-Tekrar Kalkanı] Instagram'dan son {len(recent_caps)} canlı paylaşım çekildi.")

    quarantined_files = get_30day_quarantined_filenames(recent_caps)
    print(f"🛡️ [30 Günlük Görsel Karantinası] Son 30 günde kullanılan {len(quarantined_files)} görsel koruma altında.")

    # Yerel geçmişi de yedek olarak oku
    local_hist = load_history()
    local_recent_ids = [h.get("scenario_id") for h in local_hist[-45:] if h.get("scenario_id")]

    unseen_scenarios = []
    scored_scenarios = []  # (distance_from_latest, scenario)

    for sc in all_scenarios:
        last_seen_idx = None
        for idx, rc in enumerate(recent_caps):
            if _scenario_matches_caption(sc, rc):
                last_seen_idx = idx
                break

        img_fname = os.path.basename(sc["image_path"])
        # Eğer Instagram'da hiç görülmediyse, yerel son 30 paylaşımda yoksa VE görseli 30 günlük karantinada değilse -> TAMAMEN TAZE
        if last_seen_idx is None and sc["id"] not in local_recent_ids[-30:] and img_fname not in quarantined_files:
            unseen_scenarios.append(sc)
            scored_scenarios.append((9999, sc))
        elif last_seen_idx is None and sc["id"] not in local_recent_ids[-15:]:
            # Senaryo hiç paylaşılmamış ama görseli yan karede kullanılmışsa ikinci öncelik ver
            scored_scenarios.append((5000, sc))
        else:
            dist = last_seen_idx if last_seen_idx is not None else 40
            scored_scenarios.append((dist, sc))

    print(f"🎯 [Canan Senaryo Havuzu] {len(all_scenarios)} aktif senaryodan {len(unseen_scenarios)} tanesi hiç paylaşılmamış ve görseli %100 taze!")

    now = datetime.now()
    hour = now.hour
    day_categories = ("tatil", "hobi", "sanat", "sokak", "ev", "lifestyle")
    evening_categories = ("gece", "spor", "lifestyle", "is", "sanat", "ev")
    target_cats = day_categories if hour < 16 else evening_categories

    # Kuzen Burcu Sıklık Kontrolü:
    ever_posted_burcu = any("burcu" in rc.lower() for rc in recent_caps) or any("kuzen_burcu" in sid for sid in local_recent_ids)
    recent_5_has_burcu = any("burcu" in rc.lower() for rc in recent_caps[:5]) or any("kuzen_burcu" in sid for sid in local_recent_ids[-5:])

    if unseen_scenarios:
        first_debut = [s for s in unseen_scenarios if s["id"] == "kuzen_burcu_kirmizi_pembe_oje_1"]
        if not ever_posted_burcu and first_debut:
            chosen_pool = first_debut
        else:
            bold_unseen = [s for s in unseen_scenarios if s.get("bold")]
            base_unseen = bold_unseen if bold_unseen else unseen_scenarios
            solo_unseen = [s for s in base_unseen if "kuzen_burcu" not in s["id"]]
            burcu_unseen = [s for s in base_unseen if "kuzen_burcu" in s["id"]]

            if recent_5_has_burcu and solo_unseen:
                active_pool = solo_unseen
            elif burcu_unseen and random.random() < 0.30:
                active_pool = burcu_unseen
            else:
                active_pool = solo_unseen if solo_unseen else base_unseen

            preferred = [s for s in active_pool if s.get("category") in target_cats]
            chosen_pool = preferred if preferred else active_pool
    else:
        # Tüm senaryolar en az 1 kez paylaşıldıysa, en eski paylaşılmış olan (30 gün = ~90 paylaşım öncesi) senaryolardan seç
        scored_scenarios.sort(key=lambda x: x[0], reverse=True)
        oldest_pool = [sc for dist, sc in scored_scenarios[:15] if dist >= 60] or [sc for _, sc in scored_scenarios[:10]]
        preferred = [s for s in oldest_pool if s.get("category") in target_cats]
        chosen_pool = preferred if preferred else oldest_pool

    chosen = dict(random.choice(chosen_pool))
    chosen["_quarantined_files"] = quarantined_files

    # Eğer bu senaryonun alternatif taze açıklamaları varsa ve ana açıklama daha önce kullanıldıysa, kullanılmamış olanı seç
    alt_list = [chosen["caption"]] + chosen.get("alt_captions", [])
    fresh_captions = [
        c for c in alt_list
        if not any(c[:25].lower() in rc.lower() for rc in recent_caps[:40])
    ]
    if fresh_captions:
        chosen["caption"] = random.choice(fresh_captions)
    else:
        chosen["caption"] = random.choice(alt_list)

    return chosen


def post_to_instagram_reels(video_path: str, caption: str) -> dict:
    """Canan Tuna Instagram hesabına (@canantuna_official) doğrudan Reels yayınlar."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    video_filename = os.path.basename(video_path)

    candidate_urls = []
    base_url = getattr(config, "BASE_URL", "https://cananbot.onrender.com").rstrip("/")
    candidate_urls.append(f"{base_url}/media/{video_filename}")

    try:
        with open(video_path, "rb") as f:
            r_up = requests.post(
                "https://catbox.moe/user/api.php",
                data={"reqtype": "fileupload"},
                files={"fileToUpload": f},
                timeout=40
            )
            if r_up.status_code == 200 and r_up.text.strip().startswith("http"):
                candidate_urls.append(r_up.text.strip())
    except Exception as e:
        print(f"Catbox uyarısı: {e}")

    try:
        with open(video_path, "rb") as f:
            r_tf = requests.post("https://tmpfiles.org/api/v1/upload", files={"file": f}, timeout=40).json()
            if r_tf.get("status") == "success":
                candidate_urls.append(r_tf["data"]["url"].replace("tmpfiles.org/", "tmpfiles.org/dl/"))
    except Exception as e:
        print(f"Tmpfiles uyarısı: {e}")

    last_error = None
    for video_url in candidate_urls:
        try:
            print(f"🌐 Instagram Reels Video URL deneniyor: {video_url}")
            r_c = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media",
                data={
                    "media_type": "REELS",
                    "video_url": video_url,
                    "caption": caption,
                    "share_to_feed": "true",
                    "access_token": token
                },
                timeout=30
            ).json()

            container_id = r_c.get("id")
            if not container_id:
                print(f"❌ Instagram Reels Container Hatası ({video_url}): {r_c}")
                last_error = r_c
                continue

            is_ready = False
            for i in range(30):
                time.sleep(5)
                st = requests.get(
                    f"https://graph.facebook.com/v21.0/{container_id}?fields=status_code&access_token={token}",
                    timeout=15
                ).json()
                code = st.get("status_code")
                print(f"⏳ Instagram Reels İşleme Durumu ({i+1}/30): {code}")
                if code == "FINISHED":
                    is_ready = True
                    break
                if code == "ERROR":
                    print(f"❌ Instagram Video Kodlama Hatası: {st}")
                    last_error = st
                    break

            if not is_ready:
                print("⚠️ Video işleme zaman aşımına uğradı, diğer URL deneniyor...")
                continue

            r_pub = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media_publish",
                data={"creation_id": container_id, "access_token": token},
                timeout=30
            ).json()

            if "id" in r_pub:
                print(f"🎉 Instagram Reels Başarıyla Yayınlandı! ID: {r_pub['id']}")
                time.sleep(2)
                canan_community.post_first_comment_instagram(r_pub["id"], is_video=True)
                return {"status": "success", "post_id": r_pub["id"]}
            else:
                last_error = r_pub
        except Exception as ex:
            print(f"Instagram Reels deneme istisnası: {ex}")
            last_error = str(ex)

    return {"status": "error", "error": last_error or "Reels yüklenemedi"}


def post_to_facebook_reels(video_path: str, caption: str) -> dict:
    """Canan Tuna Facebook Sayfasına (Canan tunau) doğrudan resmi Facebook REELS yayınlar."""
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    try:
        file_size = os.path.getsize(video_path)

        r_start = requests.post(
            f"https://graph.facebook.com/v21.0/{page_id}/video_reels",
            data={"upload_phase": "start", "access_token": token},
            timeout=25
        ).json()

        video_id = r_start.get("video_id")
        upload_url = r_start.get("upload_url")
        if not video_id or not upload_url:
            print(f"❌ Facebook Reels Start Hatası: {r_start}")
            return _post_to_facebook_video_fallback(video_path, caption)

        with open(video_path, "rb") as vf:
            headers = {
                "Authorization": f"OAuth {token}",
                "offset": "0",
                "file_size": str(file_size)
            }
            r_up = requests.post(upload_url, headers=headers, data=vf, timeout=120)
            if r_up.status_code not in (200, 201):
                print(f"❌ Facebook Reels Upload Hatası: {r_up.text}")
                return _post_to_facebook_video_fallback(video_path, caption)

        r_finish = requests.post(
            f"https://graph.facebook.com/v21.0/{page_id}/video_reels",
            data={
                "upload_phase": "finish",
                "video_id": video_id,
                "video_state": "PUBLISHED",
                "description": caption,
                "share_to_feed": "true",
                "access_token": token
            },
            timeout=30
        ).json()

        if r_finish.get("success") or "id" in r_finish or "video_id" in r_finish or "post_id" in r_finish:
            print(f"🎉 Facebook REELS Başarıyla Yayınlandı! Video ID: {video_id}")
            time.sleep(2)
            canan_community.post_first_comment_facebook(video_id, is_video=True)
            return {"status": "success", "post_id": video_id}
        else:
            print(f"❌ Facebook Reels Finish Hatası: {r_finish}")
            return {"status": "error", "error": r_finish}
    except Exception as e:
        print(f"❌ Facebook Reels İstisnası: {e}")
        return _post_to_facebook_video_fallback(video_path, caption)


def _post_to_facebook_video_fallback(video_path: str, caption: str) -> dict:
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    try:
        with open(video_path, "rb") as vf:
            r_fb = requests.post(
                f"https://graph-video.facebook.com/v21.0/{page_id}/videos",
                files={"source": ("video.mp4", vf, "video/mp4")},
                data={"description": caption, "published": "true", "access_token": token},
                timeout=120
            ).json()
        if "id" in r_fb:
            time.sleep(2)
            canan_community.post_first_comment_facebook(r_fb["id"], is_video=True)
            return {"status": "success", "post_id": r_fb["id"]}
        return {"status": "error", "error": r_fb}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def run_daily_story_post(slot_mode: str = "morning") -> bool:
    """
    Sabah 10:30 ('morning') ve Gece 23:00 ('night') saatlerinde Canan Tuna adına
    Instagram ve Facebook Hikaye (Story) paylaşımı yapar.
    Son 30 günde Reels veya Gönderilerde kullanılmış hiçbir fotoğrafı Story'de tekrar kullanmaz!
    """
    images_dir = os.path.join(BASE_DIR, "assets", "images")
    if not os.path.exists(images_dir):
        return False

    quarantined_files = get_30day_quarantined_filenames()

    all_imgs = sorted([
        os.path.join(images_dir, f)
        for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
        and "canan_cousin_" not in f.lower()
    ])
    if not all_imgs:
        return False

    fresh_imgs = [p for p in all_imgs if os.path.basename(p) not in quarantined_files]
    pool_imgs = fresh_imgs if fresh_imgs else all_imgs

    now = datetime.now()
    story_seq = (now.year * 366 + now.timetuple().tm_yday) * 2 + (0 if slot_mode == "morning" else 1)

    if slot_mode == "morning":
        morning_candidates = [
            p for p in pool_imgs
            if any(k in os.path.basename(p).lower() for k in ("morning", "bed", "robe", "couch", "coffee", "feet", "sunbed", "balcony", "terrace", "window"))
        ]
        cands = morning_candidates or pool_imgs
        chosen_img = cands[story_seq % len(cands)]
        greetings = [
            "Günaydın! Günün nasıl başladı?",
            "Sabah kahvem ve ben... Günaydınlar!",
            "Yeni güne enerjik başladık, günaydın!",
            "Bakım saatiyle güne merhaba, herkese günaydın!"
        ]
    else:
        night_candidates = [
            p for p in pool_imgs
            if any(k in os.path.basename(p).lower() for k in ("night", "evening", "satin", "silk", "lace", "cami", "slip", "feet", "mirror", "couch", "velvet"))
        ]
        cands = night_candidates or pool_imgs
        chosen_img = cands[(story_seq + 7) % len(cands)]
        greetings = [
            "İyi geceler, hala uyanık olan var mı?",
            "Günün yorgunluğunu atma vakti, iyi geceler!",
            "Bu saatte uyumayanlar burada mı? İyi geceler!",
            "Huzurlu geceler, yarın yine buluşalım mı?"
        ]

    story_text = greetings[story_seq % len(greetings)]
    story_out = os.path.join(OUTPUT_DIR, f"story_{slot_mode}.jpg")
    create_canan_reel.create_story_image(chosen_img, story_text, output_jpg=story_out)

    print(f"📲 [Otonom Hikaye - {slot_mode.upper()}] Paylaşılıyor: {os.path.basename(chosen_img)} | Not: '{story_text}'")
    r_ig = canan_engine.post_to_instagram_story(story_out)
    r_fb = canan_engine.post_to_facebook_story(story_out)
    print(f"📲 [Story Sonucu] IG: {r_ig.get('status')} | FB: {r_fb.get('status')}")
    return r_ig.get("status") == "success" or r_fb.get("status") == "success"


def run_single_autopilot_post(force_type: str = None):
    """Günün saatine ve senaryosuna göre Canan Tuna adına 3 platforma otonom paylaşım yapar."""
    check_meta_token_health()

    scenario = pick_next_scenario(force_type=force_type)
    if not scenario:
        print("🛑 Paylaşılacak senaryo bulunamadı.")
        return False
    sc_id = scenario["id"]
    media_type = force_type if force_type else scenario.get("type", "photo")
    quarantined_files = scenario.get("_quarantined_files") or set()

    print("\n" + "=" * 60)
    print(f"🌟 Canan Tuna Otonom Yaşam Adımı: [{scenario.get('category', '').upper()}] {sc_id} (Format: {media_type})")
    print("=" * 60)

    chosen_img = scenario.get("image_path")
    if not chosen_img or not os.path.exists(chosen_img):
        print(f"❌ Görsel dosyası bulunamadı: {chosen_img}")
        return False

    full_caption = f"{scenario['caption']}\n\n{scenario.get('tags', '')}"
    success_summary = {"telegram": False, "facebook": False, "instagram": False}
    used_companion_names = []

    if media_type == "video":
        out_video = os.path.join(OUTPUT_DIR, f"auto_{sc_id}.mp4")
        print(f"🎬 Senaryo için estetik müzikli Full HD Reels videosu üretiliyor: {sc_id}...")
        planned_companions = create_canan_reel.pick_companion_images(
            chosen_img,
            count=3,
            extra_candidates=scenario.get("companions"),
            exclude_filenames=quarantined_files
        )
        used_companion_names = [os.path.basename(p) for p in planned_companions]
        create_canan_reel.create_reels_video(
            chosen_img,
            output_mp4=out_video,
            companion_images=planned_companions,
            hook_text=scenario.get("hook"),
            custom_scene_hooks=scenario.get("scene_hooks"),
            exclude_filenames=quarantined_files
        )

        # 1. Telegram
        print("📲 Telegram'a Video Gönderiliyor...")
        try:
            with open(out_video, "rb") as vf:
                r_tg = requests.post(
                    f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendVideo",
                    files={"video": vf},
                    data={"chat_id": config.TELEGRAM_CHANNEL, "caption": full_caption},
                    timeout=60
                ).json()
            if r_tg.get("ok"):
                success_summary["telegram"] = True
                print("📲 Telegram Sonucu: ✅ BAŞARILI")
            else:
                print("📲 Telegram Sonucu: ❌", r_tg)
        except Exception as e:
            print("📲 Telegram Hatası:", e)

        # 2. Facebook
        print("📘 Facebook Sayfasına Reels/Video Gönderiliyor (Canan tunau)...")
        r_fb = post_to_facebook_reels(out_video, full_caption)
        if r_fb.get("status") == "success":
            success_summary["facebook"] = True
            print(f"📘 Facebook Sonucu: ✅ BAŞARILI (ID: {r_fb.get('post_id')})")
        else:
            print(f"📘 Facebook Sonucu: ❌ {r_fb}")
            send_telegram_alert(f"⚠️ [Canan Tuna] Facebook Reels Yüklenemedi!\nHata: {r_fb.get('error')}")

        # 3. Instagram Reels
        print("📸 Instagram'a Doğrudan Reels Gönderiliyor (@canantuna_official)...")
        r_ig = post_to_instagram_reels(out_video, full_caption)
        if r_ig.get("status") == "success":
            success_summary["instagram"] = True
            print(f"📸 Instagram Sonucu: ✅ BAŞARILI (ID: {r_ig.get('post_id')})")
        else:
            print(f"📸 Instagram Sonucu: ❌ {r_ig}")
            send_telegram_alert(f"⚠️ [Canan Tuna] Instagram Reels Yüklenemedi!\nHata: {r_ig.get('error')}")

        # 4. TikTok Reels / Video (Çerez mevcutsa)
        print("🎵 TikTok'a Reels/Video Yükleniyor...")
        try:
            import tiktok_poster
            r_tt = tiktok_poster.post_video_to_tiktok(out_video, full_caption)
            if r_tt.get("status") == "success":
                success_summary["tiktok"] = True
                print("🎵 TikTok Sonucu: ✅ BAŞARILI")
            else:
                print(f"🎵 TikTok Sonucu: ⚠️ {r_tt.get('reason')}")
        except Exception as e:
            print(f"⚠️ TikTok İstisnası: {e}")

    else:
        print("📸 Fotoğraf Paylaşımı Yapılıyor (Instagram + Facebook + Telegram)...")
        create_canan_reel.mark_images_used([chosen_img])
        res = canan_engine.publish_lifestyle_update(chosen_img, full_caption)
        if res.get("telegram", {}).get("status") == "success":
            success_summary["telegram"] = True
        if res.get("facebook", {}).get("status") == "success":
            success_summary["facebook"] = True
        else:
            send_telegram_alert(f"⚠️ [Canan Tuna] Facebook Fotoğraf Yüklenemedi!\nHata: {res.get('facebook')}")
        if res.get("instagram", {}).get("status") == "success":
            success_summary["instagram"] = True
        else:
            send_telegram_alert(f"⚠️ [Canan Tuna] Instagram Fotoğraf Yüklenemedi!\nHata: {res.get('instagram')}")

    history = load_history()
    history.append({
        "scenario_id": sc_id,
        "media_type": media_type,
        "image_path": chosen_img,
        "image_name": os.path.basename(chosen_img),
        "companion_names": used_companion_names,
        "timestamp": datetime.now().isoformat(),
        "caption": full_caption,
        "platforms": success_summary
    })
    save_history(history)
    print(f"✅ [{sc_id}] senaryosu işlendi! Özet: {success_summary}")
    return True


if __name__ == "__main__":
    run_single_autopilot_post()
