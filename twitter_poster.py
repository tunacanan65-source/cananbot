"""
Canan Tuna - Twitter (X) (@canantunau) Otonom Video (Reels) ve Görsel (Fotoğraf) Yükleyici
- Doğrudan gerçek Chrome profili (twitter_chrome_profile) veya twitter_cookies.json üzerinden çalışır.
- Hem MP4 Reels videolarını hem de JPG/PNG tekli fotoğrafları yüksek kalitede X'e yükler.
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
COOKIES_FILE = os.path.join(BASE_DIR, "twitter_cookies.json")
PROFILE_DIR = os.path.join(BASE_DIR, "twitter_chrome_profile")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def format_twitter_caption(raw_caption: str) -> str:
    """Twitter/X 280 karakter sınırına uygun, çekici ve etkileşimli metin hazırlar."""
    if not raw_caption:
        return "Yeni kombinimle 10 üzerinden kaç puan veriyorsunuz? Yoruma yazın 💕✨ #canantuna #kombin #istanbul"

    lines = [ln.strip() for ln in raw_caption.strip().splitlines() if ln.strip()]
    first_line = lines[0] if lines else ""
    clean_text = re.sub(r"#\S+", "", first_line).strip()
    if len(clean_text) > 205:
        clean_text = clean_text[:202].rstrip() + "..."
    tweet_text = f"{clean_text}\n\n#canantuna #kombin #keşfet"
    return tweet_text[:275]


def post_media_to_twitter(media_path: str, caption: str) -> dict:
    """Twitter (X) üzerinden fotoğraf veya Reels videosunu otonom olarak paylaşır."""
    import browser_session as bs
    x_cookies = bs.load_cookies("TWITTER_COOKIES_B64", COOKIES_FILE, ("x.com", "twitter.com"))
    use_profile = (not bs.IS_CLOUD) and os.path.exists(PROFILE_DIR)
    if not use_profile and not any(c.get("name") == "auth_token" for c in x_cookies):
        return {"status": "error", "reason": "Twitter oturumu (profil / TWITTER_COOKIES_B64 / twitter_cookies.json) bulunamadı."}

    if not os.path.exists(media_path):
        return {"status": "error", "reason": f"Medya dosyası bulunamadı: {media_path}"}

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"status": "error", "reason": "Playwright modülü yüklü değil."}

    is_video = media_path.lower().endswith(".mp4")
    tweet_text = format_twitter_caption(caption)
    print(f"🐦 [Twitter Uploader] {'Reels Videosu' if is_video else 'Fotoğraf'} yükleniyor: {os.path.basename(media_path)}")

    try:
        with sync_playwright() as p:
            browser = None
            if use_profile:
                context = p.chromium.launch_persistent_context(
                    user_data_dir=PROFILE_DIR,
                    headless=True,
                    channel="chrome",
                    user_agent=bs.REAL_UA,
                    args=bs.LAUNCH_ARGS,
                    ignore_default_args=["--enable-automation"],
                    viewport={"width": 1366, "height": 900}
                )
            else:
                browser = bs.launch_browser(p)
                win_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
                context = browser.new_context(user_agent=win_ua, viewport={"width": 1366, "height": 900},
                                              locale="tr-TR", timezone_id="Europe/Istanbul")
                # Sadece temel X oturum çerezlerini (.x.com) temiz şekilde ekle (çakışan eski çerezler X'te login'e atar)
                auth_val = next((c["value"] for c in x_cookies if c.get("name") == "auth_token" and c.get("value")), "")
                ct0_val = next((c["value"] for c in x_cookies if c.get("name") == "ct0" and c.get("value")), "")
                clean_x = []
                if auth_val:
                    clean_x.append({"name": "auth_token", "value": auth_val, "domain": ".x.com", "path": "/", "secure": True, "httpOnly": True})
                if ct0_val:
                    clean_x.append({"name": "ct0", "value": ct0_val, "domain": ".x.com", "path": "/", "secure": True, "httpOnly": False})
                context.add_cookies(clean_x if clean_x else x_cookies)
            page = context.pages[0] if context.pages else context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

            print("🌐 [Twitter] X Paylaşım sayfası açılıyor...")
            page.goto("https://x.com/compose/post", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(4500)

            if "login" in page.url.lower():
                print(f"❌ [Twitter] Oturum açık değil (yönlendirilen adres: {page.url})")
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Twitter oturumu henüz açık değil."}

            def dismiss_x_overlays():
                """X'in çerez, bildirim, bilgi veya etiket öneri katmanlarını temizler (compose modalını kapatmadan)."""
                for txt in [
                    "Accept all cookies", "Tüm çerezleri kabul et", "Refuse non-essential cookies",
                    "Not now", "Şimdi değil", "Got it", "Anladım", "Tamam", "Skip for now"
                ]:
                    btn = page.locator(f'button:has-text("{txt}"), [role="button"]:has-text("{txt}")')
                    if btn.count():
                        try:
                            btn.first.click(force=True, timeout=2000)
                            page.wait_for_timeout(500)
                        except Exception:
                            pass
                # Etiket (#keşfet) öneri açılır listesi açıksa güvenli şekilde kapat
                try:
                    if page.locator('div[data-testid="typeaheadDropdown"]').count():
                        page.keyboard.press("Escape")
                        page.wait_for_timeout(400)
                except Exception:
                    pass

            # Varsa çerez / bildirim popuplarını kapat
            dismiss_x_overlays()

            # 1. Önce medya dosyasını yükle ve DOM'da eklendiğini doğrula (kanıtlanmış X compose/post akışı)
            file_input = page.locator('input[data-testid="fileInput"]').first
            if not file_input.count():
                file_input = page.locator('input[type="file"]').first
            if not file_input.count():
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Twitter dosya yükleme alanı (fileInput) bulunamadı."}

            print(f"📤 [Twitter] Medya dosyası aktarılıyor ({os.path.basename(media_path)})...")
            file_input.set_input_files(media_path)

            media_ready = False
            for sec in range(1, 50 if is_video else 25):
                page.wait_for_timeout(1000)
                has_img = page.locator('div[data-testid="attachments"] img').count() > 0
                has_remove = page.locator('button[aria-label="Remove media"], div[aria-label="Remove media"], button[data-testid="removeMedia"], button[aria-label="Medyayı kaldır"]').count() > 0
                has_video_preview = is_video and page.locator('div[data-testid="attachments"] video').count() > 0
                if (has_img or has_remove or has_video_preview) and (not is_video or sec >= 6):
                    media_ready = True
                    print(f"✅ [Twitter] Medya eklendi ve doğrulandı ({sec}. sn).")
                    page.wait_for_timeout(1000)
                    break

            if not media_ready:
                page.screenshot(path=os.path.join(OUTPUT_DIR, "twitter_media_fail.png"))
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Medya X'e yüklenemedi (attachments görünmedi)."}

            # 2. Tweet metnini doldur
            textbox = page.locator('div[role="textbox"][data-testid="tweetTextarea_0"]').first
            if not textbox.count():
                textbox = page.locator('div[role="textbox"], div[contenteditable="true"]').first
            if not textbox.count():
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Tweet metin kutusu bulunamadı."}

            print("✍️ [Twitter] Tweet metni yazılıyor...")
            textbox.click()
            page.wait_for_timeout(400)
            try:
                textbox.fill(tweet_text)
            except Exception:
                page.keyboard.insert_text(tweet_text)
            page.wait_for_timeout(1500)

            # 3. Gönder (Post) butonunu bul ve aktifleşmesini bekle
            post_btn = page.locator('button[data-testid="tweetButton"]').first
            if not post_btn.count():
                post_btn = page.locator('button[data-testid="tweetButtonInline"]').first
            if not post_btn.count():
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Twitter Gönderi butonu bulunamadı."}

            btn_ready = False
            for _ in range(25 if is_video else 12):
                aria_disabled = post_btn.get_attribute("aria-disabled")
                if aria_disabled != "true":
                    btn_ready = True
                    break
                page.wait_for_timeout(1000)

            if not btn_ready:
                page.screenshot(path=os.path.join(OUTPUT_DIR, "twitter_btn_disabled.png"))
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Twitter Gönderi butonu aktifleşmedi (aria-disabled=true)."}

            dismiss_x_overlays()

            print("🚀 [Twitter] 'Gönderi / Post' butonuna tıklanıyor...")
            clicked = False
            try:
                post_btn.click(timeout=6000)
                clicked = True
            except Exception as click_err:
                print(f"⚠️ [Twitter] Normal tıklama engellendi, katmanlar temizlenip alternatif yöntem deneniyor: {str(click_err)[:140]}")
                dismiss_x_overlays()
                try:
                    post_btn.click(force=True, timeout=6000)
                    clicked = True
                except Exception:
                    pass

            page.wait_for_timeout(3000)

            # Eğer compose penceresi hâlâ açıksa ve buton duruyorsa JS click + Ctrl+Enter ile gönder
            try:
                if "compose" in page.url.lower() and post_btn.count() and post_btn.is_visible():
                    dismiss_x_overlays()
                    try:
                        post_btn.evaluate("el => el.click()")
                        page.wait_for_timeout(2500)
                    except Exception:
                        pass
                if "compose" in page.url.lower() and post_btn.count() and post_btn.is_visible():
                    print("⌨️ [Twitter] Ctrl+Enter kısayolu ile gönderiliyor...")
                    textbox.focus()
                    page.keyboard.press("Control+Enter")
                    clicked = True
            except Exception:
                pass

            if not clicked:
                page.screenshot(path=os.path.join(OUTPUT_DIR, "twitter_click_fail.png"))
                context.close()
                if browser:
                    browser.close()
                return {"status": "error", "reason": "Twitter Gönderi butonuna tıklanamadı."}

            page.wait_for_timeout(6000)

            # Eğer gönderim sonrası bilgi popup'ı çıkarsa temizle
            dismiss_x_overlays()

            confirm_path = os.path.join(OUTPUT_DIR, "twitter_published_confirm.png")
            page.screenshot(path=confirm_path)

            # Gerçekten yayınlandı mı? Profil sayfasındaki ilk gönderilerde metnimiz var mı kontrol et
            published = False
            probe = re.sub(r"[^0-9A-Za-zÇĞİÖŞÜçğıöşü ]", "", tweet_text.split("\n")[0]).strip()[:22]
            for attempt in range(3 if probe else 0):
                try:
                    page.wait_for_timeout(4000 if attempt else 2000)
                    page.goto("https://x.com/canantunau", wait_until="domcontentloaded", timeout=30000)
                    page.wait_for_timeout(5000)
                    arts = page.locator('article[data-testid="tweet"]')
                    texts = " ".join(arts.nth(i).inner_text() for i in range(min(arts.count(), 3)))
                    texts_clean = re.sub(r"[^0-9A-Za-zÇĞİÖŞÜçğıöşü ]", "", texts)
                    if probe and probe in texts_clean:
                        published = True
                        break
                except Exception:
                    pass
            try:
                page.screenshot(path=os.path.join(OUTPUT_DIR, "twitter_profile_check.png"))
            except Exception:
                pass

            # Çerezleri kaydet/güncelle (sadece ev PC'sinde)
            if not bs.IS_CLOUD:
                try:
                    updated = context.cookies()
                    if any(c.get("name") == "auth_token" for c in updated):
                        with open(COOKIES_FILE, "w", encoding="utf-8") as f:
                            json.dump(updated, f, ensure_ascii=False, indent=2)
                except Exception:
                    pass

            context.close()
            if browser:
                browser.close()
            if not published and probe:
                # Gönder tuşuna basıldı; profil geç yüklenmiş olabilir. Mükerrer tweet riskine girmemek için tekrar denemiyoruz.
                print("⚠️ [Twitter] Gönder tuşuna basıldı ama gönderi profilde henüz görünmedi (doğrulanamadı).")
                return {"status": "success", "verified": False, "message": "Gönderildi, doğrulanamadı", "proof": confirm_path}
            print("🎉 [Twitter] Gönderi @canantunau profilinde doğrulandı!")
            return {"status": "success", "message": "Twitter'da yayında", "proof": confirm_path}

    except Exception as e:
        print(f"⚠️ [Twitter Uploader] İstisna: {e}")
        return {"status": "error", "reason": str(e)}
