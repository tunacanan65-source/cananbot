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

# Günlük 2 Paylaşım: 1 Hikaye (Öğlen) + 1 Reels Videosu (Akşam)
# 13:00 -> Fotoğraf / Hikaye (Günlük Yaşam / Kombin / Kafe)
# 20:30 -> Reels Videosu (Sesli Dikey Video / Gece / Spor / Motivasyon)
SCHEDULE_SLOTS = [
    {"hour": 13, "minute": 0, "label": "Öğlen Hikayesi", "type": "photo"},
    {"hour": 20, "minute": 30, "label": "Akşam Reels Videosu", "type": "video"}
]

def run_scheduler():
    print("="*60)
    print("⏰ Canan Tuna 7/24 Otonom Zamanlayıcı Devrede!")
    print("📅 Günlük Plan (Türkiye Saati - TSİ):")
    print("   - 13:00: Öğlen Hikayesi (Fotoğraf)")
    print("   - 20:30: Akşam Reels Videosu (Sesli Video)")
    print("="*60)

    last_posted_date_slot = {}

    while True:
        try:
            # Türkiye saatini al (Sunucu Amerika'da veya Almanya'da olsa bile TSİ baz alınır)
            now = datetime.now(TR_TZ)
            today_str = now.strftime("%Y-%m-%d")

            for slot in SCHEDULE_SLOTS:
                slot_key = f"{today_str}_{slot['hour']}_{slot['minute']}"

                # Eğer o vaktin saati geldiyse ve bugün bu slot henüz atılmadıysa
                # (1 dakikalık dar aralık yerine o saat içinde kaçırılmadan tetikleme kalkanı)
                is_slot_time = (now.hour == slot["hour"] and now.minute >= slot["minute"]) or (now.hour > slot["hour"])
                
                # Ancak bir sonraki slotun vaktine geçildiyse eski slotu tetikleme
                # (Örn: Gece yarısı açılınca öğlen 13:00'ü gece 01:00'de tetiklemesin)
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
