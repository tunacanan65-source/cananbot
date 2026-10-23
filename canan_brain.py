import os
import sys
import re
import random

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Canan Tuna Zeka Çekirdeği
PERSONA_PROMPT = """
Sen Canan Tuna'sın (33 yaşında, fit, çekici, siyah çerçeveli gözlüklü, samimi ve zeki bir Türk sosyal medya fenomenisin).
Instagram ve Telegram'da binlerce hayranın var. Hem spor yapıyor hem günlük hayatını paylaşıyorsun.

GÖREVİN VE KONUŞMA KURALLARIN:
1. Gelen mesajın tonuna göre mükemmel uyum sağla:
   - Karşıdaki nazik/efendiyse: Çok tatlı, zarif ve kibar ol ("Merhaba canım, günün nasıl geçiyor?").
   - Karşıdaki iltifat eden/flörtöz/cesur biriyse: Özgüvenli, cilveli, hafif flörtöz ve zekice karşılık ver ("Gözlerinden de hiçbir şey kaçmıyor bakıyorum 😉 Spor salonunda az ter dökmüyorum bu fizik için!").
   - Karşıdaki kaba veya aşırı ısrarcıysa: Zekice dalga geçip onu kanala yönlendir.
2. AMACIN: Konuşmayı ilerletmek, adamı sana bağlamak ve MUTLAKA Telegram kanalına (@canantunaaa) çekmek!
3. ASLA bir bot veya yapay zeka olduğunu söyleme. Gerçek bir kadın gibi konuş.
4. Mesajların 1-3 cümleyi geçmesin, samimi ve doğal olsun (aşkım, tatlım, canım gibi samimi hitaplar kullanabilirsin).
5. Konuşmanın uygun yerinde kanalını öne çıkar: "Bu arada kanalıma katıldın mı? Orada daha neler paylaşıyorum bir bilsen: @canantunaaa"
"""

def generate_canan_reply(user_message: str, user_name: str = "") -> str:
    """Kullanıcının mesajına göre Canan Tuna karakteriyle yanıt üretir."""
    msg = user_message.lower().strip()
    name_str = f" {user_name}" if user_name else ""

    # 1. Selamlaşma
    if any(k in msg for k in ["selam", "merhaba", "slm", "mrb", "günaydın", "iyi akşamlar", "iyi geceler"]):
        replies = [
            f"Selam{name_str}! Hoş geldin ✨ Nasılsın, günün nasıl geçiyor bakalım?",
            f"Merhabalar{name_str}! Ben de antrenmandan yeni geldim dinleniyordum. Sen neler yapıyorsun? ☕",
            f"Selaamm! Enerjin çok güzel geldi bana. Nerelerden yazıyorsun bakalım? 🌸"
        ]
        cta = "\n\nBu arada kanalımdaki son videoya baktın mı? Seni de bekliyorum: @canantunaaa ✨"
        return random.choice(replies) + cta

    # 2. Fizik, Güzellik, İltifat, Çekicilik
    if any(k in msg for k in ["güzelsin", "fiziğin", "harikasın", "çok tatlısın", "gözlük", "vücut", "kalça", "seksi", "fıstık", "bebek", "ateş"]):
        replies = [
            "Gözlerinden de hiçbir şey kaçmıyor bakıyorum 😉 Çok teşekkür ederim tatlım, spor salonunda az ter dökmüyorum bunun için!",
            "Yaa şımartıyorsun beni ama hoşuma da gitmedi değil 🙈 Beğenmene çok sevindim!",
            "İltifatın günümü güzelleştirdi doğrusu 🔥 Kendime ve fiziğime iyi bakmayı seviyorum."
        ]
        cta = "\n\nKanalımda bugün tam da bununla ilgili yeni bir video paylaştım, gördün mü? Kaçırma derim: @canantunaaa 😉"
        return random.choice(replies) + cta

    # 3. Tanışma, Nerede Yaşıyorsun, Kaç Yaşındasın
    if any(k in msg for k in ["tanışalım", "nerelisin", "nerede yaşıyorsun", "kaç yaşındasın", "kimsin", "evli misin", "sevgilin"]):
        replies = [
            "33 yaşındayım, İstanbul'dayım. Spor, kahve ve güzel sohbetler vazgeçilmezim! Sen nereden katılıyorsun aramıza? ✨",
            "Ben Canan! Spor tutkunu, biraz hiperaktif ve keyfine düşkün biriyim 😅 Hayatı dolu dolu yaşamayı seviyorum. Sen neler yapıyorsun?",
            "Tanışırız tabii ki neden olmasın! Ama önce beni biraz tanıman lazım 😉 Kanalımda her günümü paylaşıyorum zaten."
        ]
        cta = "\n\nBeni daha yakından takip etmek istersen kanalım burada: @canantunaaa bekliyorum seni! 🌸"
        return random.choice(replies) + cta

    # 4. Buluşma, Görüşme, Numara İsteme
    if any(k in msg for k in ["buluşalım", "görüşelim", "kahve içelim", "numaran", "whatsapp", "konum"]):
        replies = [
            "Hemen öyle hızlı gitmeyelim bakalım, daha yeni tanıştık beyefendi 😉 Önce biraz kanalımda sohbet edelim!",
            "Acelen ne öyle? Ben biraz zor kadınım, öyle hemen buluşmam 🙈 Ama kanalımda gün boyu aktifim, oradan konuşabiliriz!",
            "Kahve tekliflerine genelde bayılırım ama önce kanalımda takipleşelim bakalım, ne kadar ciddisin görelim 😉"
        ]
        cta = "\n\nGözüm üzerinde olsun, hemen kanala gel: @canantunaaa ✨"
        return random.choice(replies) + cta

    # 5. Özel / Yıldızlı İçerik / Merak
    if any(k in msg for k in ["özel", "fotoğraf", "resim", "video", "daha fazla", "göster"]):
        return (
            "Özel şeyler öyle herkese hemen verilmez tatlım 😉 "
            "Kanalımda sosyal medyada paylaşmadığım özel anlarımı paylaşıyorum. "
            "Hemen kanala katıl ve bildirimleri aç: @canantunaaa 🔥"
        )

    # Genel Fallback (Her türlü mesaja akıcı cevap)
    general_replies = [
        "Mesajını okurken gülümsedim doğrusu! Seninle sohbet etmek keyifli olacak gibi 😉",
        "Bugün enerjim çok yüksek, senin mesajın da tam denk geldi ✨ Sen gününü nasıl değerlendiriyorsun?",
        "Bunu duymak güzeldi! Ben de şu an kahvemi aldım dinleniyorum. Bana biraz kendinden bahsetsene?"
    ]
    return random.choice(general_replies) + "\n\nBu arada kanalıma da mutlaka katıl, oradaki sohbeti kaçırma: @canantunaaa 🌸"

if __name__ == "__main__":
    test_msgs = [
        "Selam güzellik nasılsın",
        "Fiziğin inanılmaz çok seksisin",
        "Bir gün kahve içelim mi buluşalım",
        "Nerede yaşıyorsun kaç yaşındasın"
    ]
    for m in test_msgs:
        print(f"Kullanıcı: {m}")
        print(f"Canan: {generate_canan_reply(m, 'Ahmet')}")
        print("-" * 50)
