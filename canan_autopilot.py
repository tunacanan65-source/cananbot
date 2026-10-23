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

    # force_type verilmişse ("video" veya "photo") öncelikle ona uygun senaryoyu seç
    if force_type:
        type_candidates = [s for s in available if s.get("type") == force_type]
        if type_candidates:
            return random.choice(type_candidates)
        # Eğer available içinde o tipten kalmamışsa tüm listeden o tipe ait olanı al
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
    try:
        video_url = None
        # 1. Catbox dene
        try:
            with open(video_path, "rb") as f:
                r_up = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=45)
                if r_up.status_code == 200 and r_up.text.strip().startswith("http"):
                    video_url = r_up.text.strip()
        except Exception as e:
            print(f"Catbox yükleme uyarısı: {e}")

        # 2. Tmpfiles fallback
        if not video_url:
            with open(video_path, "rb") as f:
                r_tf = requests.post("https://tmpfiles.org/api/v1/upload", files={"file": f}, timeout=45).json()
                if r_tf.get("status") == "success":
                    raw_url = r_tf["data"]["url"]
                    video_url = raw_url.replace("tmpfiles.org/", "tmpfiles.org/dl/")

        if not video_url:
            return {"status": "error", "error": "Video public CDN'e yüklenemedi"}

        print(f"🌐 Video CDN URL: {video_url}")

        # 1. Reels Container oluştur
        r_c = requests.post(
            f"https://graph.facebook.com/v21.0/{ig_id}/media",
            data={"media_type": "REELS", "video_url": video_url, "caption": caption, "access_token": config.FACEBOOK_ACCESS_TOKEN},
            timeout=25
        ).json()
        container_id = r_c.get("id")
        if not container_id:
            print(f"❌ Instagram Reels Container Hatası: {r_c}")
            return {"status": "error", "error": r_c}

        # 2. Render bitişini bekle (Instagram video işleme)
        for i in range(15):
            time.sleep(5)
            st = requests.get(f"https://graph.facebook.com/v21.0/{container_id}?fields=status_code&access_token={config.FACEBOOK_ACCESS_TOKEN}").json()
            code = st.get("status_code")
            print(f"⏳ Instagram Reels İşleme Durumu ({i+1}/15): {code}")
            if code == "FINISHED":
                break
            if code == "ERROR":
                return {"status": "error", "error": st}

        # 3. Yayınla
        r_pub = requests.post(
            f"https://graph.facebook.com/v21.0/{ig_id}/media_publish",
            data={"creation_id": container_id, "access_token": config.FACEBOOK_ACCESS_TOKEN},
            timeout=25
        ).json()
        if "id" in r_pub:
            return {"status": "success", "post_id": r_pub["id"]}
        return {"status": "error", "error": r_pub}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def run_single_autopilot_post(force_type: str = None):
    """Günün saatine ve senaryosuna göre Canan Tuna adına 3 platforma (Instagram, Facebook, Telegram) otonom paylaşım yapar."""
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

    if media_type == "video":
        out_video = os.path.join(OUTPUT_DIR, f"auto_{sc_id}.mp4")
        print(f"🎬 Senaryo için estetik lofi müzikli Reels videosu üretiliyor: {sc_id}...")
        create_canan_reel.create_reels_video(chosen_img, output_mp4=out_video)

        # 1. Telegram
        print("📲 Telegram'a Video Gönderiliyor...")
        r_tg = requests.post(
            f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendVideo",
            files={"video": open(out_video, "rb")},
            data={"chat_id": config.TELEGRAM_CHANNEL, "caption": full_caption},
            timeout=60
        ).json()
        print("📲 Telegram Sonucu:", "✅ BAŞARILI" if r_tg.get("ok") else r_tg)

        # 2. Facebook
        print("📘 Facebook Sayfasına Reels/Video Gönderiliyor (Canan tunau)...")
        r_fb = requests.post(
            f"https://graph-video.facebook.com/v21.0/{config.FACEBOOK_PAGE_ID}/videos",
            files={"source": open(out_video, "rb")},
            data={"description": full_caption, "access_token": config.FACEBOOK_ACCESS_TOKEN},
            timeout=90
        ).json()
        print("📘 Facebook Sonucu:", "✅ BAŞARILI" if "id" in r_fb else r_fb)

        # 3. Instagram Reels
        print("📸 Instagram'a Doğrudan Reels Gönderiliyor (@canantuna_official)...")
        r_ig = post_to_instagram_reels(out_video, full_caption)
        print("📸 Instagram Sonucu:", "✅ BAŞARILI" if r_ig.get("status") == "success" else r_ig)
    else:
        print("📸 Fotoğraf Paylaşımı Yapılıyor (Instagram + Facebook + Telegram)...")
        canan_engine.publish_lifestyle_update(chosen_img, full_caption)

    # Geçmişe kaydet
    history = load_history()
    history.append({
        "scenario_id": sc_id,
        "media_type": media_type,
        "image_path": chosen_img,
        "image_name": os.path.basename(chosen_img),
        "timestamp": datetime.now().isoformat(),
        "caption": full_caption
    })
    save_history(history)
    print(f"✅ [{sc_id}] senaryosu başarıyla tamamlandı ve geçmişe işlendi!")
    return True

if __name__ == "__main__":
    run_single_autopilot_post()
