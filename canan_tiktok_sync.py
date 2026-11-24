"""
Canan Tuna - 7/24 Otomatik TikTok Reels Senkronizasyon Nöbetçisi
- Render sunucusunun her gün 12:00 ve 21:00'de Instagram'a attığı yeni Reels videolarını
  otomatik tespit eder, 1080x1920 Full HD videoyu indirir ve @canantuna06 TikTok hesabına
  doğrudan senin ev internetin (Türk Ev IP'si) üzerinden otomatik yükler!
- Ayrıca bilgisayar kapalıyken kaçırılmış bir Reels varsa, bilgisayar açıldığı anda
  eksik olan son Reels videosunu yakalayıp TikTok'a tamamlar.
"""
import os
import sys
import time
import json
import requests
from datetime import datetime
import config
import tiktok_poster

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
SYNC_STATE_FILE = os.path.join(BASE_DIR, "tiktok_synced_ids.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_synced_ids() -> list:
    if os.path.exists(SYNC_STATE_FILE):
        try:
            with open(SYNC_STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_synced_ids(ids: list):
    with open(SYNC_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(ids[-200:], f, ensure_ascii=False, indent=2)


def get_latest_instagram_reels(limit: int = 5) -> list:
    """Instagram Graph API üzerinden Canan'ın son paylaştığı VIDEO/REELS gönderilerini çeker."""
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    if not ig_id or not token:
        return []

    url = (
        f"https://graph.facebook.com/v21.0/{ig_id}/media"
        f"?fields=id,media_type,media_product_type,media_url,caption,timestamp"
        f"&limit={limit}&access_token={token}"
    )
    try:
        resp = requests.get(url, timeout=15).json()
        reels = []
        for item in resp.get("data", []):
            if item.get("media_type") == "VIDEO" and item.get("media_url"):
                reels.append(item)
        return reels
    except Exception as e:
        print(f"⚠️ [TikTok Sync] Instagram sorgu uyarısı: {e}")
        return []


def sync_once(seed_existing: bool = False) -> bool:
    """Yeni paylaşılmış Instagram Reels videosu varsa indirip TikTok'a yükler."""
    synced_ids = load_synced_ids()
    latest_reels = get_latest_instagram_reels(limit=5)
    if not latest_reels:
        return False

    # İlk kurulumda geçmişteki eski videoları bir anda üst üste yüklememek için mevcut ID'leri kaydet
    if seed_existing and not synced_ids:
        for r in latest_reels:
            synced_ids.append(r["id"])
        save_synced_ids(synced_ids)
        print(f"✅ [TikTok Sync] Mevcut {len(synced_ids)} eski Reels ID'si referans olarak kaydedildi.")
        return True

    # En yeni Reels henüz TikTok'a atılmamışsa hemen indir ve yükle
    newest = latest_reels[0]
    ig_post_id = newest["id"]
    if ig_post_id in synced_ids:
        return False

    media_url = newest.get("media_url")
    raw_caption = (newest.get("caption") or "").strip()
    first_line = raw_caption.split("\n")[0].strip() if raw_caption else "4 kareden favorin hangisi? Yoruma yaz!"
    tiktok_caption = f"{first_line[:140]} #canantuna #keşfet #fyp #kombin #reels"

    local_mp4 = os.path.join(OUTPUT_DIR, f"tiktok_sync_{ig_post_id}.mp4")
    print(f"📥 [TikTok Sync] Yeni Instagram Reels tespit edildi ({ig_post_id}), indiriliyor...")
    try:
        r_vid = requests.get(media_url, timeout=60)
        if r_vid.status_code != 200 or len(r_vid.content) < 50000:
            print("❌ [TikTok Sync] Video indirilemedi.")
            return False
        with open(local_mp4, "wb") as vf:
            vf.write(r_vid.content)
    except Exception as e:
        print(f"❌ [TikTok Sync] Video indirme hatası: {e}")
        return False

    print(f"🚀 [TikTok Sync] @canantuna06 hesabına yükleniyor: {tiktok_caption}")
    res = tiktok_poster.post_video_to_tiktok(local_mp4, tiktok_caption)
    if res.get("status") == "success":
        synced_ids.append(ig_post_id)
        save_synced_ids(synced_ids)
        print(f"🎉 [TikTok Sync] Başarıyla TikTok'ta yayınlandı! (IG ID: {ig_post_id})")
        return True
    else:
        print(f"⚠️ [TikTok Sync] Yükleme uyarısı: {res}")
        return False


def run_daemon(poll_seconds: int = 600):
    print("=" * 65)
    print("🎵 CANAN TUNA (@canantuna06) 7/24 OTOMATİK TİKTOK SENKRON NÖBETÇİSİ")
    print("=" * 65)
    sync_once(seed_existing=True)
    while True:
        try:
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now_str}] 🔍 Yeni Reels kontrol ediliyor...")
            sync_once(seed_existing=False)
        except Exception as e:
            print(f"⚠️ Döngü hatası: {e}")
        time.sleep(poll_seconds)


if __name__ == "__main__":
    if "--once" in sys.argv:
        sync_once(seed_existing=False)
    elif "--seed" in sys.argv:
        sync_once(seed_existing=True)
    else:
        run_daemon()
