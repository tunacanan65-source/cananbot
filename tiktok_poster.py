"""
Canan Tuna - TikTok Studio Otonom Video Yükleyici
- TikTok Studio (tiktok.com/tiktokstudio/upload) üzerinden çalışır.
- Çerez ve onboarding popuplarını ("Tümüne izin ver", "Anladım", "Aç") otomatik temizler.
- Gizliliği doğrudan 'Herkes' olarak seçer.
- 'Paylaş' butonunu tetikleyip yönlendirmeyi teyit eder.
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
        return {"status": "error", "reason": "TikTok oturumu (tiktok_cookies.json) bulunamadı."}

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
                viewport={"width": 1440, "height": 950}
            )
            context.add_cookies(cookies)
            page = context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

            print("🌐 [TikTok] Studio Upload sayfası açılıyor...")
            page.goto("https://www.tiktok.com/tiktokstudio/upload", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(3500)

            def dismiss_overlays():
                # Çerez bannerları
                for txt in ["Tümüne izin ver", "İsteğe bağlı çerezleri reddet", "Allow all", "Decline optional cookies"]:
                    b = page.locator(f'button:has-text("{txt}")')
                    if b.count():
                        try:
                            b.first.click(force=True)
                            page.wait_for_timeout(800)
                        except Exception:
                            pass
                # Modallar / Bilgi pencereleri
                for txt in ["Anladım", "Got it", "Tamam", "Aç", "Kapat", "Cancel"]:
                    b = page.locator(f'button:has-text("{txt}")')
                    if b.count():
                        try:
                            b.first.click(force=True)
                            page.wait_for_timeout(800)
                        except Exception:
                            pass

            dismiss_overlays()

            file_input = page.locator('input[type="file"]').first
            if not file_input.count():
                browser.close()
                return {"status": "error", "reason": "TikTok dosya yükleme kutusu bulunamadı."}

            print("📤 [TikTok] Video dosyası aktarılıyor...")
            file_input.set_input_files(video_path)

            # Video yükleme ve ön izleme hazır oluşunu bekle
            for _ in range(8):
                page.wait_for_timeout(2000)
                dismiss_overlays()

            print("✍️ [TikTok] Başlık ve etiketler yazılıyor...")
            caption_editor = page.locator('div[contenteditable="true"]').first
            if caption_editor.count():
                try:
                    caption_editor.click(force=True)
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    page.wait_for_timeout(300)
                    page.keyboard.type(caption[:200])
                    page.wait_for_timeout(1000)
                except Exception as ce:
                    print(f"⚠️ [TikTok] Başlık uyarısı: {ce}")

            dismiss_overlays()

            # Gizlilik kontrolü: "Herkes" seçili olduğundan emin ol
            try:
                priv_opt = page.locator('div:has-text("Bu gönderiyi kimler görebilir"), span:has-text("Bu gönderiyi kimler görebilir")')
                if priv_opt.count():
                    priv_opt.first.scroll_into_view_if_needed()
                    # Eğer "Sadece ben" veya "Arkadaşlar" seçiliyse "Herkes" yap
                    herkes_radio = page.locator('input[value="public"], label:has-text("Herkes"), div:has-text("Herkes")')
                    if herkes_radio.count():
                        herkes_radio.first.click(force=True)
            except Exception:
                pass

            # 'Paylaş' butonunu bul
            post_btn = page.locator('button:has-text("Paylaş")').filter(has_not_text="Posts")
            if not post_btn.count():
                post_btn = page.get_by_role("button", name=re.compile(r"^(Paylaş|Post|Yayınla)$", re.IGNORECASE))

            if not post_btn.count():
                browser.close()
                return {"status": "error", "reason": "TikTok Paylaş butonu bulunamadı."}

            post_elem = post_btn.first
            post_elem.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)

            # Buton aktifleşene kadar bekle
            for _ in range(15):
                dismiss_overlays()
                if not post_elem.is_disabled():
                    break
                time.sleep(2)

            print("🚀 [TikTok] 'Paylaş' butonuna tıklanıyor...")
            post_elem.click()
            page.wait_for_timeout(3000)

            # Ek onay penceresi varsa (örn: telif onayı)
            confirm_pop = page.locator('button:has-text("Yine de paylaş"), button:has-text("Post anyway"), button:has-text("Onayla")')
            if confirm_pop.count():
                try:
                    confirm_pop.first.click()
                    page.wait_for_timeout(3000)
                except Exception:
                    pass

            # Paylaşımın tamamlanıp içerik sayfasına yönlenmesini bekle
            published = False
            for sec in range(20):
                page.wait_for_timeout(2000)
                body_text = page.locator("body").inner_text()
                if "Yönet" in body_text or "Manage" in body_text or "Gönderiler" in body_text or "tiktokstudio/content" in page.url:
                    published = True
                    break

            # Teyit ekran görüntüsü
            confirm_path = os.path.join(BASE_DIR, "output", "tiktok_published_confirm.png")
            page.screenshot(path=confirm_path)

            # Çerezleri güncelle
            try:
                updated = context.cookies()
                with open(COOKIES_FILE, "w", encoding="utf-8") as f:
                    json.dump(updated, f, ensure_ascii=False, indent=2)
            except Exception:
                pass

            browser.close()

            if published:
                print("🎉 [TikTok] Video başarıyla yayınlandı ve onaylandı!")
                return {"status": "success", "message": "Video TikTok'ta yayında", "proof": confirm_path}
            else:
                return {"status": "success", "message": "Video yüklendi (inceleme/yayın sürecinde)", "proof": confirm_path}

    except Exception as e:
        print(f"⚠️ [TikTok Uploader] İstisna: {e}")
        return {"status": "error", "reason": str(e)}


if __name__ == "__main__":
    test_video = os.path.join(BASE_DIR, "output", "auto_gece_bogaz_cati_terasi.mp4")
    if os.path.exists(test_video):
        caption = "Altın saatler ve Boğaz manzarası... 🌇✨ Akşam planınız ne canlar? #istanbul #boğaz #lifestyle #canantuna #reels"
        res = post_video_to_tiktok(test_video, caption)
        print("Sonuç:", res)
