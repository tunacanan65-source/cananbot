import os
import sys
import threading
import time
from contextlib import asynccontextmanager
import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import config
import canan_scheduler
import canan_listener
import canan_autopilot

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

def start_scheduler_thread():
    print("⏰ [Canan Cloud] 7/24 Zamanlayıcı başlatılıyor...")
    canan_scheduler.run_scheduler()

def start_listener_thread():
    print("🎧 [Canan Cloud] Telegram Dinleyici & /paylas Komut Takipçisi başlatılıyor...")
    canan_listener.run_canan_listener()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. 7/24 Zamanlayıcıyı arka plan iş parçacığı olarak başlat
    t_sched = threading.Thread(target=start_scheduler_thread, daemon=True)
    t_sched.start()

    # 2. Telegram DM & Komut dinleyicisini arka planda başlat
    t_list = threading.Thread(target=start_listener_thread, daemon=True)
    t_list.start()

    print("🚀 [Canan Cloud] Canan Tuna 7/24 Bulut Servisi Tamamen Aktif Edildi!")
    yield

app = FastAPI(title="Canan Tuna AI Influencer Cloud Engine", lifespan=lifespan)

# Meta / Instagram ve Facebook doğrudan medya CDN servisi (Catbox/Tmpfiles bağımlılığını ve Cloudflare engellerini yok eder)
app.mount("/media", StaticFiles(directory=OUTPUT_DIR), name="media")
app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")

@app.get("/")
@app.get("/health")
def health():
    return JSONResponse({
        "status": "online",
        "bot": "Canan Tuna AI Influencer",
        "platforms": ["Instagram", "Facebook", "Telegram"],
        "schedule": "13:00 (Hikaye/Fotoğraf) & 20:30 (Reels)",
        "command": "Telegram'dan /paylas ile anında tetiklenebilir"
    })

@app.get("/api/token-status")
def token_status():
    """Facebook & Instagram Meta Token canlı sağlık durumunu raporlar."""
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "")
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "")

    status = {"facebook": False, "instagram": False, "page_name": None, "ig_username": None, "error": None}
    if not token:
        status["error"] = "Token tanımlı değil"
        return JSONResponse(status)

    try:
        r_page = requests.get(f"https://graph.facebook.com/v21.0/{page_id}?fields=id,name&access_token={token}", timeout=8).json()
        if "error" not in r_page:
            status["facebook"] = True
            status["page_name"] = r_page.get("name")
        else:
            status["error"] = r_page["error"].get("message")

        r_ig = requests.get(f"https://graph.facebook.com/v21.0/{ig_id}?fields=id,username&access_token={token}", timeout=8).json()
        if "error" not in r_ig:
            status["instagram"] = True
            status["ig_username"] = r_ig.get("username")
    except Exception as e:
        status["error"] = str(e)

    return JSONResponse(status)

@app.get("/api/trigger-post")
def trigger_post():
    """Bulut üzerinden tek tıkla paylaşımı tetikleme API'si"""
    ok = canan_autopilot.run_single_autopilot_post()
    return JSONResponse({"ok": ok})

@app.get("/api/trigger-reels")
def trigger_reels():
    """Bulut üzerinden tek tıkla Reels paylaşımı tetikleme API'si"""
    try:
        ok = canan_autopilot.run_single_autopilot_post(force_type="video")
        return JSONResponse({"ok": ok, "type": "reels"})
    except Exception as e:
        import traceback
        err = traceback.format_exc()
        print(f"❌ [Trigger Reels Error]: {err}")
        return JSONResponse({"ok": False, "error": str(e), "traceback": err}, status_code=500)

@app.get("/api/trigger-photo")
def trigger_photo():
    """Bulut üzerinden tek tıkla Fotoğraf paylaşımı tetikleme API'si"""
    ok = canan_autopilot.run_single_autopilot_post(force_type="photo")
    return JSONResponse({"ok": ok, "type": "photo"})

@app.get("/privacy")
def privacy_policy():
    from fastapi.responses import HTMLResponse
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head><title>Canan Tuna Privacy Policy</title><meta charset='utf-8'></head>
    <body style='font-family:sans-serif; max-width:800px; margin:40px auto; line-height:1.6; padding:0 20px;'>
        <h2>Canan Tuna Gizlilik Politikası (Privacy Policy)</h2>
        <p>Canan Tuna AI Influencer uygulaması kullanıcı verilerinin gizliliğine saygı duyar.</p>
        <p>Bu uygulama yalnızca Instagram ve Facebook Graph API üzerinden içerik paylaşımı amacıyla kullanılmaktadır. Herhangi bir kişisel veri toplanmaz veya üçüncü taraflarla paylaşılmaz.</p>
        <p>İletişim: tunacanan65@gmail.com</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
