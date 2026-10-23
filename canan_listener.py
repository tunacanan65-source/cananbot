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

                    # 1. Özel Komutlar: /start, /reels, /foto, /paylas
                    user_lower = user_text.lower().strip()

                    if user_lower in ["/start", "/help", "yardım", "komutlar"]:
                        welcome_msg = (
                            f"Merhaba {user_name}! Ben Canan Tuna 🌸✨\n\n"
                            "Bana dilediğin zaman yazabilirsin canım. Özel anlarım ve paylaşımlarım için kanalıma beklerim: @canantunaaa 💕\n\n"
                            "👑 *Yönetici Paylaşım Komutları:*\n"
                            "🎬 `/reels` : Anında estetik müzikli Reels videosu paylaş (Instagram + FB + TG)\n"
                            "📸 `/foto` : Anında yeni yaşam tarzı fotoğrafı paylaş (Instagram + FB + TG)\n"
                            "🚀 `/paylas` : Otonom sıradaki içeriği (fotoğraf veya video) paylaş\n"
                        )
                        requests.post(f"{base_url}/sendMessage", json={"chat_id": chat_id, "text": welcome_msg, "parse_mode": "Markdown"}, timeout=10)
                        continue

                    if user_lower in ["/reels", "reels", "/video", "video"]:
                        requests.post(f"{base_url}/sendMessage", json={
                            "chat_id": chat_id,
                            "text": "🎬 Estetik Canan Tuna REELS videosu hazırlanıyor... (Ken Burns hareketli + telifsiz lofi müzik, sıfır robot sesi) ⏳"
                        }, timeout=10)
                        try:
                            ok = canan_autopilot.run_single_autopilot_post(force_type="video")
                            if ok:
                                result_msg = "✅ Harika! Canan Tuna REELS videosu az önce Instagram Reels, Facebook ve Telegram'a başarıyla yüklendi! 🚀🎬"
                            else:
                                result_msg = "⚠️ Reels üretilirken bir sorun oluştu."
                        except Exception as err:
                            result_msg = f"❌ Reels paylaşım hatası: {err}"

                        requests.post(f"{base_url}/sendMessage", json={"chat_id": chat_id, "text": result_msg}, timeout=10)
                        continue

                    if user_lower in ["/foto", "foto", "/fotograf", "fotoğraf"]:
                        requests.post(f"{base_url}/sendMessage", json={
                            "chat_id": chat_id,
                            "text": "📸 Canan Tuna yeni FOTOĞRAF paylaşımı hazırlanıyor... (Instagram + Facebook + Telegram) ⏳"
                        }, timeout=10)
                        try:
                            ok = canan_autopilot.run_single_autopilot_post(force_type="photo")
                            if ok:
                                result_msg = "✅ Harika! Canan Tuna fotoğrafı az önce Instagram, Facebook ve Telegram'a başarıyla yüklendi! 📸✨"
                            else:
                                result_msg = "⚠️ Fotoğraf paylaşılırken bir sorun oluştu."
                        except Exception as err:
                            result_msg = f"❌ Fotoğraf paylaşım hatası: {err}"

                        requests.post(f"{base_url}/sendMessage", json={"chat_id": chat_id, "text": result_msg}, timeout=10)
                        continue

                    if user_lower in ["/paylas", "paylas", "paylaş", "/paylaş"]:
                        requests.post(f"{base_url}/sendMessage", json={
                            "chat_id": chat_id,
                            "text": "⏳ Canan Tuna sıradaki otonom paylaşımı hazırlanıyor... (Instagram + Facebook + Telegram)"
                        }, timeout=10)

                        try:
                            ok = canan_autopilot.run_single_autopilot_post()
                            if ok:
                                result_msg = "✅ Harika! Canan Tuna az önce Instagram, Facebook ve Telegram'a yeni paylaşımını yaptı! 🚀"
                            else:
                                result_msg = "⚠️ Paylaşım sırasında bir hata oluştu."
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
