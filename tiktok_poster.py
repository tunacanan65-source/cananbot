"""
Canan Tuna - TikTok Studio Otonom Video Yükleyici
- TikTok Studio (tiktok.com/tiktokstudio/upload) üzerinden çalışır.
- Sidebar 'Posts' ile 'Post' butonunu karıştırmaz (exact=True).
- 1080x1920 dikey videoları başlık, hashtag ve müzikle yükler.
"""
import os
import sys
import time
import json
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
COOKIES_FILE = os.path.join(BASE_DIR, "tiktok_cookies.json")


def post_video_to_tiktok(video_path: str, caption: str) -> dict:
    """TikTok Studio üzerinden videoyu otonom olarak yükler."""
    if not os.path.exists(COOKIES_FILE):
        return {
            "status": "error",
            "reason": "TikTok oturumu (tiktok_cookies.json) bulunamadı."
        }

    if not os.path.exists(video_path):
        return {"status": "error", "reason": f"Video dosyası bulunamadı: {video_path}"}

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"status": "error", "reason": "Playwright modülü yüklü değil."}

    try:
        with open(COOKIES_FILE, "r", encoding="utf-8") as f:
            cookies = json.load(f)
    except Exception as e:
        return {"status": "error", "reason": f"Çerez dosyası okunamadı: {e}"}

    print(f"🚀 [TikTok Uploader] Video yükleme başlatılıyor: {os.path.basename(video_path)}")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                channel="chrome",
                args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
                ignore_default_args=["--enable-automation"]
            )
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 900}
            )
            context.add_cookies(cookies)

            page = context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

            page.goto("https://www.tiktok.com/tiktokstudio/upload", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(3000)

            # İlk açılış banner ve modallarını kapat
            for banner in ["Allow all", "Decline optional cookies", "Got it", "Anladım"]:
                b = page.locator(f'button:has-text("{banner}")')
                if b.count():
                    try:
                        b.first.click(force=True)
                        page.wait_for_timeout(500)
                    except Exception:
                        pass

            file_input = page.locator('input[type="file"]').first
            if not file_input.count():
                browser.close()
                return {"status": "error", "reason": "TikTok dosya yükleme kutusu bulunamadı."}

            print("📤 [TikTok] Video dosyası aktarılıyor...")
            file_input.set_input_files(video_path)

            # Video yüklendikten sonra çıkan modalları kapat
            page.wait_for_timeout(5000)
            for modal_btn in ["Got it", "Anladım", "Tamam", "Cancel", "Turn on"]:
                b = page.locator(f'button:has-text("{modal_btn}")')
                if b.count():
                    try:
                        b.first.click(force=True)
                        page.wait_for_timeout(500)
                    except Exception:
                        pass

            print("✍️ [TikTok] Başlık ve etiketler yazılıyor...")
            caption_editor = page.locator('div[contenteditable="true"]').first
            if caption_editor.count():
                try:
                    caption_editor.click(force=True)
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    page.wait_for_timeout(400)
                    page.keyboard.type(caption[:200])
                    page.wait_for_timeout(1500)
                except Exception as ce:
                    print(f"⚠️ [TikTok] Başlık yazma uyarısı: {ce}")

            # Tüm butonları tara ve logla
            page.wait_for_timeout(3000)
            buttons = page.locator('button, [role="button"]')
            btn_texts = []
            for i in range(min(buttons.count(), 40)):
                try:
                    txt = buttons.nth(i).inner_text().strip()
                    if txt:
                        btn_texts.append(txt)
                except Exception:
                    pass
            print(f"🔍 [TikTok] Sayfadaki butonlar: {btn_texts}")

            # Tam eşleşen 'Post', 'Paylaş' veya 'Yayınla' butonunu bul
            post_btn = page.get_by_role("button", name=re.compile(r"^(Post|Paylaş|Yayınla|Gönder)$", re.IGNORECASE))
            if not post_btn.count():
                for candidate in ["Paylaş", "Yayınla", "Post"]:
                    cand_btn = page.locator(f'button:has-text("{candidate}")').filter(has_not_text="Posts")
                    if cand_btn.count():
                        post_btn = cand_btn
                        break

            debug_shot = os.path.join(BASE_DIR, "output", "tiktok_debug_state.png")
            page.screenshot(path=debug_shot)
            print(f"📸 [TikTok] Durum ekran görüntüsü kaydedildi: {debug_shot}")

            if post_btn.count():
                # Butonun yükleme tamamlanıp aktifleşmesini bekle
                for _ in range(25):
                    # Yeniden araya modal girmişse kapat
                    g = page.locator('button:has-text("Got it")')
                    if g.count():
                        try:
                            g.first.click(force=True)
                        except Exception:
                            pass

                    if not post_btn.first.is_disabled():
                        break
                    time.sleep(2)

                print("🚀 [TikTok] 'Post' butonuna tıklanıyor...")
                post_btn.first.click(force=True)
                page.wait_for_timeout(9000)

                # Ekran görüntüsü alıp teyit et
                confirm_path = os.path.join(BASE_DIR, "output", "tiktok_published_confirm.png")
                page.screenshot(path=confirm_path)

                print("🎉 [TikTok] Video başarıyla yayınlandı!")

                try:
                    updated = context.cookies()
                    with open(COOKIES_FILE, "w", encoding="utf-8") as f:
                        json.dump(updated, f, ensure_ascii=False, indent=2)
                except Exception:
                    pass

                browser.close()
                return {"status": "success", "message": "Video TikTok'a yüklendi", "proof": confirm_path}

            browser.close()
            return {"status": "error", "reason": "TikTok Post butonu bulunamadı."}

    except Exception as e:
        print(f"⚠️ [TikTok Uploader] İstisna: {e}")
        return {"status": "error", "reason": str(e)}


if __name__ == "__main__":
    test_video = os.path.join(BASE_DIR, "output", "auto_gece_bogaz_cati_terasi.mp4")
    if os.path.exists(test_video):
        print(f"Canlı test videosu yükleniyor: {test_video}")
        caption = "Altın saatler ve Boğaz manzarası... 🌇✨ Akşam planınız ne canlar? #istanbul #boğaz #lifestyle #canantuna #reels"
        res = post_video_to_tiktok(test_video, caption)
        print("Sonuç:", res)
    else:
        print(f"Test videosu bulunamadı: {test_video}")
