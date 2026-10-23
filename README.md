# Canan Tuna - 7/24 Otonom AI Influencer Bulut Motoru

Bu proje, **Canan Tuna** AI Influencer karakterinin hiçbir insan müdahalesine gerek kalmadan 7/24 otonom şekilde:
1. **Instagram (`@canantuna_official`)**
2. **Facebook (`Canan tunau`)**
3. **Telegram (`@canantunaaa`)**

üzerinde eşzamanlı olarak içerik üretmesini ve yayınlamasını sağlar.

---

## 📅 Yayın Düzeni (Günde 2 Paylaşım)
* **☀️ 13:00 (Öğlen):** 1 Estetik Hikaye / Fotoğraf (Kombin, sokak, kafe, ev hali)
* **🌙 20:30 (Akşam):** 1 Müzikli Reels Videosu (1080x1920 dikey sinematik süzülme, telifsiz estetik müzik, sıfır yapay zeka sesi)

---

## 📱 Telegram'dan Cep Telefonuyla Anında Paylaşım
Botun Telegram hesabına (veya grubuna) telefonunuzdan:
* `/paylas` veya `paylaş`

yazdığınız anda, bilgisayarınız kapalı olsa bile bulut sunucusu saniyeler içinde yeni bir Reels/Fotoğraf üretir ve Instagram, Facebook ve Telegram'a anında fırlatır!

---

## ☁️ Render.com Üzerinde 7/24 Kesintisiz Çalıştırma (Ücretsiz)
1. Bu klasörü Canan Tuna adına açacağınız yeni ve bağımsız bir GitHub deposuna yükleyin (örneğin: `canan-influencer-bot`).
2. [render.com](https://render.com) üzerinde **New Web Service** deyin ve bu depoyu seçin:
   * **Runtime:** Python 3
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. "Create Web Service" butonuna tıklayın. 
4. Artık bilgisayarınız kapalı olsa bile Canan Tuna 365 gün 24 saat buluttan kendi kendine paylaşım yapmaya devam eder!
