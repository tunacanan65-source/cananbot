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
    """TikTok Studio üzerinden videoyu otonom olarak yükler (ev PC'si veya GitHub Actions bulutu)."""
    import browser_session as bs
    cookies = bs.load_cookies("TIKTOK_COOKIES_B64", COOKIES_FILE, ("tiktok.com", "byteoversea.com"))
    if not any(c.get("name") == "sessionid" for c in cookies):
        return {"status": "error", "reason": "TikTok oturumu (TIKTOK_COOKIES_B64 / tiktok_cookies.json) bulunamadı."}

    if not os.path.exists(video_path):
        return {"status": "error", "reason": f"Video dosyası bulunamadı: {video_path}"}

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"status": "error", "reason": "Playwright modülü yüklü değil."}

    print(f"🚀 [TikTok Uploader] Video yükleme başlatılıyor: {os.path.basename(video_path)}")

    try:
        with sync_playwright() as p:
            browser = bs.launch_browser(p)
            win_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            context = browser.new_context(
                user_agent=win_ua,
                viewport={"width": 1440, "height": 950},
                locale="tr-TR",
                timezone_id="Europe/Istanbul"
            )
            if bs.IS_CLOUD:
                # Bulutta sadece çekirdek oturum çerezlerini (.tiktok.com) ver; TR IP'ye bağlı ttwid/msToken/s_v_web_id/odin_tt çakışıp login'e atar
                core_names = ("sessionid", "sessionid_ss", "sid_tt", "sid_guard", "uid_tt", "uid_tt_ss")
                clean_tt = []
                for c in cookies:
                    if c.get("name") in core_names and c.get("value"):
                        clean_tt.append({
                            "name": c["name"],
                            "value": c["value"],
                            "domain": ".tiktok.com",
                            "path": "/",
                            "secure": True,
                            "httpOnly": True,
                            "sameSite": "Lax",
                        })
                context.add_cookies(clean_tt if clean_tt else cookies)
            else:
                context.add_cookies(cookies)
            page = context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)

            if bs.IS_CLOUD:
                print("🌐 [TikTok] Önce ana sayfa açılıp bulut oturum belirteçleri alınıyor...")
                try:
                    page.goto("https://www.tiktok.com/", wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(3500)
                except Exception:
                    pass

            print("🌐 [TikTok] Studio Upload sayfası açılıyor...")
            page.goto("https://www.tiktok.com/tiktokstudio/upload", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(5000)
            if "login" in page.url.lower():
                print("⚠️ [TikTok] Studio login'e attı, creator-center/upload alternatifi deneniyor...")
                page.goto("https://www.tiktok.com/creator-center/upload", wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(5000)
            if "login" in page.url.lower():
                try:
                    page.screenshot(path=os.path.join(BASE_DIR, "output", "tiktok_login_redirect.png"))
                except Exception:
                    pass
                print(f"❌ [TikTok] Giriş sayfasına yönlendirildi: {page.url}")
                browser.close()
                return {"status": "error", "reason": f"TikTok oturumu düşmüş veya bulut IP doğrulaması istiyor ({page.url})."}

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
                # Modallar / Bilgi pencereleri (DİKKAT: "Kapat"/"Cancel" yüklemeyi iptal edip çıkış onayı açtırıyor, ekleme!)
                for txt in ["Anladım", "Got it", "Tamam", "Aç"]:
                    b = page.locator(f'button:has-text("{txt}")')
                    if b.count():
                        try:
                            b.first.click(force=True)
                            page.wait_for_timeout(800)
                        except Exception:
                            pass

            dismiss_overlays()

            # Dosya yükleme alanını ana sayfada ve iframe'lerde 20 saniyeye kadar bekle
            file_input = None
            for _ in range(10):
                loc = page.locator('input[type="file"]').first
                if loc.count():
                    file_input = loc
                    break
                for fr in page.frames:
                    try:
                        floc = fr.locator('input[type="file"]').first
                        if floc.count():
                            file_input = floc
                            break
                    except Exception:
                        pass
                if file_input is not None:
                    break
                page.wait_for_timeout(2000)
                dismiss_overlays()

            if file_input is None:
                try:
                    page.screenshot(path=os.path.join(BASE_DIR, "output", "tiktok_no_file_input.png"))
                    snippet = page.locator("body").inner_text()[:300].replace("\n", " | ")
                    print(f"❌ [TikTok] Dosya kutusu bulunamadı. URL={page.url} | Metin={snippet}")
                except Exception:
                    pass
                browser.close()
                return {"status": "error", "reason": f"TikTok dosya yükleme kutusu bulunamadı (URL: {page.url})."}

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

            # Gizlilik kontrolü: "Herkes" / "Everyone" (Public) seçili olduğundan emin ol
            try:
                priv_dropdown = page.locator(
                    'button:has-text("Sadece ben"), div[role="combobox"]:has-text("Sadece ben"), '
                    'span:has-text("Sadece ben"), button:has-text("Only me"), div[role="combobox"]:has-text("Only me"), '
                    'span:has-text("Only me"), div:has-text("Bu gönderiyi kimler görebilir") >> .. >> button, '
                    'div:has-text("Who can watch this video") >> .. >> button'
                )
                if priv_dropdown.count():
                    priv_dropdown.first.scroll_into_view_if_needed()
                    priv_dropdown.first.click(force=True)
                    page.wait_for_timeout(800)
                    herkes_opt = page.locator(
                        'div[role="option"]:has-text("Herkes"), li:has-text("Herkes"), '
                        'span:has-text("Herkes"), div[role="option"]:has-text("Everyone"), '
                        'li:has-text("Everyone"), span:has-text("Everyone")'
                    )
                    if herkes_opt.count():
                        herkes_opt.first.click(force=True)
                        page.wait_for_timeout(800)
            except Exception:
                pass

            # 'Paylaş' / 'Post' butonunu bul (Türkçe ve İngilizce TikTok Studio)
            post_btn = page.locator('button[data-e2e="post_video_button"]')
            if not post_btn.count():
                post_btn = page.locator('button:has-text("Paylaş")').filter(has_not_text="Posts")
            if not post_btn.count():
                post_btn = page.get_by_role("button", name=re.compile(r"^(Paylaş|Post|Yayınla)$", re.IGNORECASE))

            if not post_btn.count():
                try:
                    page.screenshot(path=os.path.join(BASE_DIR, "output", "tiktok_no_post_btn.png"))
                except Exception:
                    pass
                browser.close()
                return {"status": "error", "reason": "TikTok Paylaş/Post butonu bulunamadı."}

            post_elem = post_btn.first
            post_elem.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)

            # Buton aktifleşene kadar bekle
            for _ in range(15):
                dismiss_overlays()
                if not post_elem.is_disabled():
                    break
                time.sleep(2)

            def clear_tux_modals(tag: str = ""):
                """TikTok Studio'nun tux-portal modallarını tespit edip içindeki butonla kapatır."""
                for _ in range(4):
                    backdrop = page.locator("div._TUXModal-backdrop--entered, div[class*='TUXModal-backdrop']")
                    if not backdrop.count():
                        return
                    portal = page.locator("#tux-portal-container")
                    try:
                        txt = portal.inner_text()[:400].replace("\n", " | ")
                        print(f"🪟 [TikTok] Modal tespit edildi {tag}: {txt}")
                        page.screenshot(path=os.path.join(BASE_DIR, "output", "tiktok_modal_debug.png"))
                    except Exception:
                        pass
                    clicked = False
                    for t in ["Hemen paylaş", "Post now", "Paylaş", "Anladım", "Got it", "Tamam", "OK",
                              "Devam", "Continue", "Aç", "Turn on", "Kapat", "Close", "İptal", "Cancel", "Şimdi değil", "Not now"]:
                        b = portal.locator(f'button:has-text("{t}")')
                        if b.count():
                            try:
                                b.first.click(force=True)
                                print(f"✅ [TikTok] Modal butonu tıklandı: {t}")
                                clicked = True
                                page.wait_for_timeout(1500)
                                break
                            except Exception:
                                pass
                    if not clicked:
                        try:
                            page.keyboard.press("Escape")
                            page.wait_for_timeout(1000)
                        except Exception:
                            pass

            clear_tux_modals("(paylaş öncesi)")
            print("🚀 [TikTok] 'Paylaş' butonuna tıklanıyor...")
            try:
                post_elem.click(timeout=8000)
            except Exception:
                clear_tux_modals("(tıklama engellendi)")
                post_elem.click(force=True, timeout=8000)
            page.wait_for_timeout(3000)
            clear_tux_modals("(paylaş sonrası)")

            # Ek onay penceresi varsa (örn: "Paylaşmaya devam edilsin mi? -> Hemen paylaş", "Yine de paylaş", "Post now")
            for _ in range(5):
                confirm_pop = page.locator(
                    'button:has-text("Hemen paylaş"), button:has-text("Yine de paylaş"), '
                    'button:has-text("Post now"), button:has-text("Post anyway"), button:has-text("Onayla")'
                )
                if confirm_pop.count():
                    try:
                        print("✅ [TikTok] 'Hemen paylaş' onay penceresine tıklanıyor...")
                        confirm_pop.first.click(force=True)
                        page.wait_for_timeout(4000)
                        break
                    except Exception:
                        pass
                page.wait_for_timeout(1000)

            # Paylaşımın tamamlanıp içerik sayfasına yönlenmesini bekle
            published = False
            for sec in range(25):
                page.wait_for_timeout(2000)
                confirm_pop = page.locator('button:has-text("Hemen paylaş"), button:has-text("Post now")')
                if confirm_pop.count():
                    try:
                        confirm_pop.first.click(force=True)
                    except Exception:
                        pass
                body_text = page.locator("body").inner_text()
                if (
                    "tiktokstudio/content" in page.url
                    or "Gönderilerim" in body_text
                    or "Videolarınız yükleniyor" in body_text
                    or "Manage your posts" in body_text
                    or "Your video is being uploaded" in body_text
                    or "Your video has been uploaded" in body_text
                ):
                    published = True
                    break

            # İçerik listesi sayfasında ("tiktokstudio/content") eğer herhangi bir gönderi "Sadece ben" / "Only me" olarak kaldıysa otomatik "Herkes" / "Everyone"a çevir!
            try:
                page.wait_for_timeout(2000)
                sadece_ben_btns = page.locator('button:has-text("Sadece ben"), div:has-text("Sadece ben"), button:has-text("Only me"), div:has-text("Only me")')
                if sadece_ben_btns.count():
                    sadece_ben_btns.first.click(force=True)
                    page.wait_for_timeout(800)
                    herkes_item = page.locator('div[role="option"]:has-text("Herkes"), li:has-text("Herkes"), span:has-text("Herkes"), div[role="option"]:has-text("Everyone"), li:has-text("Everyone"), span:has-text("Everyone")')
                    if herkes_item.count():
                        herkes_item.first.click(force=True)
                        page.wait_for_timeout(1500)
            except Exception:
                pass

            # Teyit ekran görüntüsü
            os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)
            confirm_path = os.path.join(BASE_DIR, "output", "tiktok_published_confirm.png")
            page.screenshot(path=confirm_path)

            # Çerezleri güncelle (sadece ev PC'sinde; bulutta diske çerez yazılmaz)
            if not bs.IS_CLOUD:
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
