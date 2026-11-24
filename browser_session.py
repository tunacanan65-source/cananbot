"""
Canan Tuna - Ortak Tarayıcı Oturum Yardımcısı (Ev PC'si + GitHub Actions Bulutu)
- Ev PC'sinde: kalıcı Chrome profili veya yerel *_cookies.json dosyası kullanılır.
- Bulutta (GitHub Actions): Çerezler GitHub Secrets'tan (base64 JSON) okunur, diske yazılmaz.
"""
import os
import sys
import json
import base64

IS_CLOUD = os.environ.get("GITHUB_ACTIONS", "").lower() == "true"

if sys.platform.startswith("win"):
    REAL_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
else:
    REAL_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

LAUNCH_ARGS = ["--disable-blink-features=AutomationControlled", "--no-sandbox"]


def load_cookies(env_name: str, local_file: str, domain_keywords: tuple) -> list:
    """Önce ortam değişkeninden (bulut), yoksa yerel dosyadan çerezleri yükler ve sadece ilgili alan adlarını tutar."""
    cookies = []
    raw = os.environ.get(env_name, "").strip()
    if raw:
        try:
            if not raw.startswith("["):
                raw = base64.b64decode(raw).decode("utf-8")
            cookies = json.loads(raw)
        except Exception as e:
            print(f"⚠️ [Oturum] {env_name} çözülemedi: {e}")
            cookies = []
    elif os.path.exists(local_file):
        try:
            with open(local_file, "r", encoding="utf-8") as f:
                cookies = json.load(f)
        except Exception as e:
            print(f"⚠️ [Oturum] {os.path.basename(local_file)} okunamadı: {e}")
            cookies = []

    clean = []
    for c in cookies:
        dom = (c.get("domain") or "").lower()
        if not any(k in dom for k in domain_keywords):
            continue
        item = {k: c[k] for k in ("name", "value", "domain", "path", "expires", "httpOnly", "secure", "sameSite") if k in c}
        if item.get("sameSite") not in ("Strict", "Lax", "None"):
            item["sameSite"] = "Lax"
        clean.append(item)
    return clean


def launch_browser(p, prefer_chrome: bool = True):
    """Ev PC'sinde gerçek Chrome, bulutta Chrome yoksa Playwright Chromium açar."""
    if prefer_chrome:
        try:
            return p.chromium.launch(headless=True, channel="chrome", args=LAUNCH_ARGS,
                                     ignore_default_args=["--enable-automation"])
        except Exception:
            pass
    return p.chromium.launch(headless=True, args=LAUNCH_ARGS, ignore_default_args=["--enable-automation"])
