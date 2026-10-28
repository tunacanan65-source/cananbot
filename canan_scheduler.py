import os
import sys
import time
from datetime import datetime, timezone, timedelta
import canan_autopilot

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Türkiye Saati (TSİ / UTC+3)
TR_TZ = timezone(timedelta(hours=3))

# Günlük 2 Reels Videosu (Öğlen + Akşam) + Haftada 1 Vitrin Fotoğrafı (Pazar)
# 13:00 -> Öğlen Reels Videosu (Tatil / Yaşam / Estetik Dikey Video)
# 20:30 -> Akşam Reels Videosu (Gece / Spor / Lifestyle Dikey Video)
# Pazar 16:30 -> Haftalık Vitrin Fotoğrafı (Estetik Ana Akış Gönderisi)
SCHEDULE_SLOTS = [
    {"hour": 13, "minute": 0, "label": "Öğlen Reels Videosu", "type": "video"},
    {"hour": 20, "minute": 30, "label": "Akşam Reels Videosu", "type": "video"},
    {"hour": 16, "minute": 30, "label": "Pazar Haftalık Vitrin Fotoğrafı", "type": "photo", "day_of_week": 6}
]

def run_scheduler():
    print("="*60)
    print("🚀 Canan Tuna 7/24 Otonom Zamanlayıcı Devrede!")
    print("📅 Günlük Plan (Türkiye Saati - TSİ):")
    print("   - 13:00: Öğlen Reels Videosu (Dikey Video)")
    print("   - 20:30: Akşam Reels Videosu (Dikey Video)")
    print("   - Pazar 16:30: Haftalık Vitrin Fotoğrafı")
    print("="*60)

    last_posted_date_slot = {}

    while True:
        try:
            # Türkiye saatini al (Sunucu Amerika'da veya Almanya'da olsa bile TSİ baz alınır)
            now = datetime.now(TR_TZ)
            today_str = now.strftime("%Y-%m-%d")

            for slot in SCHEDULE_SLOTS:
                # Belirli bir güne özgüyse kontrol et (Örn: Pazar vitrin fotoğrafı)
                if "day_of_week" in slot and now.weekday() != slot["day_of_week"]:
                    continue

                slot_key = f"{today_str}_{slot['hour']}_{slot['minute']}"

                # Slot saati kontrolü
                if now.hour == slot["hour"] and now.minute >= slot["minute"]:
                    if slot_key not in last_posted_date_slot:
                        print(f"\n🚀 [VAKİT GELDİ - TSİ {now.strftime('%H:%M')}] {slot['label']} ateşleniyor... (Tip: {slot['type']})")
                        canan_autopilot.run_single_autopilot_post(force_type=slot["type"])
                        last_posted_date_slot[slot_key] = True
                        time.sleep(65)

            time.sleep(20)
        except Exception as e:
            print(f"⚠️ Zamanlayıcı istisnası: {e}")
            time.sleep(30)

if __name__ == "__main__":
    run_scheduler()
