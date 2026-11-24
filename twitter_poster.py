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
                context = browser.new_context(user_agent=bs.REAL_UA, viewport={"width": 1366, "height": 900},
                                              locale="tr-TR", timezone_id="Europe/Istanbul")
                context.add_cookies(x_cookies)
            page = context.pages[0] if context.pages else context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

            print("🌐 [Twitter] X Ana Sayfa açılıyor...")
            page.goto("https://x.com/home", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(4500)

            if "login" in page.url.lower():
                context.close()
                return {"status": "error", "reason": "Twitter oturumu henüz açık değil."}

            # Varsa çerez / bildirim popuplarını kapat
            for txt in ["Accept all cookies", "Tüm çerezleri kabul et", "Refuse non-essential cookies", "Not now", "Şimdi değil", "Got it", "Anladım"]:
                btn = page.locator(f'button:has-text("{txt}"), span:has-text("{txt}")')
                if btn.count():
                    try:
                        btn.first.click(force=True)
                        page.wait_for_timeout(600)
                    except Exception:
                        pass

            # 1. Önce Tweet metin kutusunu ("Neler oluyor?") bul, tıkla ve yazıyı gir
            textbox = page.locator('[data-testid="tweetTextarea_0"], div[role="textbox"], div[contenteditable="true"]').first
            if not textbox.count():
                placeholder = page.locator('div:has-text("Neler oluyor?"), div:has-text("What is happening")').last
                if placeholder.count():
                    try:
                        placeholder.click(force=True)
                        page.wait_for_timeout(800)
                    except Exception:
                        pass
                textbox = page.locator('[data-testid="tweetTextarea_0"], div[role="textbox"], div[contenteditable="true"]').first

            if textbox.count():
                print("✍️ [Twitter] Tweet metni yazılıyor...")
                try:
                    textbox.click(force=True)
                    page.wait_for_timeout(500)
                    page.keyboard.insert_text(tweet_text)
                    page.wait_for_timeout(1000)
                except Exception as te:
                    print(f"⚠️ [Twitter] Metin uyarısı: {te}")

            # 2. Medya yükleme inputuna dosyayı aktar
            file_input = page.locator('input[type="file"]').first
            if not file_input.count():
                context.close()
                return {"status": "error", "reason": "Twitter dosya yükleme alanı (input[type=file]) bulunamadı."}

            print(f"📤 [Twitter] Medya dosyası aktarılıyor ({os.path.basename(media_path)})...")
            file_input.set_input_files(media_path)
            page.wait_for_timeout(2000)

            # 3. Gönderi (Post) butonunu bul ve aktifleşmesini bekle
            wait_loops = 24 if is_video else 6
            post_btn = page.locator('[data-testid="tweetButtonInline"], [data-testid="tweetButton"]').first
            if not post_btn.count():
                # Türkçe arayüzde "Gönderi" yazan sağdaki inline buton
                post_btn = page.locator('button:has-text("Gönderi"), [role="button"]:has-text("Gönderi")').last

            for i in range(wait_loops):
                page.wait_for_timeout(2000)
                # Tekrar bul
                cand = page.locator('[data-testid="tweetButtonInline"], [data-testid="tweetButton"]').first
                if cand.count():
                    post_btn = cand
                if post_btn.count():
                    aria_disabled = post_btn.get_attribute("aria-disabled")
                    is_dis = False
                    try:
                        is_dis = post_btn.is_disabled()
                    except Exception:
                        pass
                    if not is_dis and aria_disabled != "true" and i >= (8 if is_video else 2):
                        break

            if not post_btn.count():
                context.close()
                return {"status": "error", "reason": "Twitter Gönderi butonu bulunamadı."}

            print("🚀 [Twitter] 'Gönderi / Post' butonuna tıklanıyor...")
            post_btn.click(force=True)
            page.wait_for_timeout(6000)

            # Eğer "Kilidi aç / Unlock more on X" veya benzeri bir bilgi popup'ı çıkarsa Got it / Anladım / Kapat tıkla
            for txt in ["Got it", "Anladım", "Tamam", "Kapat", "Close", "Şimdi değil", "Not now"]:
                pop = page.locator(f'button:has-text("{txt}"), [role="button"]:has-text("{txt}")')
                if pop.count():
                    try:
                        pop.first.click(force=True)
                        page.wait_for_timeout(1500)
                    except Exception:
                        pass

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
