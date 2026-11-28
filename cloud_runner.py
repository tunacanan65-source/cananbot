"""
Canan Tuna - GitHub Actions Bulut Çalıştırıcısı (PC kapalıyken Twitter/X + TikTok)

Kullanım:
  python cloud_runner.py --check   -> Paylaşım vakti gelmiş bir iş var mı? (GITHUB_OUTPUT'a due=true/false yazar)
  python cloud_runner.py --run     -> Vakti gelen TikTok ve Twitter paylaşımlarını yapar

Kurallar:
- TikTok: Render'ın Instagram'a attığı en yeni Reels henüz TikTok'a gitmediyse indirip yükler.
- Twitter: Günde 6 slot (3 Reels + 3 Görsel). Bir çalıştırmada en fazla 2 slot (aralarında 2,5 dk) atılır.
- Bir paylaşım başarısız olursa çıkış kodu 1 olur; GitHub sana e-posta ile haber verir.
"""
import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import canan_tiktok_sync
import canan_twitter_sync


def tiktok_pending_reel_id():
    reels = canan_tiktok_sync.get_latest_instagram_reels(limit=5)
    if not reels:
        return None
    newest = reels[0]["id"]
    return None if newest in canan_tiktok_sync.load_synced_ids() else newest


def write_output(key: str, val: str):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"{key}={val}\n")


def do_check() -> int:
    # TikTok artık sadece Ev PC'sinden (Türk Ev IP'si) yüklenir; bulutta yalnızca Twitter/X çalışır.
    tw = canan_twitter_sync.get_due_slots()
    print(f"🔎 [Bulut] Twitter vakti gelen slotlar: {[s['id'] for s in tw] or 'yok'}")
    write_output("due", "true" if tw else "false")
    return 0


def do_run() -> int:
    failures = 0

    # TikTok bulut (ABD veri merkezi IP) kısıtlaması nedeniyle devre dışı; sadece Ev PC'sinden yüklenir.
    print("ℹ️ [Bulut] TikTok yüklemesi Ev PC'sine (Türk IP) devredildi, bulutta atlanıyor.")

    # Twitter / X (her çalışmada en fazla 1 gönderi — peş peşe spam olmasın, saatlerinde tek tek atsın)
    res = canan_twitter_sync.check_and_run_due_slots(max_posts=1)
    print(f"🐦 [Bulut] Twitter sonucu: {res}")
    failures += res.get("failed", 0)

    return 1 if failures else 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(do_check())
    sys.exit(do_run())
