import os
import sys
import time
import requests
import config

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def post_to_telegram(image_path: str, caption: str) -> dict:
    """Canan Tuna Telegram Kanalına (@canantunaaa) fotoğraf ve kısa etkileşim metni yayınlar."""
    if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_CHANNEL:
        return {"status": "error", "message": "Telegram yapılandırması eksik"}

    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendPhoto"
    try:
        with open(image_path, "rb") as f:
            files = {"photo": f}
            data = {"chat_id": config.TELEGRAM_CHANNEL, "caption": caption}
            resp = requests.post(url, files=files, data=data, timeout=30)
            res_json = resp.json()
            if res_json.get("ok"):
                return {"status": "success", "message_id": res_json["result"]["message_id"]}
            return {"status": "error", "error": res_json}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def post_to_facebook(image_path: str, caption: str) -> dict:
    """Canan Tuna Facebook Sayfasına (Canan tunau) fotoğraf ve kısa etkileşim metni yayınlar."""
    if not config.FACEBOOK_ACCESS_TOKEN or not config.FACEBOOK_PAGE_ID:
        return {"status": "error", "message": "Facebook yapılandırması eksik"}

    url = f"https://graph.facebook.com/v21.0/{config.FACEBOOK_PAGE_ID}/photos"
    try:
        with open(image_path, "rb") as f:
            files = {"source": f}
            data = {"caption": caption, "access_token": config.FACEBOOK_ACCESS_TOKEN}
            resp = requests.post(url, files=files, data=data, timeout=45)
            res_json = resp.json()
            if "id" in res_json:
                return {"status": "success", "post_id": res_json.get("post_id", res_json["id"])}
            return {"status": "error", "error": res_json}
    except Exception as e:
        return {"status": "error", "error": str(e)}

def post_to_instagram_photo(image_path: str, caption: str) -> dict:
    """Canan Tuna Instagram hesabına (@canantuna_official) doğrudan fotoğraf yayınlar."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    try:
        with open(image_path, "rb") as f:
            r_up = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=25)
            img_url = r_up.text.strip()

        # 1. Container oluştur
        r_c = requests.post(
            f"https://graph.facebook.com/v21.0/{ig_id}/media",
            data={"image_url": img_url, "caption": caption, "access_token": config.FACEBOOK_ACCESS_TOKEN},
            timeout=25
        ).json()
        container_id = r_c.get("id")
        if not container_id:
            return {"status": "error", "error": r_c}

        time.sleep(3)
        # 2. Yayınla
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

def publish_lifestyle_update(image_path: str, caption: str) -> dict:
    """Hem Instagram, hem Facebook hem Telegram kanalına eşzamanlı yayınlar."""
    print("="*60)
    print("💃 Canan Tuna Yayına Başlıyor (3 Platform Birden)...")
    print(f"📸 Görsel: {image_path}")
    print(f"✍️ Açıklama: {caption}")
    print("="*60)

    tg_res = post_to_telegram(image_path, caption)
    print(f"📲 Telegram Paylaşımı: {'✅ BAŞARILI' if tg_res.get('status') == 'success' else '❌ ' + str(tg_res)}")

    fb_res = post_to_facebook(image_path, caption)
    print(f"📘 Facebook Paylaşımı: {'✅ BAŞARILI' if fb_res.get('status') == 'success' else '❌ ' + str(fb_res)}")

    ig_res = post_to_instagram_photo(image_path, caption)
    print(f"📸 Instagram Paylaşımı: {'✅ BAŞARILI' if ig_res.get('status') == 'success' else '❌ ' + str(ig_res)}")

    return {
        "telegram": tg_res,
        "facebook": fb_res,
        "instagram": ig_res
    }
