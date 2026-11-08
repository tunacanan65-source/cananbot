import os
import sys
import time
import requests
import config
import canan_community

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
                post_id = res_json.get("post_id", res_json["id"])
                time.sleep(2)
                canan_community.post_first_comment_facebook(post_id, is_video=False)
                return {"status": "success", "post_id": post_id}
            return {"status": "error", "error": res_json}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def post_to_instagram_photo(image_path: str, caption: str) -> dict:
    """Canan Tuna Instagram hesabına (@canantuna_official) doğrudan fotoğraf yayınlar."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    img_name = os.path.basename(image_path)
    base_url = getattr(config, "BASE_URL", "https://cananbot.onrender.com").rstrip("/")

    candidate_urls = [
        f"{base_url}/images/{img_name}",
        f"{base_url}/media/{img_name}"
    ]

    try:
        with open(image_path, "rb") as f:
            r_up = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=25)
            if r_up.status_code == 200 and r_up.text.strip().startswith("http"):
                candidate_urls.append(r_up.text.strip())
    except Exception as e:
        print(f"Catbox uyarısı: {e}")

    last_error = None
    for img_url in candidate_urls:
        try:
            r_c = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media",
                data={"image_url": img_url, "caption": caption, "access_token": token},
                timeout=25
            ).json()
            container_id = r_c.get("id")
            if not container_id:
                last_error = r_c
                continue

            time.sleep(3)
            r_pub = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media_publish",
                data={"creation_id": container_id, "access_token": token},
                timeout=25
            ).json()
            if "id" in r_pub:
                media_id = r_pub["id"]
                time.sleep(2)
                canan_community.post_first_comment_instagram(media_id, is_video=False)
                return {"status": "success", "post_id": media_id}
            last_error = r_pub
        except Exception as e:
            last_error = str(e)

    return {"status": "error", "error": last_error or "Fotoğraf yüklenemedi"}


def post_to_instagram_story(story_image_path: str) -> dict:
    """Canan Tuna Instagram hesabına (@canantuna_official) doğrudan 24 saatlik HİKAYE (Story) yayınlar."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    img_name = os.path.basename(story_image_path)
    base_url = getattr(config, "BASE_URL", "https://cananbot.onrender.com").rstrip("/")

    candidate_urls = [f"{base_url}/media/{img_name}"]
    try:
        with open(story_image_path, "rb") as f:
            r_up = requests.post("https://catbox.moe/user/api.php", data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=25)
            if r_up.status_code == 200 and r_up.text.strip().startswith("http"):
                candidate_urls.append(r_up.text.strip())
    except Exception:
        pass

    last_error = None
    for img_url in candidate_urls:
        try:
            r_c = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media",
                data={
                    "media_type": "STORIES",
                    "image_url": img_url,
                    "access_token": token
                },
                timeout=25
            ).json()
            container_id = r_c.get("id")
            if not container_id:
                last_error = r_c
                continue
            time.sleep(4)
            r_pub = requests.post(
                f"https://graph.facebook.com/v21.0/{ig_id}/media_publish",
                data={"creation_id": container_id, "access_token": token},
                timeout=25
            ).json()
            if "id" in r_pub:
                return {"status": "success", "story_id": r_pub["id"]}
            last_error = r_pub
        except Exception as e:
            last_error = str(e)
    return {"status": "error", "error": last_error}


def post_to_facebook_story(story_image_path: str) -> dict:
    """Canan Tuna Facebook Sayfasına doğrudan 24 saatlik Fotoğraf Hikayesi (Story) yayınlar."""
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    try:
        with open(story_image_path, "rb") as f:
            r_photo = requests.post(
                f"https://graph.facebook.com/v21.0/{page_id}/photos",
                files={"source": f},
                data={"published": "false", "access_token": token},
                timeout=35
            ).json()
        photo_id = r_photo.get("id")
        if not photo_id:
            return {"status": "error", "error": r_photo}

        r_story = requests.post(
            f"https://graph.facebook.com/v21.0/{page_id}/photo_stories",
            data={"photo_id": photo_id, "access_token": token},
            timeout=25
        ).json()
        if r_story.get("success") or "post_id" in r_story:
            return {"status": "success", "story_id": r_story.get("post_id", photo_id)}
        return {"status": "error", "error": r_story}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def publish_lifestyle_update(image_path: str, caption: str) -> dict:
    """Hem Instagram, hem Facebook hem Telegram kanalına eşzamanlı yayınlar."""
    print("=" * 60)
    print("💃 Canan Tuna Yayına Başlıyor (3 Platform Birden)...")
    print(f"📸 Görsel: {image_path}")
    print(f"✍️ Açıklama: {caption}")
    print("=" * 60)

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
