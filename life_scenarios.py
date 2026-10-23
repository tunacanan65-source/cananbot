import os

"""
Canan Tuna - Otonom Yaşam Simülasyonu Senaryo Kütüphanesi
Her senaryo kendine özel, sıfırdan üretilmiş BİRİNCİL GÖRSELİNE sahiptir.
Tüm görseller assets/images/ altında bağımsız ve taşınabilir olarak saklanır.
"""

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")

SCENARIOS = [
    # 🌟 5. YENİ: Ateş Kırmızısı Saten Abiye - İtalyan Restoranı (Gece Daveti)
    {
        "id": "gece_kirmizi_italyan_restoran",
        "category": "gece",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_red_dress_restaurant.jpg"),
        "caption": "Kırmızı her kadının gardırobunda en az bir kere olmalı bence... ❤️✨ Mum ışığı, güzel bir akşam yemeği ve hafif İtalyan ezgileri. Kırmızı kombinimi nasıl buldunuz aşklar? 🍷👇",
        "tags": "#kırmızıelbise #gecedaveti #zarafet #dinner #italyan #lifestyle #canantuna #gününkaresi"
    },

    # 🌟 6. YENİ: Zümrüt Yeşili Kruvaze Blazer - Business Executive (İş & Kariyer)
    {
        "id": "is_zumrut_blazer_executive",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_emerald_blazer_office.jpg"),
        "caption": "Yeni projeler, yeni toplantılar ve yüksek hedefler! 💼💚 Zümrüt yeşili blazer'ımın verdiği özgüveni çok seviyorum. Kadın girişimciler ve iş kadınları burada mı? Gücünüzü gösterin! 🚀✨",
        "tags": "#businesswoman #blazer #kariyer #ofisstili #kombin #girişimci #canantuna #stil"
    },

    # 🌟 7. YENİ: Hardal Sarısı Keten Elbise - Alaçatı Begonvilleri (Yaz Sokak Modası)
    {
        "id": "sokak_alacati_sari_elbise",
        "category": "tatil",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_alacati_yellow_dress.jpg"),
        "caption": "Alaçatı sokakları, pembe begonviller ve güneş sarısı bir yaz günü... ☀️🌸 Sarı renk bana inanılmaz pozitif enerji veriyor! Sizin en sevdiğiniz yaz rengi hangisi? Yorumlarda buluşalım 💛👇",
        "tags": "#alaçatı #çeşme #sarıelbise #yazmodası #begonvil #tatil #canantuna #enerji"
    },

    # 🌟 8. YENİ: Pastel Lila Dikişsiz Spor Takımı - Sabah Park Egzersizi (Fitness)
    {
        "id": "spor_lila_park_fitness",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_lilac_fitness_park.jpg"),
        "caption": "Sabah koşusu ve park esnemesi tamamlandı! 💜🌿 Lila spor takımımın enerjisine bayıldım. Güne erken başlamak ve ter atmak gün boyu zinde tutuyor. Bugün kendiniz için ne yaptınız? 💪🔥",
        "tags": "#fitness #sabahsporu #lilatakım #gymgirl #motivasyon #sağlıklıyaşam #canantuna #reels"
    },
    # 🌟 1. YENİ: Kapadokya Balonlar & Mağara Otel Terası (Tatil Fotoğrafı)
    {
        "id": "tatil_kapadokya_balonlar",
        "category": "tatil",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_cappadocia_terrace.jpg"),
        "caption": "Kapadokya'da gün doğumu masal gibi... 🎈✨ Gökyüzündeki balonları izlerken sıcacık kahvemi yudumlamak bana inanılmaz bir huzur verdi. Hayatınızda mutlaka görmeniz gereken yerler listenize ekleyin derim! Siz Kapadokya'ya gittiniz mi aşklar? ☕🌅👇",
        "tags": "#kapadokya #cappadocia #gündoğumu #balon #seyahat #travelblogger #canantuna #huzur"
    },

    # 🌟 2. YENİ: Bebek Sahilinde Kruvasan & Sabah Kahvesi (Sabah Yaşam Fotoğrafı)
    {
        "id": "sabah_bebek_kruvasan_kahve",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_bebek_cafe.jpg"),
        "caption": "Sabah kahvesi ve taze kruvasan klasiği! 🥐☕ Bebek sahilinde güne mis gibi başladım. Tatlı krizine girenler burada mı? Kendinize güzel bir gün hediye edin aşklar 🌸💛",
        "tags": "#bebek #kahvekeyfi #kruvasan #günaydın #istanbul #lifestyle #canantuna #gününkaresi"
    },

    # 🌟 3. YENİ: Ege Lüks Yat Turu & Deniz Esintisi (Müzikli Reels Videosu)
    {
        "id": "tatil_ege_yat_turu",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_yacht_summer.jpg"),
        "caption": "Rüzgar saçımda, masmavi deniz önümde... 🛥️🌊 Bazen her şeyi geride bırakıp denize açılmak en güzel terapi! Yaz tatilini en çok nerede geçirmeyi seviyorsunuz? Yorumları görelim ☀️⚓👇",
        "tags": "#yatturu #deniz #tatil #yaz #summervibes #canantuna #reels #mavi"
    },

    # 🌟 4. YENİ: Boğaz Manzaralı Çatı Terası Golden Hour (Müzikli Reels Videosu)
    {
        "id": "gece_bogaz_cati_terasi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_rooftop_sunset.jpg"),
        "caption": "Altın saatler (Golden hour) ve Boğaz manzarası... 🌇✨ Gün batarken bu şehir bambaşka bir büyüye bürünüyor. Akşam planınız ne canlar? 🍷❤️",
        "tags": "#goldenhour #günbatımı #istanbul #boğaz #rooftop #zarafet #canantuna #reels"
    },
    # 1. Bodrum Beach Club (Bikinili / Mayolu Güneşlenme - Tatil Fotoğrafı)
    {
        "id": "tatil_bodrum_beach",
        "category": "tatil",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_bodrum_beach_1792678870147.jpg"),
        "caption": "Deniz, güneş ve biraz kafa dinlemece... ☀️🌊 Bodrum bana her zaman çok iyi geliyor. Siz tatilde deniz insanı mısınız havuz mu? 🏖️👇",
        "tags": "#bodrum #tatil #beachvibes #güneş #yaz #canantuna #lifestyle"
    },

    # 2. Yağmurlu Karaköy Akşamı (Trenchcoat & Şeffaf Şemsiye - Sokak Fotoğrafı)
    {
        "id": "sokak_karakoy_yagmur",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_karakoy_street_portrait_1792678880948.jpg"),
        "caption": "Yağmurda ıslanmayı seven kaç kişiyiz? 🌧️🌂 Karaköy sokaklarında yürüyüş yapıp kahvemi aldım. Yağmurlu havalar bana inanılmaz ilham veriyor... ✨",
        "tags": "#karaköy #istanbul #yağmur #trenchcoat #sokakmodası #canantuna #lifestyle"
    },

    # 3. Pilates Reformer Stüdyosu (Bebek Mavisi Tayt - Spor Videosu)
    {
        "id": "spor_pilates_reformer",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_pilates_portrait_1792678899801.jpg"),
        "caption": "Reformer seansı bitti, ter atıldı! 💪🧘‍♀️ Vücuduna iyi bakmak kendine yapabileceğin en büyük iyilik. Bugün spora vakit ayırdınız mı canlar? 🔥👇",
        "tags": "#pilates #reformer #fitgirl #spor #sağlıklıyaşam #canantuna #gymmotivation"
    },

    # 4. Boğaz Manzaralı Çatı Katı Akşam Yemeği (Siyah Şık Elbise - Gece Videosu)
    {
        "id": "gece_bogaz_aksam_yemegi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_bosphorus_night_1792678913579.jpg"),
        "caption": "İstanbul geceleri ve Boğaz'ın ışıkları... 🌉✨ Bazen sadece durup bu şehrin tadını çıkarmak gerekiyor. Akşamınız nasıl geçiyor aşklar? 🍷❤️",
        "tags": "#boğaz #istanbul #iyigeceler #şekerim #canantuna #gecehayatı #dinner"
    },

    # 5. İstanbul Trafiğinde Araba İçi Selfie (Direksiyon Başında - Gündüz Videosu)
    {
        "id": "sokak_araba_selfie",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_driver_selfie_1792678924695.jpg"),
        "caption": "İstanbul trafiği klasiği: Kırmızı ışıkta selfie çekilir! 🚗💨 Şarkımı açtım enerjimi düşürmüyorum. Trafikte olanlara sabırlar diliyorum 🙈🎧",
        "tags": "#istanbul #trafik #selfie #carselfie #gününkaresi #canantuna #enerji"
    },

    # 6. Balkonda Çıplak Ayak Kahve Keyfi (Hırka & Şort - Sabah Dinlenme Fotoğrafı)
    {
        "id": "ev_balkon_ciplak_ayak",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_cozy_balcony_portrait_1792678939456.jpg"),
        "caption": "Balkonda sabah kahvesi, serin hava ve sessizlik... ☕🌿 Bütün gün böyle oturabilirim. Güne güzel bir başlangıç yaptık, sizde durumlar ne? 🌸👇",
        "tags": "#günaydın #kahvekeyfi #huzur #evhali #balkonkeyfi #canantuna #gününkaresi"
    },

    # 7. Nişantaşı Kafe Molası (Deri Ceket & İced Coffee - Gündüz Fotoğrafı)
    {
        "id": "sokak_nisantasi_kafe",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tana_nisantasi_cafe_1792666291150.jpg"),
        "caption": "Nişantaşı sokakları ve buz gibi bir filtre kahve... ☕🕶️ Enerjim tavan! Bugün kendiniz için ne yaptınız aşklar? 👇✨",
        "tags": "#nişantaşı #istanbul #kahvekeyfi #sokakmodası #canantuna #lifestyle"
    },

    # 8. Sabah Ev Rutini (Mutfak & Sıcak Kupa - Sabah Videosu)
    {
        "id": "ev_sabah_kahvesi",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_morning_lifestyle_1792660779429.jpg"),
        "caption": "Güne kahvesiz başlayamayanlar el kaldırsın! ☕☀️ Bugünün mottosu: Gülümse ve anı yaşa! Harika bir gün olsun hepimize 🌸💛",
        "tags": "#günaydın #sabahkahvesi #evhali #huzur #canantuna #pozitifenerji"
    },

    # 9. Kış Günü Sıcak Kahve (Karlı Sokak & Puffer Mont - Kış Fotoğrafı)
    {
        "id": "sokak_kis_sicak_kahve",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_winter_street_1792666325312.jpg"),
        "caption": "Hava buz gibi ama içimizi ısıtan kahvemiz var ❄️☕ Karlı günlerde sokakta yürümek bana hep masal gibi gelir. Siz kış insanı mısınız? ☃️🤍",
        "tags": "#kış #kar #soğuk #kahvekeyfi #canantuna #wintervibes"
    },

    # 10. Spor Salonu Ayna İlerlemesi (Tayt & Crop Top - Spor Videosu)
    {
        "id": "spor_gym_ayna_selfie",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_fitness_selfie_1792663898849.jpg"),
        "caption": "Bahane yok, disiplin var! 🔥💪 Bugünkü antrenmanı tamamladım. Aynadaki değişimi görmek en büyük motivasyonum! Siz başladınız mı? 🏋️‍♀️",
        "tags": "#fitness #gymmotivation #fitgirl #disiplin #spor #canantuna #workout"
    },

    # 11. Yoğun Antrenman Sonrası Halı Keyfi (Pembe Spor Sütyeni - Akşamüstü Fotoğrafı)
    {
        "id": "spor_sonrasi_hali_dinlenme",
        "category": "spor",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_post_workout_1792664056043.jpg"),
        "caption": "Bacak gününden sonra halıya serilenler derneği başkanı seçildim sanırım! 🙈😂 Yorulduk ama değdi. Şimdi güzel bir dinlenme zamanı 💆‍♀️✨",
        "tags": "#postworkout #fitlife #dinlenme #yorgunluk #canantuna #gymgirl"
    },

    # 12. Pazar Rahatlığı (Krem Örgü Kazak - Ev Fotoğrafı)
    {
        "id": "ev_pazar_rahatligi",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_cozy_livingroom_png_1792663231002.jpg"),
        "caption": "Evde battaniye ve sıcak bir çay modundayım bugün... 🛋️📖 Bazen hiçbir şey yapmamak da ruhuna çok iyi gelir. Bugün evde misiniz dışarıda mı? 🍵👇",
        "tags": "#evkeyfi #huzur #cozyvibes #dinlenme #canantuna #haftasonu"
    },

    # 13. Güneşli Balkon Portresi (Lila Crop Top - Gündüz Videosu)
    {
        "id": "ev_gunesli_balkon_selfie",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_selfie_1792665280198.jpg"),
        "caption": "Güneş açtıysa enerjimiz de yerine gelir! ☀️🌸 Yepyeni hedefler, güzel başlangıçlar... Gününüz harika geçsin canlar! 💖✨",
        "tags": "#güneş #pozitifenerji #selfie #balkonkeyfi #canantuna #gününkaresi"
    },

    # 14. Vanity Aynası & Parfüm (Lüks Giyinme Odası - Reels Videosu)
    {
        "id": "lifestyle_vanity_mirror_makyaj",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_vanity_mirror.jpg"),
        "caption": "Hazırlanırken aynaya bir bakış ve günün enerjisini yakalama anı... ✨💄 Kendinize değer verdiğiniz her an çok kıymetli. Akşam planları yapıldı mı canlar? 💋👠",
        "tags": "#vanity #grwm #lifestyle #makyaj #güzellik #canantuna #mirrorselfie"
    },

    # 15. Tenis / Padel Kortu (Kort Şıklığı & Raket - Spor Videosu)
    {
        "id": "spor_kortta_tenis_padel",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tennis_court.jpg"),
        "caption": "Kortta maç bitti ama enerji hala tavan! 🎾🔥 Spor sadece bedenine değil ruhuna da iyi gelen en güzel terapi. Bugün hareket ettik mi? 💪✨",
        "tags": "#tennis #padel #tenis #fitgirl #sportystyle #canantuna #fitnessmotivation"
    },

    # 16. Sonsuzluk Havuzu & Gün Batımı (Lüks Tatil & Ege Manzarası - Reels Videosu)
    {
        "id": "tatil_sonsuzluk_havuzu_gunbatimi",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_infinity_pool.jpg"),
        "caption": "Gün batımında sonsuzluğa karşı durup derin bir nefes almak... 🌅🌊 Hayat koşturmacasında durup anın tadını çıkarmayı unutmayın. Huzur dolu bir akşam olsun hepimize 🧡✨",
        "tags": "#sunset #infinitypool #tatil #manzara #huzur #canantuna #travelgram #goldenhour"
    },

    # 17. Çağdaş Sanat Galerisi (Bej Blazer & Modern Sanat - Kültür Sokak Fotoğrafı)
    {
        "id": "kultur_cagdas_sanat_galerisi",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_art_gallery.jpg"),
        "caption": "Sanatın içinde kaybolduğum, renklerin hikayesini dinlediğim bir gün... 🎨🖼️ Modern sanat bana her zaman yeni bakış açıları kazandırıyor. Galerileri gezmeyi sevenler burda mı? 🤍✨",
        "tags": "#artgallery #sanat #istanbul #modernart #kultur #canantuna #streetstyle #ootd"
    }
]

def get_scenario_by_id(scenario_id: str) -> dict:
    for s in SCENARIOS:
        if s["id"] == scenario_id:
            return s
    return SCENARIOS[0]
