"""
Canan Tuna - Twitter (X) (@canantunau) 7/24 Günlük 6 Gönderi (3 Reels + 3 Fotoğraf) Otonom Motoru
- Her gün 3 adet 4-karelik 16sn Full HD Reels videosu + 3 adet Tekli Yüksek Çözünürlüklü Görsel paylaşır:
  1) 10:30 -> 1. Görsel (Sabah Fotoğrafı)
  2) 12:30 -> 1. Reels Videosu (Öğlen 4 Karelik Video)
  3) 15:00 -> 2. Reels Videosu (İkindi 4 Karelik Video)
  4) 17:00 -> 2. Görsel (Akşamüstü Kombin Fotoğrafı)
  5) 21:00 -> 3. Reels Videosu (Prime-Time Akşam 4 Karelik Video)
  6) 23:00 -> 3. Görsel (Gece / Yatak Odası Fotoğrafı)
- 30 günlük sıfır-tekrar karantina kalkanına ve yeni üretilen 176 görsel önceliğine %100 uyar.
- Bilgisayar kapalıyken kaçan bir slot varsa, açıldığı anda eksik slotu otomatik tamamlar.
"""
import os
import sys
import time
import json
from datetime import datetime
# Ağır modüller (canan_autopilot, create_canan_reel, twitter_poster) sadece paylaşım anında yüklenir;
# böylece buluttaki hızlı "paylaşım vakti geldi mi?" kontrolü saniyeler sürer.

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
STATE_FILE = os.path.join(BASE_DIR, "twitter_daily_state.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

TWITTER_DAILY_SLOTS = [
    {"id": "tw_photo_1_morning",   "hour": 10, "minute": 30, "type": "photo", "label": "1. Görsel (Sabah Fotoğrafı)"},
    {"id": "tw_reels_1_noon",      "hour": 12, "minute": 30, "type": "video", "label": "1. Reels Videosu (Öğlen 4 Kare)"},
    {"id": "tw_reels_2_afternoon", "hour": 15, "minute": 0,  "type": "video", "label": "2. Reels Videosu (İkindi 4 Kare)"},
    {"id": "tw_photo_2_evening",   "hour": 17, "minute": 0,  "type": "photo", "label": "2. Görsel (Akşamüstü Kombin Fotoğrafı)"},
    {"id": "tw_reels_3_primetime", "hour": 21, "minute": 0,  "type": "video", "label": "3. Reels Videosu (Akşam 4 Kare)"},
    {"id": "tw_photo_3_night",     "hour": 23, "minute": 0,  "type": "photo", "label": "3. Görsel (Gece / Yatak Odası Fotoğrafı)"},
]


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"posted_slots": {}, "used_images": []}
    return {"posted_slots": {}, "used_images": []}


def save_state(state: dict):
    state["used_images"] = state.get("used_images", [])[-180:]
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def post_single_twitter_item(media_type: str = "photo") -> bool:
    """Yeni nesil görsel havuzundan sıfır tekrarla 1 Reels videosu veya 1 Fotoğraf üretip @canantunau'ya atar."""
    import canan_autopilot
    import create_canan_reel
    import twitter_poster
    state = load_state()
    tw_used = set(state.get("used_images", []))

    scenario = canan_autopilot.pick_next_scenario(force_type=media_type, meta_safe_only=False)
    if not scenario:
        print("⚠️ [Twitter Autopilot] Senaryo bulunamadı.")
        return False

    chosen_img = scenario.get("image_path")
    if not chosen_img or not os.path.exists(chosen_img):
        return False

    # Eğer bu görsel Twitter'da son zamanlarda kullanıldıysa yeni nesil havuzdan taze bir görsel seç
    images_dir = os.path.join(BASE_DIR, "assets", "images")
    if os.path.basename(chosen_img) in tw_used and os.path.exists(images_dir):
        all_new = sorted([
            os.path.join(images_dir, f)
            for f in os.listdir(images_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
            and create_canan_reel.is_new_generation_image(f)
            and f not in tw_used
        ])
        if all_new:
            chosen_img = all_new[0]

    caption = f"{scenario.get('caption', '')}\n\n{scenario.get('tags', '')}".strip()

    if media_type == "video":
        out_mp4 = os.path.join(OUTPUT_DIR, f"tw_reel_{int(time.time())}.mp4")
        quarantined = (scenario.get("_quarantined_files") or set()) | tw_used
        companions = create_canan_reel.pick_companion_images(
            chosen_img,
            count=3,
            extra_candidates=scenario.get("companions"),
            exclude_filenames=quarantined
        )
        create_canan_reel.create_reels_video(
            chosen_img,
            output_mp4=out_mp4,
            companion_images=companions,
            hook_text=scenario.get("hook"),
            custom_scene_hooks=scenario.get("scene_hooks"),
            exclude_filenames=quarantined
        )
        res = twitter_poster.post_media_to_twitter(out_mp4, caption)
        if res.get("status") == "success":
            used_list = state.get("used_images", [])
            used_list.append(os.path.basename(chosen_img))
            for c in companions:
                used_list.append(os.path.basename(c))
            state["used_images"] = used_list
            save_state(state)
            return True
        return False
    else:
        res = twitter_poster.post_media_to_twitter(chosen_img, caption)
        if res.get("status") == "success":
            used_list = state.get("used_images", [])
            used_list.append(os.path.basename(chosen_img))
            state["used_images"] = used_list
            save_state(state)
            return True
        return False


def get_due_slots() -> list:
    """Saati gelmiş (veya kaçmış) ama bugün henüz paylaşılmamış slotları döner."""
    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    now_mins = now.hour * 60 + now.minute
    today_done = load_state().get("posted_slots", {}).get(today_str, [])
    return [s for s in TWITTER_DAILY_SLOTS
            if s["id"] not in today_done and now_mins >= s["hour"] * 60 + s["minute"]]


def check_and_run_due_slots(max_posts: int = 1, gap_seconds: int = 150) -> dict:
    """Saati gelmiş slotları sırayla (en fazla max_posts adet) paylaşır. Sonuç: {'posted': n, 'failed': n}"""
    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    result = {"posted": 0, "failed": 0}

    for slot in get_due_slots()[:max_posts]:
        slot_id = slot["id"]
        if result["posted"] or result["failed"]:
            time.sleep(gap_seconds)
        print(f"🚀 [Twitter 6/Gün Zamanlayıcı] {slot['label']} paylaşılıyor...")
        ok = post_single_twitter_item(media_type=slot["type"])
        if ok:
            # post_single_twitter_item kullanılan görselleri kaydetti; ezmemek için state'i yeniden oku
            state = load_state()
            posted_slots = state.get("posted_slots", {})
            today_done = posted_slots.get(today_str, [])
            today_done.append(slot_id)
            posted_slots[today_str] = today_done
            for old_k in sorted(posted_slots.keys())[:-14]:
                posted_slots.pop(old_k, None)
            state["posted_slots"] = posted_slots
            save_state(state)
            result["posted"] += 1
            print(f"✅ [Twitter] {slot['label']} tamamlandı! (Bugün: {len(today_done)}/6)")
        else:
            result["failed"] += 1
            print(f"❌ [Twitter] {slot['label']} paylaşılamadı.")
            break
    return result


if __name__ == "__main__":
    if "--first-test" in sys.argv:
        print("🔥 [Twitter İlk Canlı Test] 1 Fotoğraf + 1 Reels Videosu @canantunau hesabına gönderiliyor...")
        post_single_twitter_item("photo")
        time.sleep(5)
        post_single_twitter_item("video")
    else:
        check_and_run_due_slots()
