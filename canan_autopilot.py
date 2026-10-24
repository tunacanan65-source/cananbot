import os
import sys
import json
import time
import random
from datetime import datetime
import requests
import config
import life_scenarios
import canan_engine
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
        r = requests.get(f"https://graph.facebook.com/v21.0/{page_id}?fields=id,name&access_token={token}", timeout=8).json()
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

def pick_next_scenario(force_type: str = None) -> dict:
    history = load_history()
    used_ids = {h.get("scenario_id") for h in history}
    used_images = {os.path.basename(h.get("image_path", "")) for h in history if h.get("image_path")}

    available = [
        s for s in life_scenarios.SCENARIOS
        if s["id"] not in used_ids and os.path.basename(s.get("image_path", "")) not in used_images
    ]
    if not available:
        print("⚠️ [BİLGİ] Tüm senaryolar paylaşıldı. Döngü devamı için geçmiş sıfırlanıyor...")
        history = []
        save_history([])
        available = list(life_scenarios.SCENARIOS)

    if force_type:
        type_candidates = [s for s in available if s.get("type") == force_type]
        if type_candidates:
            return random.choice(type_candidates)
        all_type_candidates = [s for s in life_scenarios.SCENARIOS if s.get("type") == force_type]
        if all_type_candidates:
            return random.choice(all_type_candidates)

    hour = datetime.now().hour
    if 7 <= hour < 12:
        preferred = [s for s in available if s.get("category") in ("ev", "spor")]
    elif 12 <= hour < 17:
        preferred = [s for s in available if s.get("category") in ("sokak", "tatil")]
    elif 17 <= hour < 21:
        preferred = [s for s in available if s.get("category") in ("spor", "sokak")]
    else:
        preferred = [s for s in available if s.get("category") in ("gece", "ev")]

    return random.choice(preferred if preferred else available)

def post_to_instagram_reels(video_path: str, caption: str) -> dict:
    """Canan Tuna Instagram hesabına (@canantuna_official) doğrudan Reels yayınlar."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    video_filename = os.path.basename(video_path)

    # 1. Video URL belirleme: Öncelikle Render'ın kendi güvenli HTTPS linki
    candidate_urls = []
    base_url = getattr(config, "BASE_URL", "https://cananbot.onrender.com").rstrip("/")
    candidate_urls.append(f"{base_url}/media/{video_filename}")

    # Fallback CDN'ler
    try:
        with open(video_path, "rb") as f:
            r_up = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=40)
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
            # 1. Reels Container oluştur
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

            # 2. Render / Video işleme bitişini bekle (30 x 5 sn = 150 saniye)
            is_ready = False
            for i in range(30):
                time.sleep(5)
                st = requests.get(f"https://graph.facebook.com/v21.0/{container_id}?fields=status_code&access_token={token}", timeout=15).json()
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

            # 3. Yayınla
            r_pub = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media_publish",
                data={"creation_id": container_id, "access_token": token},
                timeout=30
            ).json()

            if "id" in r_pub:
                print(f"🎉 Instagram Reels Başarıyla Yayınlandı! ID: {r_pub['id']}")
                return {"status": "success", "post_id": r_pub["id"]}
            else:
                last_error = r_pub
        except Exception as ex:
            print(f"Instagram Reels deneme istisnası: {ex}")
            last_error = str(ex)

    return {"status": "error", "error": last_error or "Reels yüklenemedi"}

def post_to_facebook_video(video_path: str, caption: str) -> dict:
    """Canan Tuna Facebook Sayfasına (Canan tunau) doğrudan Reels/Video yayınlar."""
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    try:
        with open(video_path, "rb") as vf:
            r_fb = requests.post(
                f"https://graph-video.facebook.com/v21.0/{page_id}/videos",
                files={"source": ("video.mp4", vf, "video/mp4")},
                data={"description": caption, "access_token": token},
                timeout=120
            ).json()
        if "id" in r_fb:
            return {"status": "success", "post_id": r_fb["id"]}
        return {"status": "error", "error": r_fb}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def run_single_autopilot_post(force_type: str = None):
    """Günün saatine ve senaryosuna göre Canan Tuna adına 3 platforma (Instagram, Facebook, Telegram) otonom paylaşım yapar."""
    # Ön kontrol: Token geçerliliği
    check_meta_token_health()

    scenario = pick_next_scenario(force_type=force_type)
    if not scenario:
        print("🛑 Paylaşılacak senaryo bulunamadı.")
        return False
    sc_id = scenario["id"]
    media_type = force_type if force_type else scenario.get("type", "photo")

    print("\n" + "="*60)
    print(f"🌟 Canan Tuna Otonom Yaşam Adımı: [{scenario.get('category').upper()}] {sc_id} (Format: {media_type})")
    print("="*60)

    chosen_img = scenario.get("image_path")
    if not chosen_img or not os.path.exists(chosen_img):
        print(f"❌ Görsel dosyası bulunamadı: {chosen_img}")
        return False

    full_caption = f"{scenario['caption']}\n\n{scenario.get('tags', '')}"

    success_summary = {"telegram": False, "facebook": False, "instagram": False}

    if media_type == "video":
        out_video = os.path.join(OUTPUT_DIR, f"auto_{sc_id}.mp4")
        print(f"🎬 Senaryo için estetik lofi müzikli Reels videosu üretiliyor: {sc_id}...")
        create_canan_reel.create_reels_video(chosen_img, output_mp4=out_video)

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
        r_fb = post_to_facebook_video(out_video, full_caption)
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
    else:
        print("📸 Fotoğraf Paylaşımı Yapılıyor (Instagram + Facebook + Telegram)...")
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

    # Geçmişe kaydet
    history = load_history()
    history.append({
        "scenario_id": sc_id,
        "media_type": media_type,
        "image_path": chosen_img,
        "image_name": os.path.basename(chosen_img),
        "timestamp": datetime.now().isoformat(),
        "caption": full_caption,
        "platforms": success_summary
    })
    save_history(history)
    print(f"✅ [{sc_id}] senaryosu işlendi! Özet: {success_summary}")
    return True

if __name__ == "__main__":
    run_single_autopilot_post()
