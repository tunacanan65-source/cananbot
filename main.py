import os
import sys
import threading
import time
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import canan_scheduler
import canan_listener
import canan_autopilot

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

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

@app.get("/")
@app.get("/health")
def health():
    return JSONResponse({
        "status": "online",
        "bot": "Canan Tuna AI Influencer",
        "platforms": ["Instagram", "Facebook", "Telegram"],
        "schedule": "13:00 (Hikaye) & 20:30 (Reels)",
        "command": "Telegram'dan /paylas ile anında tetiklenebilir"
    })

@app.get("/api/trigger-post")
def trigger_post():
    """Bulut üzerinden tek tıkla paylaşımı tetikleme API'si"""
    ok = canan_autopilot.run_single_autopilot_post()
    return JSONResponse({"ok": ok})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
