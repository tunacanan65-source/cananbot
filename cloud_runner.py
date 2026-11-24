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
    tt = tiktok_pending_reel_id()
    tw = canan_twitter_sync.get_due_slots()
    print(f"🔎 TikTok bekleyen Reels: {tt or 'yok'}")
    print(f"🔎 Twitter vakti gelen slotlar: {[s['id'] for s in tw] or 'yok'}")
    write_output("due", "true" if (tt or tw) else "false")
    return 0


def do_run() -> int:
    failures = 0

    # 1) TikTok (yurt dışı IP engeline takılırsa Twitter'ı ve iş akışını kırmızıya düşürmesin)
    pending = tiktok_pending_reel_id()
    if pending:
        print(f"🎵 [Bulut] TikTok'a yüklenecek Reels: {pending}")
        try:
            canan_tiktok_sync.sync_once(seed_existing=False)
            if pending not in canan_tiktok_sync.load_synced_ids():
                print("⚠️ [Bulut] TikTok yurt dışı IP nedeniyle atlandı (PC açılınca otomatik yüklenir).")
        except Exception as te:
            print(f"⚠️ [Bulut] TikTok uyarısı: {te}")
    else:
        print("🎵 [Bulut] TikTok için yeni Reels yok.")

    # 2) Twitter / X (her çalışmada en fazla 1 gönderi — peş peşe spam olmasın, saatlerinde tek tek atsın)
    res = canan_twitter_sync.check_and_run_due_slots(max_posts=1)
    print(f"🐦 [Bulut] Twitter sonucu: {res}")
    failures += res.get("failed", 0)

    return 1 if failures else 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(do_check())
    sys.exit(do_run())
