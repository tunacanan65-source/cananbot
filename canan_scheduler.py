import os
import sys
import time
import threading
from datetime import datetime, timezone, timedelta
import requests
import config
import canan_autopilot

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Türkiye Saati (TSİ / UTC+3)
TR_TZ = timezone(timedelta(hours=3))

# Günlük 2 Reels Videosu (Öğlen + Akşam) + Haftada 1 Vitrin Fotoğrafı (Pazar)
# window_start - window_end: Sunucu o an uyuyakalsa bile bu saat aralığında uyanınca telafi (catch-up) yapar!
SCHEDULE_SLOTS = [
    {
        "id": "noon_reels",
        "hour": 13,
        "minute": 0,
        "window_end_hour": 17,
        "check_start_hour": 11,
        "check_end_hour": 17,
        "label": "Öğlen Reels Videosu",
        "type": "video"
    },
    {
        "id": "sunday_photo",
        "hour": 16,
        "minute": 30,
        "window_end_hour": 19,
        "check_start_hour": 16,
        "check_end_hour": 19,
        "label": "Pazar Haftalık Vitrin Fotoğrafı",
        "type": "photo",
        "day_of_week": 6
    },
    {
        "id": "evening_reels",
        "hour": 20,
        "minute": 30,
        "window_end_hour": 23,
        "check_start_hour": 19,
        "check_end_hour": 24,
        "label": "Akşam Reels Videosu",
        "type": "video"
    }
]


def get_today_instagram_posts_tr() -> list:
    """
    Instagram Graph API'den bugünün (TSİ) paylaşımlarını canlı çeker.
    Sunucu yeniden başlasa bile aynı slotta mükerrer paylaşım yapılmasını önler
    ve uyku nedeniyle kaçan paylaşımları tespit eder.
    """
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    if not ig_id or not token:
        return []

    today_tr = datetime.now(TR_TZ).date()
    today_posts = []
    try:
        url = f"https://graph.facebook.com/v21.0/{ig_id}/media?fields=id,timestamp,media_type&limit=10&access_token={token}"
        resp = requests.get(url, timeout=12).json()
        for item in resp.get("data", []):
            ts_str = item.get("timestamp", "")
            if not ts_str:
                continue
            # Örn: 2026-11-04T10:01:54+0000
            dt_utc = datetime.strptime(ts_str[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
            dt_tr = dt_utc.astimezone(TR_TZ)
            if dt_tr.date() == today_tr:
                today_posts.append({
                    "hour": dt_tr.hour,
                    "minute": dt_tr.minute,
                    "media_type": item.get("media_type", "")
                })
    except Exception as e:
        print(f"⚠️ [Zamanlayıcı] Canlı Instagram kontrol uyarısı: {e}")
    return today_posts


def has_slot_posted_today(slot: dict, today_posts: list) -> bool:
    """Belirtilen slot aralığında bugün Instagram'da paylaşım yapılıp yapılmadığını döner."""
    for p in today_posts:
        if slot["check_start_hour"] <= p["hour"] < slot["check_end_hour"]:
            if slot["type"] == "photo" and p["media_type"] != "IMAGE":
                continue
            return True
    return False


def start_self_keepalive():
    """Render sunucusunun 15 dakikalık uyku moduna girmesini önlemek için her 5 dakikada bir dış URL'yi dürter."""
    def _ping_loop():
        base_url = getattr(config, "BASE_URL", "https://cananbot.onrender.com").rstrip("/")
        ping_url = f"{base_url}/health"
        while True:
            time.sleep(280)  # 4 dk 40 sn
            try:
                requests.get(ping_url, timeout=15)
            except Exception:
                pass

    t = threading.Thread(target=_ping_loop, daemon=True)
    t.start()


def run_scheduler():
    print("=" * 60)
    print("🚀 Canan Tuna 7/24 Otonom Zamanlayıcı & Telafi Kalkanı Devrede!")
    print("📅 Günlük Plan (Türkiye Saati - TSİ):")
    print("   - 13:00 (Telafi penceresi 13:00-17:00): Öğlen Reels Videosu")
    print("   - 20:30 (Telafi penceresi 20:30-23:15): Akşam Reels Videosu")
    print("   - Pazar 16:30: Haftalık Vitrin Fotoğrafı")
    print("=" * 60)

    start_self_keepalive()
    last_posted_date_slot = {}

    while True:
        try:
            now = datetime.now(TR_TZ)
            today_str = now.strftime("%Y-%m-%d")
            now_minutes = now.hour * 60 + now.minute

            for slot in SCHEDULE_SLOTS:
                if "day_of_week" in slot and now.weekday() != slot["day_of_week"]:
                    continue

                slot_key = f"{today_str}_{slot['id']}"
                if slot_key in last_posted_date_slot:
                    continue

                target_minutes = slot["hour"] * 60 + slot["minute"]
                end_minutes = slot["window_end_hour"] * 60 + 15

                # Paylaşım vakti geldiyse veya telafi penceresi içindeysek
                if target_minutes <= now_minutes <= end_minutes:
                    today_posts = get_today_instagram_posts_tr()
                    if has_slot_posted_today(slot, today_posts):
                        print(f"✅ [Zamanlayıcı] {slot['label']} bugün zaten Instagram'da paylaşılmış, atlanıyor.")
                        last_posted_date_slot[slot_key] = True
                        continue

                    print(f"\n🚀 [VAKİT GELDİ - TSİ {now.strftime('%H:%M')}] {slot['label']} ateşleniyor... (Tip: {slot['type']})")
                    ok = canan_autopilot.run_single_autopilot_post(force_type=slot["type"])
                    if ok:
                        last_posted_date_slot[slot_key] = True
                    time.sleep(65)

            time.sleep(25)
        except Exception as e:
            print(f"⚠️ Zamanlayıcı istisnası: {e}")
            time.sleep(30)


if __name__ == "__main__":
    run_scheduler()
