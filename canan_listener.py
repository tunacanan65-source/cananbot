import os
import sys
import time
import requests
import config
import canan_brain
import canan_autopilot

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_canan_listener():
    """
    Telegram botuna gelen özel mesajları dinler:
    - /paylas veya 'paylaş' yazıldığında anında 3 platforma (Instagram, Facebook, Telegram) yeni içerik basar.
    - Normal mesaj atan takipçilere Canan Tuna AI zekasıyla tatlı yanıtlar verir.
    """
    token = config.TELEGRAM_BOT_TOKEN
    base_url = f"https://api.telegram.org/bot{token}"
    last_update_id = 0

    print("🎧 Canan Tuna DM & Komut Dinleyicisi Başlatıldı...")

    while True:
        try:
            params = {"offset": last_update_id + 1, "timeout": 20}
            resp = requests.get(f"{base_url}/getUpdates", params=params, timeout=25)
            data = resp.json()

            if data.get("ok"):
                for update in data.get("result", []):
                    last_update_id = update["update_id"]
                    msg = update.get("message")
                    if not msg or not msg.get("text"):
                        continue

                    # Sadece özel (private) sohbet mesajlarına yanıt ver
                    chat_type = msg.get("chat", {}).get("type")
                    if chat_type != "private":
                        continue

                    chat_id = msg["chat"]["id"]
                    user_name = msg["from"].get("first_name", "")
                    user_text = msg.get("text", "").strip()

                    print(f"📩 [{user_name}]: {user_text}")

                    # 1. Özel Paylaşım Komutu: /paylas veya 'paylaş'
                    if user_text.lower() in ["/paylas", "paylas", "paylaş", "/paylaş", "/start"]:
                        if user_text.lower() == "/start":
                            welcome_msg = (
                                f"Merhaba {user_name}! Ben Canan Tuna 🌸✨\n\n"
                                "Bana dilediğin zaman yazabilirsin canım. Özel anlarım ve paylaşımlarım için kanalıma beklerim: @canantunaaa 💕\n\n"
                                "💡 Yöneticiysen: İstediğin an /paylas yazarak Instagram, Facebook ve Telegram'a anında yeni gönderi attırabilirsin!"
                            )
                            requests.post(f"{base_url}/sendMessage", json={"chat_id": chat_id, "text": welcome_msg}, timeout=10)
                            continue

                        requests.post(f"{base_url}/sendMessage", json={
                            "chat_id": chat_id,
                            "text": "⏳ Canan Tuna paylaşımı hazırlanıyor... (Instagram + Facebook + Telegram)"
                        }, timeout=10)

                        try:
                            ok = canan_autopilot.run_single_autopilot_post()
                            if ok:
                                result_msg = "✅ Harika! Canan Tuna az önce Instagram, Facebook ve Telegram'a yeni paylaşımını yaptı! 🚀"
                            else:
                                result_msg = "⚠️ Paylaşılacak yeni görsel kalmadı veya bir hata oluştu."
                        except Exception as err:
                            result_msg = f"❌ Paylaşım hatası: {err}"

                        requests.post(f"{base_url}/sendMessage", json={"chat_id": chat_id, "text": result_msg}, timeout=10)
                        continue

                    # 2. Canan Tuna AI Zekasıyla Sohbet Yanıtı
                    reply_text = canan_brain.generate_canan_reply(user_text, user_name)
                    send_payload = {
                        "chat_id": chat_id,
                        "text": reply_text
                    }
                    requests.post(f"{base_url}/sendMessage", json=send_payload, timeout=10)
                    print(f"💬 [Canan]: {reply_text[:60]}... -> Gönderildi!")
            time.sleep(2)
        except Exception as e:
            time.sleep(3)

if __name__ == "__main__":
    run_canan_listener()
