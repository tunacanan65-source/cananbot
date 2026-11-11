import os

"""
Canan Tuna - Dev Otonom Yaşam & Glamour Simülasyonu Senaryo Kütüphanesi (117 Benzersiz Senaryo)
- 16 Özel Oje / Ayak Bakımı / Barefoot Senaryosu
- 40 Özel Cesur / Glamour / Bacak & Dekolte Detaylı Senaryo
- 61 Klasik Lüks Yaşam & Spor Senaryosu
"""

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")

SCENARIOS = [
    {
        "id": 'kuzen_burcu_kirmizi_pembe_oje_1',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "priority_first": True,
        "hook": 'Kuzenim Burcu ile bakım gecesi! Kırmızı mı Pembe mi?',
        "scene_hooks": [
            'Kuzenim Burcu ile bakım gecesi! Kırmızı mı Pembe mi?',
            'İddiaya girdik, kimin ojesi ve bacakları daha güzel?',
            'Ojemiz bitti! Esmer Canan (1) mı Sarışın Burcu (2) mu?',
            'Kaybeden yemek ısmarlıyor! Canan (1) mı Burcu (2) mu?'
        ],
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_red_pink_oje_1.jpg'),
        "companions": [
            os.path.join(IMAGES_DIR, 'canan_cousin_red_pink_oje_2.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_red_pink_oje_3.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_red_pink_oje_4.jpg')
        ],
        "signatures": ['kuzenim burcu ile bu akşam iddiaya girdik', 'kırmızı oje ve kırmızı kombin mi yoksa burcunun pembesi mi'],
        "caption": 'Kuzenim Burcu ile bu akşam iddiaya girdik, kaybeden yarın akşam yemeğini ısmarlıyor! 💅🔥 Ben kırmızı saten kombinim ve kırmızı ojemle (1), Burcu ise pembe saten kombini ve pembe ojesiyle (2) karşınızda! Videoyu son kareye kadar dikkatle izleyin; sizce Esmer Canan (1) mı yoksa Sarışın Kuzenim Burcu (2) mu kazandı? Hakem sizsiniz, yoruma yazın bakalım! 😉👇',
        "tags": '#kuzen #ojekeyfi #kırmızıoje #pembeoje #bakımgecesi #esmer #sarışın #canantuna #reels #keşfet'
    },
    {
        "id": 'kuzen_burcu_siyah_beyaz_oje_1',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "priority_first": True,
        "hook": 'Kuzenim Burcu ile yeni iddia! Siyah mı Beyaz mı?',
        "scene_hooks": [
            'Kuzenim Burcu ile yeni iddia! Siyah mı Beyaz mı?',
            'Bordo oje mi yoksa Beyaz oje mi daha çekici?',
            'Bakım bitti! Esmer Canan (1) mı Sarışın Burcu (2) mu?',
            'Geceye hazırız! Favorin 1 mi yoksa 2 mi? Yoruma yaz!'
        ],
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_black_white_oje_1.jpg'),
        "companions": [
            os.path.join(IMAGES_DIR, 'canan_cousin_black_white_oje_2.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_black_white_oje_3.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_night_dresses.jpg')
        ],
        "signatures": ['kuzenim burcu ile siyah ve beyazın rekabetini', 'ben siyah satenim ve bordo ojemle'],
        "caption": 'Kuzenim Burcu ile siyah ve beyazın rekabetini başlattık! 🖤🤍 Ben siyah satenim ve bordo ojemle (1), Burcu ise beyaz sateni ve beyaz ojesiyle (2) bakım modunda. Son karedeki gece elbiselerimize kadar izleyin; bu sefer oyunu kime veriyorsun? Canan (1) mı, Burcu (2) mu? 🔥👇',
        "tags": '#kuzen #siyahbeyaz #pedikür #bordo #beyazoje #bakım #canantuna #reels #keşfet'
    },
    {
        "id": 'kuzen_burcu_sabah_kahvesi',
        "category": 'ev',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile sabah kahvesi! Günaydın tatlım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_coffee_morning.jpg'),
        "signatures": ['kuzenim burcu ile balkonda sabah kahvesi', 'dün akşamki oje mesaimizden sonra'],
        "caption": 'Dün akşamki oje mesaimizden sonra kuzenim Burcu ile balkonda sabah kahvesi keyfi! ☕☀️ Ojelerimiz hala ilk günkü gibi parlak. Bize katılmak isteyen var mı, kahveler bizden! 🥰👇',
        "tags": '#sabahkahvesi #kuzen #balkonkeyfi #ojeler #günaydın #canantuna #lifestyle'
    },
    {
        "id": 'kuzen_burcu_havuz_basi_ayaklar',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Kuzenim Burcu ile havuz keyfi! Kimin ojesi daha güzel?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_poolside_feet.jpg'),
        "signatures": ['kuzenim burcu ile güneşin ve havuzun tadını', 'ayaklarımızı serin sulara bıraktık'],
        "caption": 'Kuzenim Burcu ile güneşin ve havuzun tadını çıkarıyoruz! 🏊‍♀️☀️ Ayaklarımızı serin sulara bıraktık, kırmızı ve pembe ojelerimiz güneşin altında parlıyor. Yanımızdaki şezlong boş, kimler gelmek isterdi? 😉👇',
        "tags": '#havuzbaşı #kuzen #yazkeyfi #bikini #oje #tatil #canantuna #reels'
    },
    {
        "id": 'kuzen_burcu_film_gecesi_koltuk',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Kuzenim Burcu ile film gecesi! Yanımıza kim geliyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_couch_movie_feet.jpg'),
        "signatures": ['mısırlarımızı patlattık kuzenim burcu ile', 'uzattık ayaklarımızı film seçiyoruz'],
        "caption": 'Mısırlarımızı patlattık, kuzenim Burcu ile ayaklarımızı uzatıp film gecesi yapıyoruz! 🍿🎬 Ama hala hangi filmi izleyeceğimize karar veremedik. Bize güzel bir film önerir misin tatlım? 👇✨',
        "tags": '#filmgecesi #kuzen #evkeyfi #bakımlı #kırmızı #pembe #canantuna #reels'
    },
    {
        "id": 'kuzen_burcu_lila_mercan_oje_yatak',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Kuzenim Burcu ile yatakta bakım! Lila mı Mercan mı?',
        "scene_hooks": [
            'Kuzenim Burcu ile yatakta bakım! Lila mı Mercan mı?',
            'Mürdüm oje mi yoksa Mercan oje mi daha çekici?',
            'Bakım tamam! Esmer Canan (1) mı Sarışın Burcu (2) mu?',
            'Pijama partimizden selam! Favorin 1 mi 2 mi? Seç!'
        ],
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_purple_coral_oje_1.jpg'),
        "companions": [
            os.path.join(IMAGES_DIR, 'canan_cousin_purple_coral_oje_2.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_purple_coral_oje_3.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_balcony_evening_wine.jpg')
        ],
        "signatures": ['kuzenim burcu ile bu gece pijama partisi ve oje', 'ben lila saten takımım ve mürdüm ojemle'],
        "caption": 'Kuzenim Burcu ile bu gece pijama partisi ve oje mesaisindeyiz! 💜🧡 Ben lila saten takımım ve mürdüm ojemle (1), Burcu ise mercan saten takımı ve mercan ojesiyle (2) yarışıyor! Videoyu sonuna kadar izleyin; bu gecenin kazananı Canan (1) mı yoksa Burcu (2) mu? Yoruma yazın! 😉👇',
        "tags": '#kuzen #pijamapartisi #ojekeyfi #pedikür #esmer #sarışın #canantuna #reels #keşfet'
    },
    {
        "id": 'kuzen_burcu_kabin_ayna_kombin',
        "category": 'lifestyle',
        "type": 'video',
        "bold": True,
        "hook": 'Burcu ile alışverişteyiz! Kırmızı (1) mı Mavi (2) mi?',
        "scene_hooks": [
            'Burcu ile alışverişteyiz! Kırmızı (1) mı Mavi (2) mi?',
            'Mutfakta buzlu kahve molası! Hangi şort kombini?',
            'Teras gün batımı! Siyah (1) mı Rose-Gold (2) mu?',
            'Esmer Canan (1) mı Sarışın Burcu (2) mu? Favorini yaz!'
        ],
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_fitting_room_mirror.jpg'),
        "companions": [
            os.path.join(IMAGES_DIR, 'canan_cousin_kitchen_shorts_barefoot.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_terrace_sunset_drinks.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_balcony_evening_wine.jpg')
        ],
        "signatures": ['kuzenim burcu ile mağaza kabininde elbise deniyoruz', 'kırmızı mini elbise mi yoksa saks mavisi mi'],
        "caption": 'Kuzenim Burcu ile alışverişe çıktık, kabinde elbise denemekten yorulduk! 👗🛍️ Benim üzerimdeki kırmızı mini elbise (1) mi daha çok yakışmış yoksa Burcu nun saks mavisi elbisesi (2) mi? Karar veremedik, bize yardımcı olun tatlım! 🔥👇',
        "tags": '#alışveriş #kuzen #minielbise #kabin #kırmızı #mavi #canantuna #reels #keşfet'
    },
    {
        "id": 'kuzen_burcu_yat_tatil_gunes',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Kuzenim Burcu ile yat keyfi! Beyaz (1) mı Turkuaz (2) mı?',
        "scene_hooks": [
            'Kuzenim Burcu ile yat keyfi! Beyaz (1) mı Turkuaz (2) mı?',
            'Kumsalda güneşleniyoruz! Kırmızı mı Sarı bikini mi?',
            'Spa ve jakuzi molası! Enerjimiz 10 üzerinden kaç?',
            'Tatil ikilisi! Canan (1) mı Burcu (2) mu? Seç bakalım!'
        ],
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_yacht_sunbed_feet.jpg'),
        "companions": [
            os.path.join(IMAGES_DIR, 'canan_cousin_beach_sand_toes.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_spa_jacuzzi_relax.jpg'),
            os.path.join(IMAGES_DIR, 'canan_cousin_poolside_feet.jpg')
        ],
        "signatures": ['kuzenim burcu ile tekne güvertesinde güneşleniyoruz', 'beyaz bikini mi turkuaz bikini mi'],
        "caption": 'Kuzenim Burcu ile tekne güvertesinde güneşin ve Ege nin tadını çıkarıyoruz! 🛥️☀️ Beyaz bikinimle ben (1) mi yoksa turkuaz bikinisiyle Burcu (2) mu? 4 kareyi de izleyip favorinizi yoruma bırakın bakalım! 😉👇',
        "tags": '#yatturu #kuzen #bikini #tatil #güneş #plaj #canantuna #reels #keşfet'
    },
    {
        "id": 'kuzen_burcu_mutfak_buzlu_kahve',
        "category": 'ev',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile mutfakta buzlu kahve hazırlığı!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_kitchen_shorts_barefoot.jpg'),
        "signatures": ['kuzenim burcu ile mutfağa girdik buzlu kahvelerimizi', 'evde yalınayak şortlarla rahatlık gibisi yok'],
        "caption": 'Kuzenim Burcu ile mutfağa girdik, kendi ellerimizle buzlu kahve hazırladık! 🧋🌸 Evde yalınayak rahat şortlarla takılmak gibisi yok. Bir bardak da fazladan yaptık, kimler içmeye gelir? 🥰👇',
        "tags": '#mutfak #kahvekeyfi #kuzen #evhali #şort #yalınayak #canantuna #lifestyle'
    },
    {
        "id": 'kuzen_burcu_araba_yolculuk',
        "category": 'sokak',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile yola çıktık! Nereye gidiyoruz?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_car_roadtrip_selfie.jpg'),
        "signatures": ['kuzenim burcu ile güneşli havayı görünce kendimizi yollara', 'araba yolculuğunda yan koltukta müzik'],
        "caption": 'Güneşli havayı görünce kuzenim Burcu ile kendimizi yollara attık! 🚗☀️ Müzik açık, enerjimiz yerinde. Sizce nereye doğru gidiyoruz, doğru tahmin edene benden sürpriz kalp! 😉👇',
        "tags": '#yolculuk #roadtrip #kuzen #arabaselfie #haftasonu #canantuna #keşfet'
    },
    {
        "id": 'kuzen_burcu_spa_jakuzi',
        "category": 'tatil',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile spa ve jakuzi keyfi!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_spa_jacuzzi_relax.jpg'),
        "signatures": ['kuzenim burcu ile tüm haftanın yorgunluğunu jakuzide', 'bordo bikini mi altın sarısı bikini mi'],
        "caption": 'Kuzenim Burcu ile tüm haftanın yorgunluğunu sıcak spa havuzunda atıyoruz... 🧖‍♀️💦 Ayaklarımızı suya uzattık, huzur dolduk. Bordo bikinim (1) mi, Burcu nun altın tonlu bikinisi (2) mi? 🔥👇',
        "tags": '#spa #jakuzi #kuzen #dinlenme #bikini #bakım #canantuna #lifestyle'
    },
    {
        "id": 'kuzen_burcu_teras_gunbatimi',
        "category": 'gece',
        "type": 'photo',
        "bold": True,
        "hook": 'Burcu ile gün batımında teras keyfi! Siyah mı Pembe mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_terrace_sunset_drinks.jpg'),
        "signatures": ['gün batımında kuzenim burcu ile deniz manzaralı terasta', 'siyah saten elbisem mi rose gold mu'],
        "caption": 'Gün batımında kuzenim Burcu ile deniz manzaralı terasta akşam keyfi! 🍹🌅 Siyah saten mini elbisem (1) mi yoksa Burcu nun rose-gold saten elbisesi (2) mi daha şık olmuş? Yorumlarda buluşalım! ✨👇',
        "tags": '#günbatımı #teras #kuzen #satenelbise #akşamkeyfi #canantuna #şıklık'
    },
    {
        "id": 'kuzen_burcu_kumsal_sezlong',
        "category": 'tatil',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile kumsalda! Kırmızı mı Sarı mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_beach_sand_toes.jpg'),
        "signatures": ['ayaklarımızı sıcak kumlara uzattık kuzenim burcu ile', 'kırmızı bikini mi sarı bikini mi'],
        "caption": 'Ayaklarımızı sıcak altın kumlara uzattık, kuzenim Burcu ile plajın keyfini çıkarıyoruz! 🏖️☀️ Kırmızı bikini (Canan) mı, sarı bikini (Burcu) mu? Güneşten daha sıcak olan hangisi? 😉🔥👇',
        "tags": '#plaj #kumsal #kuzen #kırmızıbikini #yaz #tatil #canantuna #beach'
    },
    {
        "id": 'kuzen_burcu_evde_yoga_esneklik',
        "category": 'spor',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile evde spor bitti! Enerji nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_livingroom_rug_stretch.jpg'),
        "signatures": ['evde kuzenim burcu ile yoga ve esneme antrenmanımızı', 'yalınayak matın üzerinde dinlenme vakti'],
        "caption": 'Evde kuzenim Burcu ile yoga ve esneme antrenmanımızı bitirdik, matın üzerinde yalınayak dinleniyoruz! 🧘‍♀️🌸 Pembe takım (1) mı, gri takım (2) mi? Bizimle spor yapmak isteyenleri görelim! 💪👇',
        "tags": '#evdespor #yoga #kuzen #fit #yalınayak #motivasyon #canantuna'
    },
    {
        "id": 'kuzen_burcu_pilates_ayna',
        "category": 'spor',
        "type": 'photo',
        "bold": True,
        "hook": 'Kuzenim Burcu ile antrenman bitti! Enerjimiz nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cousin_gym_mirror.jpg'),
        "signatures": ['kuzenim burcu ile sabah pilatesini tamamladık', 'beraber spor yapınca motivasyon ikiye katlanıyor'],
        "caption": 'Kuzenim Burcu ile sabah pilatesini tamamladık! 💪🔥 Beraber spor yapınca motivasyon ikiye katlanıyor. Bordo takım (Canan) mı, lacivert takım (Burcu) mu? Hangimizin spor tarzı daha iyi? 😉👇',
        "tags": '#pilates #spor #kuzen #motivasyon #fit #canantuna #gym'
    },
    {
        "id": 'oje_kirmizi_koltuk_bakim',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Yeni sürdüm, kırmızı ojem nasıl olmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_red_polish_couch.jpg'),
        "signatures": ['kırmızı ojemi yeni sürdüm', 'ayak bakımımı bitirdim nasıl olmuş'],
        "caption": 'Kırmızı ojemi yeni sürdüm, kurumalarını beklerken koltuğa kıvrıldım... 💅❤️ Bakımlı olmak her kadının kendine borcu bence! Sence kırmızı oje mi daha çekici yoksa başka renk mi? Yorumlarda puanını bekliyorum tatlım 😉👇',
        "tags": '#oje #pedikür #kırmızıoje #bakım #evhali #çekicilik #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_kiraz_kirmizi_yesil_koltuk',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Son katı sürüyorum, ojem nasıl olmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_cherry_polish_sofa.jpg'),
        "signatures": ['kiraz kırmızısı ojemi sürerken', 'son katı da sürdüm mü tamamdır'],
        "caption": 'Kiraz kırmızısı ojemi sürerken yakalandım! 🍒💅 Son katı da sürdüm mü bakımım tamamdır. Beyaz kombinimle kırmızı ojenin uyumunu nasıl buldun? 10 üzerinden puanla bakalım! 🔥👇',
        "tags": '#ojekeyfi #bakımlıkadın #kırmızı #evşıklığı #güzellik #canantuna #reels'
    },
    {
        "id": 'oje_beyaz_pedikur_yatak',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Beyaz oje yakışmış mı? Puanın kaç?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_white_pedicure_bed.jpg'),
        "signatures": ['beyaz oje kadar temiz ve şık', 'pedikürüm bitti, beyaz ojelerimle'],
        "caption": 'Pedikürüm bitti, beyaz ojelerimle yatağımda dinlenme moduna geçtim... 🤍💅 Beyaz oje kadar zarif ve dikkat çekici bir detay yok bence. Sen beyaz ojeyi beğeniyor musun yoksa koyu tonlar mı favorin? ✨👇',
        "tags": '#beyazoje #pedikür #ipekşort #yatakkeyfi #bakım #canantuna #reels #lifestyle'
    },
    {
        "id": 'oje_bordo_pelus_hali',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Bordo ojem bitti, sence nasıl görünüyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_burgundy_polish_rug.jpg'),
        "signatures": ['yumuşacık halının üstünde bordo oje', 'bordo ojelerimi sürüp dinlenmeye'],
        "caption": 'Yumuşacık halının üstünde bordo ojelerimi sürüp dinlenmeye çekildim... 🍷💅 Bordo tonunun tenime çok yakıştığını söylüyorlar, sence de öyle mi? Gözün hangi karede kaldıysa yoruma yaz bakalım 😉👇',
        "tags": '#bordooje #halıkeyfi #evmodu #bakımzamanı #fitgirl #canantuna #reels'
    },
    {
        "id": 'oje_pembe_balkon_uzanma',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Pembe ojem ve balkon keyfim, nasılım?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_pink_polish_balcony.jpg'),
        "signatures": ['balkonda ayakları uzatıp pembe oje', 'toz pembe ojelerim güneşte'],
        "caption": 'Balkonda ayakları uzatıp güneşin tadını çıkarma saati! 🌸💅 Toz pembe ojelerimi yeni bitirdim, şişesi bile hala elimde. Pembe tonlarını sevenler kalpleri bıraksın, bakalım kaç kişiyiz? 💕👇',
        "tags": '#pembeoje #balkonkeyfi #güneş #yazmodu #pedikür #canantuna #reels'
    },
    {
        "id": 'oje_siyah_mini_elbise_puf',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Siyah elbise ve siyah oje uyumu nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_black_polish_mirror.jpg'),
        "signatures": ['siyah mini elbisem ve parlak siyah oje', 'siyah ojenin verdiği o iddialı'],
        "caption": 'Siyah mini elbisem ve parlak siyah ojelerimle geceye hazırım! 🖤💅 Siyah ojenin verdiği o iddialı ve çekici havayı tek geçerim. Sence siyah oje mi yoksa klasik kırmızı mı kazanır? 👇🔥',
        "tags": '#siyahoje #minielbise #gecehazırlığı #iddialı #tarz #canantuna #reels'
    },
    {
        "id": 'oje_mercan_havuz_kenari',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Havuz başında ojemizi de tazeledik!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_coral_polish_pool.jpg'),
        "signatures": ['havuz kenarında mercan rengi oje', 'suya girmeden önce ojelerimi'],
        "caption": 'Havuz kenarında güneşlenirken mercan rengi ojelerimi de tazeledim! 🧡🌊 Bronz tende canlı renk ojelerin duruşuna bayılıyorum. Tatilde bile bakımından ödün vermeyenler burada mı? ✨👇',
        "tags": '#havuzbaşı #yazbakımı #oje #tatilkeyfi #beachvibes #canantuna #reels'
    },
    {
        "id": 'oje_french_pedikur_pencere_kahve',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'French pedikür mü düz renk mi? Seç bakalım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_french_pedi_morning.jpg'),
        "signatures": ['pencere önünde sabah kahvem ve french', 'klasik french pedikürden vazgeçemeyen'],
        "caption": 'Pencere önünde sabah kahvem, ipek sabahlığım ve tertemiz French pedikürüm... ☕🤍 Klasik French bakımdan vazgeçemeyen bir tek ben miyim? Doğal ve bakımlı görünümü sevenler yoruma gelsin! 🌸👇',
        "tags": '#frenchpedicure #sabahkahvesi #ipeksabahlık #zarafet #bakım #canantuna #reels'
    },
    {
        "id": 'oje_murdum_makyaj_aynasi_minder',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Mürdüm rengi ojem nasıl olmuş tatlım?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_plum_polish_vanity.jpg'),
        "signatures": ['ayna karşısında minderime oturdum, mürdüm', 'mürdüm rengi ojemi yeni sürdüm'],
        "caption": 'Ayna karşısında minderime oturdum, mürdüm rengi ojemi yeni sürdüm! 💜💅 İpek şort takımım ve yeni ojelerimle evde bakım gecesi yapıyorum. Mürdüm rengi sence nasıl durmuş? 😉👇',
        "tags": '#mürdümoje #bakımgecesi #evşıklığı #güzelliksırları #canantuna #reels'
    },
    {
        "id": 'oje_nude_sezlong_plaj',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Plajda bile ojemiz eksik olmaz, nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_nude_pedi_sunbed.jpg'),
        "signatures": ['şezlongda uzanırken nude pembe oje', 'turkuaz kombinim ve bakımlı'],
        "caption": "Şezlongda uzanırken nude-pembe ojelerimle güneşin keyfini çıkarıyorum... 🏖️💅 Turkuaz plaj kombinim ve bakımlı ayaklarımla yaz enerjisi tam gaz! Bu kareye 1'den 10'a kadar kaç puan verirsin? ☀️👇",
        "tags": '#plajşıklığı #sezlong #pedikür #yazgüneşi #tatil #canantuna #reels'
    },
    {
        "id": 'oje_kirmizi_bornoz_spa_banyo',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Duş sonrası kırmızı oje keyfi, beğendin mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_red_toes_bathrobe.jpg'),
        "signatures": ['banyo sonrası ipek bornozumla kırmızı oje', 'duş sonrası kendime bakım saati'],
        "caption": 'Banyo sonrası ipek bornozumla kendime bakım saati ayırdım... 🛁❤️ Parlak kırmızı ojemi sürdüm, şimdi keyif zamanı! Kadında en çok dikkat ettiğiniz bakım detayı ne? Doğruyu söyleyin bakalım 😉👇',
        "tags": '#spakeyfi #bornoz #kırmızıoje #bakımrutini #çekicilik #canantuna #reels'
    },
    {
        "id": 'oje_lila_yatak_ustunde',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Lila takımım ve lila ojem uyumlu mu?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_lilac_polish_mattress.jpg'),
        "signatures": ['lila ev takımım ve birebir aynı tonda lila oje', 'renk uyumuna takıntılı olanlar'],
        "caption": 'Lila ev takımım ve birebir aynı tonda sürdüğüm lila ojelerim! 💜💅 Renk uyumuna bu kadar dikkat eden bir tek ben olamam değil mi? Yeni ojelerim nasıl olmuş, yorumları görelim! ✨👇',
        "tags": '#lilaoje #renkuyumu #evkombin #tatlılık #bakım #canantuna #reels'
    },
    {
        "id": 'oje_yat_guvertesi_ciplak_ayak',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Gün batımı, tekne ve kırmızı oje... Puanın?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_barefoot_wooden_deck.jpg'),
        "signatures": ['yat güvertesinde çıplak ayak gün batımı', 'saks mavisi mayom ve kırmızı ojelerim'],
        "caption": 'Yat güvertesinde ayakları uzatıp gün batımını izlemek gibisi yok... 🛥️🌅 Saks mavisi mayom ve kırmızı ojelerimle denizin ortasında huzuru buldum. Yanımda olsaydın ne konuşurduk? 😉👇',
        "tags": '#yatturu #günbatımı #kırmızıoje #mavi #denizkeyfi #canantuna #reels'
    },
    {
        "id": 'oje_altin_halhal_deri_koltuk',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Halhal ve kırmızı oje ikilisi nasıl durmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_gold_anklet_couch.jpg'),
        "signatures": ['altın halhalım ve yeni sürdüğüm kırmızı oje', 'bordo saten elbisemle halhal'],
        "caption": 'Bordo saten elbisem, ince altın halhalım ve yeni sürdüğüm kırmızı ojelerim... ✨👠 Halhal detayını kadında çekici bulanlar kimler? Bu akşamki ev şıklığıma puanınızı bekliyorum aşklar! ❤️👇',
        "tags": '#halhal #satenelbise #kırmızıoje #zarafet #çekici #canantuna #reels'
    },
    {
        "id": 'oje_gul_kurusu_hali_uzanma',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Halıya uzandım dinleniyorum, nasılım?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_rose_polish_carpet.jpg'),
        "signatures": ['halıya yüzüstü uzanıp dinlenme', 'gül kurusu ojelerim ve rahat şortum'],
        "caption": 'Yorucu bir günün ardından yumuşacık halıya yüzüstü uzanıp dinlenme vakti! 🌸✨ Gül kurusu ojelerim ve rahat ev şortumla günün stresini atıyorum. Senin günün nasıl geçti bakalım? 😉👇',
        "tags": '#evkeyfi #halı #dinlenme #pembeoje #doğallık #canantuna #reels'
    },
    {
        "id": 'oje_sarap_kirmizisi_berjer_koltuk',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Şarap rengi ojem bitti, olmuş mu?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_wine_polish_chair.jpg'),
        "signatures": ['ipek gömleğim ve şarap kırmızısı oje', 'koltuğuma çekildim ojelerimin kurumasını'],
        "caption": 'İpek gömleğim ve yeni sürdüğüm şarap kırmızısı ojelerim... 🍷💅 Koltuğuma çekildim, ojelerimin kurumasını beklerken mesajlarınızı okuyorum! En sevdiğin oje rengini yoruma yaz, bir sonrakine onu süreyim 😉👇',
        "tags": '#şarapkırmızısı #oje #ipekgömlek #evhali #sohbet #canantuna #reels'
    },
    {
        "id": 'cesur_kirmizi_bikini_sonsuzluk_havuzu',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Kırmızı bikinimle yaz enerjisi! Puanın kaç?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_red_bikini_pool.jpg'),
        "signatures": ['yakut kırmızısı bikinim ve sonsuzluk havuzu'],
        "caption": 'Yakut kırmızısı bikinim ve sonsuzluk havuzunda batan güneş... ❤️🌊 Suyun verdiği tazelik ve kırmızı enerjisi bir başka oluyor. Kırmızı rengin bende duruşuna kaç puan verirsin? 🔥👇',
        "tags": '#kırmızıbikini #havuz #günbatımı #fitbody #tatil #canantuna #reels'
    },
    {
        "id": 'cesur_siyah_dantelli_saten_yatak',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Siyah ipek ve dantel uyumu nasıl olmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_lace_cami_bed.jpg'),
        "signatures": ['siyah dantel detaylı ipek takımım', 'gece lambasının loş ışığında'],
        "caption": 'Gece lambasının loş ışığında siyah dantel detaylı ipek takımım... 🖤✨ Evde kendimi şık ve çekici hissetmeyi çok seviyorum. İyi geceler mesajımı buraya bırakıyorum, kimler uyanık? 😉🌙👇',
        "tags": '#siyahipek #geceşıklığı #iyigeceler #evhali #zarafet #canantuna #reels'
    },
    {
        "id": 'cesur_zumrut_yirtmacli_gece_elbisesi',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Derin yırtmaçlı zümrüt elbisem nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_emerald_plunge_dress.jpg'),
        "signatures": ['zümrüt yeşili derin yırtmaçlı elbisem', 'mermer barda geceye başlangıç'],
        "caption": 'Zümrüt yeşili derin yırtmaçlı elbisemle geceye iddialı bir başlangıç! 💚🥂 Hem bacak dekoltesi hem de zümrüt tonu bir araya gelince gözler üzerimizde. Bu kombinle nereye gidilir? 😉👇',
        "tags": '#zümrütyeşili #yırtmaçlıelbise #gecehayatı #şıklık #çekici #canantuna #reels'
    },
    {
        "id": 'cesur_beyaz_bikini_yat_guneslenme',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Teknede beyaz bikini şıklığı! Beğendin mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_white_bikini_yacht.jpg'),
        "signatures": ['teknede beyaz bikinimle güneşlenirken'],
        "caption": 'Teknede beyaz bikinimle güneşlenirken masmavi koyların tadını çıkarıyorum... 🛥️🤍 Bronz tende beyaz bikininin yeri her zaman ayrıdır. Deniz tatilini özleyenler burada mı? 🌊👇',
        "tags": '#beyazbikini #yatturu #bronz #deniz #yaz #canantuna #reels'
    },
    {
        "id": 'cesur_pembe_korse_mini_etek_ayna',
        "category": 'sokak',
        "type": 'video',
        "bold": True,
        "hook": 'Pembe korse ve mini etek kombinim nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_pink_corset_mirror.jpg'),
        "signatures": ['fuşya korse büstiyerim ve beyaz mini eteğim'],
        "caption": 'Fuşya korse büstiyerim ve beyaz mini eteğimle çıkmadan önce son ayna kontrolü! 💖🪞 Korse kesim kıyafetlerin beli incecik göstermesine bayılıyorum. Kombinim geçer not aldı mı? 🔥👇',
        "tags": '#korse #minietek #mirrorselfie #pembe #kombin #canantuna #reels'
    },
    {
        "id": 'cesur_leopar_mayo_beach_cabana',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Leopar desen bana yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_leopard_swimsuit_beach.jpg'),
        "signatures": ['leopar desenli mayom ve gün batımı loca'],
        "caption": 'Plaj locasında gün batımı ve iddialı leopar desenli mayom... 🐆🌅 Leopar deseni taşıması zordur derler ama ben enerjisine bayıldım! Sence nasıl durmuş tatlım? 😉👇',
        "tags": '#leopar #beachclub #loca #günbatımı #yazstili #canantuna #reels'
    },
    {
        "id": 'cesur_bordo_saten_gecelik_pencere',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Bordo saten ve şehir ışıkları... Nasılım?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_burgundy_satin_slip.jpg'),
        "signatures": ['ince askılı bordo saten elbisemle cam kenarında'],
        "caption": 'İnce askılı bordo saten elbisemle cam kenarında İstanbul ışıklarını izliyorum... 🍷🌃 Gece ilerledikçe şehrin büyüsü bambaşka oluyor. Bu saatte uyanık olanlara selam olsun! ✨👇',
        "tags": '#bordosaten #gece #istanbul #penthouse #zarafet #canantuna #reels'
    },
    {
        "id": 'cesur_mavi_spor_takim_kalca_ayna',
        "category": 'spor',
        "type": 'video',
        "bold": True,
        "hook": 'Squat antrenmanı bitti, formum nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_blue_gym_booty_pose.jpg'),
        "signatures": ['elektrik mavisi spor takımım ve bacak günü'],
        "caption": 'Elektrik mavisi spor takımım ve yoğun bir bacak-kalça antrenmanı sonrası! 💙🍑 Spor salonunda dökülen her ter damlası formumu korumaya değiyor. Spora devam mı, motivasyonunuz nasıl? 💪🔥👇',
        "tags": '#squat #legday #gymgirl #fitbody #spor #canantuna #reels'
    },
    {
        "id": 'cesur_altin_bikini_jakuzi_spa',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Sıcak jakuzi ve altın ışıltısı... Puanın?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_gold_chain_bikini_spa.jpg'),
        "signatures": ['altın zincir detaylı bikinimle sıcak spa havuzu'],
        "caption": 'Altın zincir detaylı bikinimle sıcak spa havuzunda yorgunluk atıyorum... ✨🧖\u200d♀️ Sıcak su ve loş ışık bütün haftanın stresini sildi. Kendini şımartmayı sevenler burada mı? 💛👇',
        "tags": '#spa #jakuzi #altınbikini #lüks #dinlenme #canantuna #reels'
    },
    {
        "id": 'cesur_beyaz_gomlek_mutfak_sabah',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Sabah kahvesini beraber içelim mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_white_shirt_unbuttoned.jpg'),
        "signatures": ['salaş beyaz gömleğim ve sabah kahvem mutfak'],
        "caption": 'Sabah mutfakta salaş beyaz gömleğim ve dantelli büstiyerimle ilk kahvemi hazırladım... ☕🤍 Evde böyle rahat takılmayı çok seviyorum. Kahveyi sade mi içersin yoksa sütlü mü? 😉👇',
        "tags": '#günaydın #beyazgömlek #mutfak #sabahkahvesi #evhali #canantuna #reels'
    },
    {
        "id": 'cesur_mor_ipek_sabahlik_makyaj',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Hazırlanırken yakalandık, mor yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_purple_silk_robe.jpg'),
        "signatures": ['lila-mor ipek sabahlığım ve dudak parlatıcım'],
        "caption": 'Lila-mor ipek sabahlığım ve makyaj masamda son dokunuşlar... 💜💄 Hazırlanırken geçen o tatlı telaşı bile seviyorum. Mor tonları tenime uymuş mu aşklar? ✨👇',
        "tags": '#ipeksabahlık #makyaj #vanity #güzellik #mor #canantuna #reels'
    },
    {
        "id": 'cesur_siyah_dekolteli_mini_gece',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Geceye siyah mini elbiseyle çıktık, nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_cutout_club.jpg'),
        "signatures": ['bel dekolteli siyah mini elbisemle terasta'],
        "caption": 'Bel ve göğüs dekolteli siyah mini elbisemle terasta gece havası! 🖤🔥 Siyahın en cesur ve en şık halini üzerimde taşımayı seviyorum. Bu kombine 10 üzerinden kaç veriyorsun? 👇',
        "tags": '#siyahmini #dekolte #gecehayatı #rooftop #tarz #canantuna #reels'
    },
    {
        "id": 'cesur_turkuaz_plaj_dus_gunes',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Deniz sonrası serinleme anı! Enerji nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_turquoise_bikini_shower.jpg'),
        "signatures": ['denizden çıkınca ahşap plaj duşunda'],
        "caption": 'Denizden çıkınca güneşin altında serinleme molası... 🩵☀️ Turkuaz rengin bronz tenle uyumuna doyum olmuyor. Yaz tatilini dört gözle bekleyenler el kaldırsın! 🌊👇',
        "tags": '#turkuaz #plaj #yazmodası #güneş #beachclub #canantuna #reels'
    },
    {
        "id": 'cesur_kirmizi_omzu_acik_deri_koltuk',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Kırmızı mini elbise mi siyah mı? Seç bakalım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_red_satin_couch.jpg'),
        "signatures": ['omzu açık ateş kırmızısı mini elbisemle koltukta'],
        "caption": 'Omzu açık ateş kırmızısı mini elbisemle deri koltukta akşam pozu... ❤️🔥 Uzun bacaklar ve kırmızı bir araya gelince başka söze gerek kalmıyor. Bakışları yakaladık mı? 😉👇',
        "tags": '#kırmızımini #uzunbacak #çekicilik #akşamşıklığı #canantuna #reels'
    },
    {
        "id": 'cesur_gri_sort_beyaz_crop_parke',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Evde spor şort rahatlığı, nasıl görünüyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_grey_shorts_floor.jpg'),
        "signatures": ['beyaz crop atletim ve gri mini şortumla'],
        "caption": 'Beyaz crop atletim ve gri mini şortumla evde en doğal halim... 🤍✨ Bazen en sade kombinler bile fiziği en güzel şekilde ortaya çıkarıyor. Doğal ev halimi beğendin mi? 👇',
        "tags": '#evhali #minişort #croptop #doğalgüzellik #fit #canantuna #reels'
    },
    {
        "id": 'cesur_sampanya_sirt_dekolteli_balkon',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Sırt dekoltesi mi ön dekolte mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_champagne_backless.jpg'),
        "signatures": ['sırt dekolteli şampanya saten elbisemle'],
        "caption": 'Sırt dekolteli şampanya saten elbisemle alacakaranlıkta balkon sefası... 🥂✨ Zarif bir sırt dekoltesi her zaman çok asil ve çekici duruyor bence. Sen ne düşünüyorsun tatlım? 😉👇',
        "tags": '#sırtdekoltesi #şampanyasaten #zarafet #geceelbisesi #canantuna #reels'
    },
    {
        "id": 'cesur_mercan_bikini_havuz_bar',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Mercan rengi plaj kombinim kaç puan alır?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_neon_coral_bikini.jpg'),
        "signatures": ['mercan rengi plaj takımım ve soğuk kokteylim'],
        "caption": 'Havuz barında mercan rengi plaj takımım ve buz gibi içeceğim... 🍹🧡 Canlı renkler enerjimi anında ikiye katlıyor! Benimle karşılıklı bir şeyler içmeye var mısın? 😉👇',
        "tags": '#mercan #havuzbarı #tatilenerjisi #yaz #kokteyl #canantuna #reels'
    },
    {
        "id": 'cesur_siyah_deri_korse_araba',
        "category": 'sokak',
        "type": 'video',
        "bold": True,
        "hook": "Deri korse ve araba selfie'si! Yan koltuk boş!",
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_leather_corset_car.jpg'),
        "signatures": ['siyah deri korse büstiyerimle direksiyon başında'],
        "caption": 'Siyah deri korse büstiyerimle direksiyon başında güneşli bir tur! 🚗🖤 Deri korsenin verdiği o asi ve çekici havayı çok seviyorum. Yan koltuk boş, nereye sürüyoruz? 😉🔥👇',
        "tags": '#derikorse #carselfie #araba #tarz #çekici #canantuna #reels'
    },
    {
        "id": 'cesur_yesil_kadife_straplez_somine',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Şömine başında straplez kadife şıklığı!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_green_velvet_mini.jpg'),
        "signatures": ['straplez zümrüt kadife mini elbisem ve şömine'],
        "caption": 'Şömine ateşi önünde straplez yeşil kadife mini elbisem... 🔥💚 Dışarısı soğuk olabilir ama içerisi fazlasıyla sıcak! Straplez kesim bana yakışmış mı canlar? 👇',
        "tags": '#straplez #kadifeelbise #şömine #kışgecesi #zarafet #canantuna #reels'
    },
    {
        "id": 'cesur_seftali_yoga_esneklik_gunbatimi',
        "category": 'spor',
        "type": 'video',
        "bold": True,
        "hook": 'Esneklik ve form bir arada! Nasıl görünüyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_peach_yoga_arch.jpg'),
        "signatures": ['şeftali tonu spor takımım ve gün batımı esneme'],
        "caption": 'Gün batımı ışığında şeftali tonu spor takımımla esneklik çalışması... 🍑🧘\u200d♀️ Vücudun esnek ve sıkı kalması için her gün düzenli hareket şart! Spor yapanları görelim bakalım 💪👇',
        "tags": '#yoga #esneklik #fitgirl #şeftalitonu #spor #canantuna #reels'
    },
    {
        "id": 'cesur_kobalt_mavi_mini_merdiven',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Kobalt mavi mini elbisemle geceye hazırım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_cobalt_mini_stairs.jpg'),
        "signatures": ['kobalt mavisi büzgülü mini elbisem mermer merdiven'],
        "caption": 'Mermer merdivenlerde kobalt mavisi büzgülü mini elbisem ve topuklularım... 💙👠 Vücudu saran kesimler ve canlı mavi tonu gece davetlerinde favorim! Kombinime puanın kaç? ✨👇',
        "tags": '#kobaltmavi #minielbise #topukluayakkabı #geceşıklığı #canantuna #reels'
    },
    {
        "id": 'cesur_siyah_bikini_deniz_hamak',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Denizin üstünde hamak keyfi! Gelmek ister misin?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_bikini_hammock.jpg'),
        "signatures": ['turkuaz suyun üzerindeki file hamakta siyah bikini'],
        "caption": 'Turkuaz suyun üzerindeki file hamakta altın halkalı siyah bikinimle huzur... 🖤🌊 Altımda berrak deniz, üstümde sıcacık güneş! Buraya kiminle gelmek isterdin? 😉👇',
        "tags": '#siyahbikini #hamak #turkuazdeniz #tatil #yaz #canantuna #reels'
    },
    {
        "id": 'cesur_beyaz_dantelli_korse_balkon',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Beyaz dantel korse ve deniz manzarası!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_white_corset_balcony.jpg'),
        "signatures": ['beyaz dantel korse büstiyerim ve ipek mini etek'],
        "caption": 'Begonvilli taş balkonda beyaz dantel korse büstiyerim ve ipek mini eteğim... 🤍🌺 Hem romantik hem de oldukça çekici bir yaz kombini oldu. Beyaz dantel detayını sevdin mi? 👇',
        "tags": '#beyazkorse #dantel #ipeketek #akdeniz #yazşıklığı #canantuna #reels'
    },
    {
        "id": 'cesur_sarap_fermuarli_spor_ayna',
        "category": 'spor',
        "type": 'video',
        "bold": True,
        "hook": 'Evde spor bitti, ayna pozumuz eksik olmasın!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_wine_gym_squat_mirror.jpg'),
        "signatures": ['fermuarlı şarap rengi spor büstiyerim ve tayt şort'],
        "caption": 'Fermuarlı şarap rengi spor büstiyerim ve kısa tayt şortumla ev antrenmanı tamam! 🍷💪 Evde spor yaparken bile şıklığımdan ödün vermem. Bugünkü formumu nasıl buldun? 🔥👇',
        "tags": '#evsporu #bikershorts #fitbody #aynaselfie #motivasyon #canantuna #reels'
    },
    {
        "id": 'cesur_gumus_metalik_mini_parti',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Gümüş ışıltılı mini elbisemle göz kamaştıralım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_silver_chainmail_party.jpg'),
        "signatures": ['gümüş metalik boyundan bağlamalı mini elbisem'],
        "caption": 'Gümüş metalik boyundan bağlamalı mini elbisemle gece kulübünde tüm bakışları topladık! 🪩✨ Parlamayı ve iddialı seçimler yapmayı seviyorum. Gümüş mü altın mı sana göre? 🥂👇',
        "tags": '#gümüşelbise #partistili #gecehayatı #ışıltı #minielbise #canantuna #reels'
    },
    {
        "id": 'cesur_sari_bikini_sezlong_bakis',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Sarı bikinim güneşten daha parlak değil mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_yellow_bikini_sunbed.jpg'),
        "signatures": ['güneş sarısı bikinimle şezlongda uzanırken'],
        "caption": 'Güneş sarısı bikinimle şezlongda uzanırken omzumun üzerinden küçük bir tebessüm... 💛☀️ Sarı renk bronz tende bir başka parlıyor! Bakışımı yakalayanlar yoruma kalp bıraksın 😉👇',
        "tags": '#sarıbikini #plaj #güneşlenme #summervibes #çekici #canantuna #reels'
    },
    {
        "id": 'cesur_moka_dar_elbise_asansor_selfie',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Asansör aynasında tam boy kontrol! Nasılım?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_mocha_bodycon_elevator.jpg'),
        "signatures": ['moka kahve vücudu saran elbisemle asansör'],
        "caption": "Otel asansöründe moka kahve vücudu saran elbisemle klasik ayna selfie'si! 🤎🪞 Vücut hatlarını saran triko elbiseler her zaman kurtarıcım. Bu elbiseye 10 üzerinden kaç verirsin? 🔥👇",
        "tags": '#bodycondress #asansörselfie #kahverengi #kıvrımlar #şıklık #canantuna #reels'
    },
    {
        "id": 'cesur_roze_saten_kuvet_mum_isigi',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Mum ışığı, gül yaprakları ve saten... Romantik mi?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_rose_satin_bath.jpg'),
        "signatures": ['gül yapraklarıyla dolu küvet kenarında roze saten'],
        "caption": 'Mum ışığında, gül yapraklarıyla dolu mermer küvet kenarında roze saten elbisemle... 🌹🕯️ Kendime hazırladığım en romantik ve huzurlu akşam! Böyle bir atmosferi kim sevmez ki? 💕👇',
        "tags": '#mumışığı #rozesaten #romantik #lüksbanyo #zarafet #canantuna #reels'
    },
    {
        "id": 'cesur_kot_sort_beyaz_crop_iskele',
        "category": 'sokak',
        "type": 'video',
        "bold": True,
        "hook": 'Kot şort ve beyaz crop klasiği! Yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_denim_shorts_crop.jpg'),
        "signatures": ['düğümlü beyaz crop bluzum ve yüksek bel kot şortum'],
        "caption": 'Sahil iskelesinde düğümlü beyaz crop bluzum ve yüksek bel kot şortumla altın saatler... 🌅👖 Hem rahat hem de bacak boyunu ortaya çıkaran en sevdiğim yaz kombini! Beğendin mi tatlım? 😉👇',
        "tags": '#kotşort #croptop #sahil #günbatımı #yazstili #canantuna #reels'
    },
    {
        "id": 'cesur_yakut_halter_Bogaz_teras',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Boğaz manzarası mı ben mi? Doğruyu söyle!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_ruby_halter_rooftop.jpg'),
        "signatures": ['göğüs pencereli yakut kırmızısı halter elbisemle'],
        "caption": 'Boğaz terasında göğüs pencereli yakut kırmızısı halter elbisemle akşam sefası... ❤️🌉 Arkamda İstanbul, üzerimde en sevdiğim kırmızı tonu! Gözün manzarada mı kaldı yoksa bende mi? 😉👇',
        "tags": '#boğaz #kırmızıelbise #rooftop #istanbulgeceleri #çekicilik #canantuna #reels'
    },
    {
        "id": 'cesur_lila_bikini_havuz_merdiveni',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Havuzdan çıkarken yakalandık! Lila nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_lilac_bikini_pool_steps.jpg'),
        "signatures": ['havuz merdivenlerinde pastel lila mayo-bikinim'],
        "caption": 'Havuz merdivenlerinde pastel lila kesimli bikinim ve güneşin ışıltısı... 💜💦 Suyun içinden çıkarken yakalanan en doğal ve çekici kare! Lila rengi plajda nasıl durmuş? ✨👇',
        "tags": '#lilabikini #havuzkeyfi #su #yaz #fitgirl #canantuna #reels'
    },
    {
        "id": 'cesur_siyah_tul_korse_mum_yemek',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Karşımdaki sandalye boş, yemeğe eşlik eder misin?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_mesh_night.jpg'),
        "signatures": ['tül kollu siyah büstiyer elbisemle mum ışığında'],
        "caption": 'Tül kollu siyah büstiyer elbisemle mum ışığında özel bir akşam yemeği... 🖤🍷 Karşımdaki sandalye senin için ayrılmış olsaydı bana ilk ne söylerdin? Yorumlarda buluşalım 😉👇',
        "tags": '#akşamyemeği #siyahbüstiyer #romantik #geceşıklığı #canantuna #reels'
    },
    {
        "id": 'cesur_krem_fitilli_sort_takim_hali',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Krem rengi ev takımım nasıl olmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_cream_ribbed_set_rug.jpg'),
        "signatures": ['krem rengi fitilli büstiyer ve mini şort takımım'],
        "caption": 'Krem rengi fitilli büstiyer ve mini şort takımımla pofuduk halı üzerinde akşam keyfi... 🤍✨ Evde hem rahat hem de bakımlı olmayı sevenlerdenim. Bu ev kombinime kaç puan verirsin? 👇',
        "tags": '#evkombin #kremrengi #minişort #huzur #cozy #canantuna #reels'
    },
    {
        "id": 'cesur_zumrut_bikini_altin_zincir_palmiye',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Zümrüt yeşili ve altın zincir detayı nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_emerald_bikini_palm.jpg'),
        "signatures": ['palmiye ağacına yaslanmış zümrüt yeşili mayo'],
        "caption": 'Palmiye gölgesinde zümrüt yeşili plaj şıklığım ve belimdeki altın zincir detayı... 💚🌴 Yeşilin en asil tonu güneşle buluşunca harika bir enerji ortaya çıktı. Beğenenler kalp bıraksın! ✨👇',
        "tags": '#zümrütyeşili #palmiye #plajmodası #altınzincir #tatil #canantuna #reels'
    },
    {
        "id": 'cesur_fusya_mini_elbise_yatak_odasi_ayna',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Fuşya mini elbisemle enerjim tavan! Puanın?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_fuchsia_mini_mirror.jpg'),
        "signatures": ['fuşya pembe omzu açık mini elbisemle boy aynası'],
        "caption": 'Fuşya pembe omzu açık mini elbisemle yatak odası boy aynasında son poz! 💗🪞 Canlı pembe tonları içimdeki neşeyi ve enerjiyi dışarı yansıtıyor. Bu elbiseyle dışarı çıkılır mı? 😉👇',
        "tags": '#fuşya #minielbise #boyaynası #selfie #enerji #canantuna #reels'
    },
    {
        "id": 'cesur_bronz_saten_kruvaze_mini_teras',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Bronz saten mini elbisem güneşte nasıl parlıyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_bronze_satin_sunset.jpg'),
        "signatures": ['bronz saten kruvaze mini elbisemle gün batımı teras'],
        "caption": 'Deniz manzaralı terasta bronz saten kruvaze mini elbisem ve rüzgarın tatlı esintisi... 🌅🤎 Saten kumaşın gün batımı ışığındaki ışıltısına bayılıyorum. Favori rengin hangisi? ✨👇',
        "tags": '#bronzsaten #kruvazeelbise #günbatımı #teras #zarafet #canantuna #reels'
    },
    {
        "id": 'cesur_lacivert_mini_tenis_etek_kort',
        "category": 'spor',
        "type": 'video',
        "bold": True,
        "hook": 'Tenis kortunda mini etek şıklığı! Maça var mısın?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_navy_tennis_mini.jpg'),
        "signatures": ['lacivert spor büstiyerim ve beyaz pileli mini tenis'],
        "caption": 'Güneşli kortta lacivert spor büstiyerim ve beyaz pileli mini tenis eteğimle maça hazırım! 🎾💙 Tenis kıyafetlerinin hem sportif hem de bu kadar çekici olmasına bayılıyorum. Rakibim olur musun? 😉👇',
        "tags": '#tenis #minietek #kortşıklığı #sportif #fitgirl #canantuna #reels'
    },
    {
        "id": 'cesur_murdum_ipek_gecelik_balkon_kapi',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Sabah kahvesi ve ipek rahatlığı... Günaydın!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_plum_velvet_robe_morning.jpg'),
        "signatures": ['mürdüm rengi ipek geceliğimle balkon kapısında'],
        "caption": 'Sabah güneşinde mürdüm rengi ipek geceliğimle balkon kapısında espresso keyfi... ☕💜 Güne erken ve enerjik başlayan herkese kocaman günaydın! Bugün planlarınız ne bakalım? 🌸👇',
        "tags": '#ipekgecelik #sabahgüneşi #espresso #günaydın #evhali #canantuna #reels'
    },
    {
        "id": 'cesur_beyaz_pencereli_mayo_yat_burun',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Beyaz kesimli mayomla koylardayız! Nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_white_cutout_swim_yacht.jpg'),
        "signatures": ['bel pencereli beyaz monokini mayomla yatın burnunda'],
        "caption": 'Turkuaz koylarda bel pencereli beyaz monokini mayomla güneşin tadını çıkarıyorum... 🛥️🤍 Kesimli mayolar vücut hatlarını çok zarif gösteriyor bence. Sen beğendin mi tatlım? 🌊👇',
        "tags": '#monokini #beyazmayo #yatturu #turkuaz #tatil #canantuna #reels'
    },
    {
        "id": 'cesur_cikolata_deri_mini_etek_lounge',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Deri mini etek ve büstiyer uyumu kaç puan?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_chocolate_leather_skirt.jpg'),
        "signatures": ['bej büstiyerim ve çikolata kahve deri mini eteğim'],
        "caption": 'Bej büstiyerim ve çikolata kahve deri mini eteğimle akşam buluşmasına hazırım! 🤎🔥 Deri mini etek her zaman iddialı ve vazgeçilmez bir parça. Kombinim 10 üzerinden kaç alır? 👇',
        "tags": '#derietek #minietek #kahvetonları #gecekombini #tarz #canantuna #reels'
    },
    {
        "id": 'spor_bordo_gym_ayna_selfie',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_burgundy_gym_mirror.jpg'),
        "signatures": ['bordo spor takımım', 'antrenman sonrası aynada kendime'],
        "caption": 'Bordo spor takımım ve ben bugün salonda fırtına gibi estik! 🔥💪 Emek verilen her ter damlası fiziğime fazlasıyla değiyor. Bugün spora gidenler kimler bakalım? 😉👇',
        "alt_captions": ['Antrenman sonrası aynada kendime bakınca bütün yorgunluğum uçup gidiyor... 🍷✨ Bordo bana yakışmış mı aşklar, puanınız kaç? 🔥👇'],
        "tags": '#fitness #gymgirl #bordotakım #fitbody #motivasyon #spor #canantuna #reels #mirrorselfie'
    },
    {
        "id": 'ev_beyaz_triko_koltuk_keyfi',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_white_knit_couch.jpg'),
        "signatures": ['omzu açık beyaz trikom', 'zümrüt koltuğuma kıvrıldım'],
        "caption": 'Omzu açık beyaz trikom, sıcak çayım ve evimin huzuru... 🤍🍵 Dışarıdaki koşturmacadan kaçıp zümrüt koltuğuma kıvrıldım. Yanıma bir kahve alıp sohbete gelecek var mı? 😉✨',
        "alt_captions": ['Evde rahat ama şık olmayı sevenler kulübü! 🤍✨ Beyaz triko elbisemle akşam dinlenmesine geçtim, gününüz nasıl geçti canlar? 🌸👇'],
        "tags": '#evhali #beyazelbise #triko #cozyvibes #zarafet #huzur #canantuna #lifestyle #reels'
    },
    {
        "id": 'tatil_saks_mavisi_yat_gunbatimi',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_royal_blue_yacht_sunset.jpg'),
        "signatures": ['saks mavisi ve gün batımının', 'güvertede rüzgarı dinlerken'],
        "caption": 'Saks mavisi ve gün batımının büyüleyici uyumu... 💙🌅 Güvertede hafif esen rüzgarı dinlerken zaman dursun istedim. Mavinin bu tonunu benim kadar seven var mı? ✨👇',
        "alt_captions": ['Deniz üstünde batan güneşin verdiği o tatlı huzur... 🛥️💙 Arşivden içimi ısıtan en özel karelerden biri, nasıl buldunuz? 🌅👇'],
        "tags": '#saksmavisi #günbatımı #yatturu #deniz #zarafet #summervibes #canantuna #reels'
    },
    {
        "id": 'spor_cikolata_kahve_yoga_tulum',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_chocolate_brown_pilates.jpg'),
        "signatures": ['çikolata kahve tulumumla', 'esneklik ve denge seansı'],
        "caption": 'Çikolata kahve tulumumla esneklik ve denge seansı tamamlandı! 🍫🧘\u200d♀️ Vücudumu dinlendiren ve formda tutan en güzel saatler. Spor tulumumu nasıl buldunuz tatlım? ✨👇',
        "alt_captions": ['Matın üzerinde geçen her dakika bedenime ayrı bir enerji katıyor... 🤎💪 Kahve tonları bu sezon favorim, sizce nasıl durmuş? 👇'],
        "tags": '#yoga #pilates #fitlife #kahvetonları #athleisure #esneklik #canantuna #reels'
    },
    {
        "id": 'gece_siyah_saten_penthouse_balkon',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_black_satin_penthouse.jpg'),
        "signatures": ['siyah satenin asaleti', 'penthouse terasında şehir'],
        "caption": 'Siyah satenin asaleti ve ayaklarımın altında parlayan İstanbul gecesi... 🖤🍸 Penthouse terasında hafif müzik eşliğinde geceye başladık. Bu gece planlar ne bakalım? 😉✨',
        "alt_captions": ['Geceye siyah bir imza bırakalım... 🌃🖤 Şehir ışıkları mı daha parlak yoksa enerjimiz mi? Yorumları bekliyorum aşklar 👇'],
        "tags": '#siyahsaten #geceşıklığı #istanbulgeceleri #penthouse #zarafet #canantuna #reels'
    },
    {
        "id": 'sokak_haki_crop_etiler_yuruyus',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_olive_cargo_street.jpg'),
        "signatures": ['haki ve beyazın enerjisi', 'etiler sokaklarında buzlu'],
        "caption": 'Haki ve beyazın enerjisiyle Etiler sokaklarında buzlu kahve turu! 🌿☕ Hem spor hem çekici kombinleri günlük hayatta çok seviyorum. Tarzıma 10 üzerinden kaç veriyorsunuz? 😎👇',
        "alt_captions": ['Güneşli havayı yakalayınca sokaklara taşan enerji! 🍃🕶️ Bugünkü sokak stilimi beğendiniz mi canlar? 👇'],
        "tags": '#sokakstili #etiler #bebek #kombin #streetfashion #ootd #canantuna #reels'
    },
    {
        "id": 'ev_pembe_ipek_sabah_yatak_kahvalti',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_pink_silk_morning_bed.jpg'),
        "signatures": ['pudra pembesi ipek pijamam', 'yatakta kruvasan ve latte'],
        "caption": 'Pudra pembesi ipek pijamam, yatakta taze kruvasan ve latte keyfi... 🌸🥐 Bugün kendimi biraz şımartmaya karar verdim. Bana günaydın yok mu bakalım? 😉💕',
        "alt_captions": ['Sabah güneşinin odaya vurduğu en tatlı dakikalar... 💕☕ Güne böyle huzurlu başlamak gibisi yok, hepinize öpücükler! 🌸👇'],
        "tags": '#günaydın #sabahkeyfi #ipekpijama #kahvaltı #evhali #canantuna #morningvibes #reels'
    },
    {
        "id": 'gece_altin_payet_otel_daveti',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_gold_sequin_gala.jpg'),
        "signatures": ['şampanya altını ışıltısı', 'avizelerin altında büyüleyici'],
        "caption": 'Şampanya altını ışıltısı ve özel bir davet gecesi... ✨🥂 Avizelerin altında parlamayı seviyorum. Bu elbisenin sırt detayına bayıldım, sizce nasıl olmuş? 💛👇',
        "alt_captions": ['Özel gecelerde altın tonlarının yeri bende hep ayrı... 🌟🥂 Gözlerinizi alamadığınız o kare bu olsun mu? 😉👇'],
        "tags": '#altınelbise #gala #gecedaveti #ışıltı #lüksyaşam #zarafet #canantuna #reels'
    },
    {
        "id": 'ev_lavanta_hali_uzanma_keyfi',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_lavender_rug_stretch.jpg'),
        "signatures": ['lavanta takımım ve yumuşacık halı', 'halıya uzanıp biraz mola'],
        "caption": 'Esnetme hareketlerinden sonra yumuşacık halıya uzanıp biraz mola verdim... 💜✨ Lavanta takımım hem çok rahat hem de fiziği harika sarıyor. Kimler bugün tembellik modunda? 😉👇',
        "alt_captions": ['Evde antrenman biter, halı üstünde tatlı yorgunluk başlar! 💜🙈 Gözlerimin içine bakanlara selam olsun, gününüz nasıl geçiyor? 👇'],
        "tags": '#lavanta #evsporu #fitgirl #halıkeyfi #çekicilik #motivasyon #canantuna #reels'
    },
    {
        "id": 'sokak_kirmizi_trenckot_pastane',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_red_trench_rain_paris.jpg'),
        "signatures": ['kırmızı trençkotumla sokaklarda', 'uzun çizmeler ve kırmızı'],
        "caption": 'Kırmızı trençkotum ve uzun çizmelerimle sonbahar sokaklarında dikkatleri üzerimize çekelim biraz! ❤️👢 Serin havalarda koyu kırmızı giymeye bayılıyorum. Kombinim geçer not aldı mı? 🔥👇',
        "alt_captions": ['Butik pastane önünde kısa bir kahve molası... ❤️🥐 Kırmızı trençkot enerjisi diye bir gerçek var, katılıyor musunuz? 👇'],
        "tags": '#kırmızıtrençkot #sonbaharmodası #çizmekombini #nişantaşı #tarz #canantuna #reels'
    },
    {
        "id": 'tatil_turkuaz_havuz_sezlong',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_turquoise_poolside_lounger.jpg'),
        "signatures": ['turkuaz takımım ve palmiyeler', 'şezlongda güneşin tadını'],
        "caption": 'Turkuaz takımım, palmiyeler ve suyun verdiği o eşsiz dinginlik... 🩵🌴 Şezlongda uzanıp güneşin tadını çıkardığım anları hiçbir şeye değişmem. Turkuaz rengi bana yakışmış mı? ✨👇',
        "alt_captions": ['Sıcak bir tatil molası her zaman ruhu gençleştirir... 🌊🩵 Havuz başı stilime puanınız kaç aşklar? 👇'],
        "tags": '#turkuaz #havuzbaşı #resortwear #tatilkeyfi #beachstyle #canantuna #reels'
    },
    {
        "id": 'spor_antrasit_bisiklet_sahil_park',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_charcoal_cycling_park.jpg'),
        "signatures": ['bisikletimle sahil turu', 'antrasit şort takımım'],
        "caption": 'Güneşli havada bisikletimle sahil parkuru tamamlandı! 🚲🔥 Antrasit şort takımım ve bitmeyen enerjimle harika bir turdu. Benimle sahilde pedal çevirmeye var mısın? 😉👇',
        "alt_captions": ['Açık havada spor yapmanın tadı bambaşka! 🌿🚲 Bacak antrenmanını bugün sahilde bisikletle yaptık, nasıl görünüyor? 💪👇'],
        "tags": '#bisiklet #sahilturu #bikershorts #fitlife #moda #enerji #canantuna #reels'
    },
    {
        "id": 'lifestyle_terrakota_elbise_bahce_kafe',
        "category": 'lifestyle',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_terracotta_pottery_cafe.jpg'),
        "signatures": ['tarçın rengi kruvaze elbisem', 'çiçekli bahçe kafede'],
        "caption": 'Tarçın rengi kruvaze elbisem ve çiçekler içinde huzurlu bir bahçe kafe... 🌺☕ Sıcak tonlar tenime çok uyuyor bence, siz ne dersiniz? Bir kahve ısmarlar mısınız bana? 😉🧡',
        "alt_captions": ['Begonvillerin altında buzlu latte ve tatlı bir tebessüm... 🧡🌸 Gününüz benimki kadar renkli geçsin canlar! 👇'],
        "tags": '#kruvazeelbise #bahçekafe #tarçınrengi #zarafet #kahvekeyfi #canantuna #reels'
    },
    {
        "id": 'lifestyle_lacivert_blazer_marina_yat_kulubu',
        "category": 'is',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_navy_blazer_yacht_club.jpg'),
        "signatures": ['lacivert blazer ve beyaz', 'marina yat kulübünde akşamüstü'],
        "caption": 'Marina yat kulübünde akşamüstü buluşması... ⚓💙 Lacivert blazer ve beyaz kombininin o asil duruşuna bayılıyorum. Hem klasik hem çekici olmak tam benim tarzım! ✨👇',
        "alt_captions": ['Deniz kenarında şık bir akşamüstü toplantısı... 🛥️🤍 Lacivert-beyaz uyumu sizce de her zaman kazanmıyor mu? 👇'],
        "tags": '#marina #yachtclub #blazer #oldmoney #şıklık #istanbul #canantuna #reels'
    },
    {
        "id": 'ev_mint_yesili_mutfak_detoks_smoothie',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_mint_wellness_smoothie.jpg'),
        "signatures": ['mint yeşili spor takımım', 'yeşil detoks smoothie'],
        "caption": 'Mint yeşili spor takımım ve antrenman sonrası kendi ellerimle hazırladığım detoks smoothie! 🥑💚 Formumu korumak için mutfakta da disiplin şart. Sağlıklı beslenenler burada mı? ✨👇',
        "alt_captions": ['Sabah enerjisini yeşil içeceğimden, neşemi de sizden alıyorum! 💚🥤 Mint yeşili rengi nasıl buldunuz tatlım? 👇'],
        "tags": '#smoothie #detoks #mintyeşili #sağlıklıyaşam #fitkitchen #canantuna #reels'
    },
    {
        "id": 'gece_murver_mor_elbise_giyinme_odasi',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_silver_mirror_dressing.jpg'),
        "signatures": ['mürdüm rengi kokteyl elbisem', 'giyinme odasında son dokunuşlar'],
        "caption": 'Giyinme odasında geceye hazırlanırken son dokunuşlar... 💜✨ Mürdüm rengi dar elbisem ve küpelerim hazır! Bakalım bu akşam nereye gidiyoruz, tahminleri alayım? 😉👠',
        "alt_captions": ['Ayna karşısında hazırlanmak benim için ayrı bir ritüel... 💄💜 Mürdüm tonu sizce de çok çekici değil mi? 👇'],
        "tags": '#mürdüm #kokteylelbise #giyinmeodası #grwm #gecehazırlığı #canantuna #reels'
    },
    {
        "id": 'is_gunbatimi_plaza_masasi',
        "category": 'is',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_executive_sunset_desk.jpg'),
        "signatures": ['masamda gün batımı kahvesi', 'yüksek katlardan şehri izlerken'],
        "caption": 'Ofiste masamda gün batımı kahvesi ve yeni hedefler... ☕🌆 Yüksek katlardan şehri izlerken çalışmak bana ilham veriyor. İş çıkışı planlarınız hazır mı canlar? 💼✨',
        "alt_captions": ['Hem çalışkan hem bakımlı olmak bizim doğamızda var! 💼🌸 Günün yorgunluğunu bir kahveyle atıyoruz, sizde durumlar ne? 👇'],
        "tags": '#ofisşıklığı #plaza #işkadını #günbatımı #motivasyon #canantuna #reels'
    },
    {
        "id": 'hobi_seramik_atolyesi_heykel',
        "category": 'sanat',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_ceramics_studio.jpg'),
        "signatures": ['ellerim çamurlu ama ruhum', 'seramik atölyesi molası'],
        "caption": 'Ellerim çamurlu ama ruhum kuş gibi hafif... 🏺✨ Bugün kendime harika bir seramik atölyesi molası verdim. Kendi ellerinle çamura şekil vermek, sıfırdan bir şey yaratmak o kadar dinlendirici bir terapi ki! Siz en son kendiniz için ne zaman yeni bir şey denediniz? 🤍🌿',
        "tags": '#seramik #çömlek #atölye #hobi #sanat #ceramics #mindfulness #lifestyle #canantuna #reels'
    },
    {
        "id": 'kis_uludag_dag_evi_kar',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_uludag_winter.jpg'),
        "signatures": ["uludağ'da ilk kar keyfi", 'fincan sıcak çikolata gibisi yok'],
        "caption": "Uludağ'da ilk kar keyfi! ❄️☕ Beyazlar içinde sıcacık bir fincan sıcak çikolata gibisi yok... Dışarısı buz gibi ama ruhuma öyle iyi geldi ki anlatamam. Kış mevsimini ve kar tatilini sevenler kalpleri bıraksın! 🤍✨",
        "tags": '#uludağ #kartatili #kar #kışmodası #wintervibes #cozy #canantuna #reels #huzur'
    },
    {
        "id": 'sonbahar_nisantasi_kahve_yuruyusu',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_autumn_nisantasi.jpg'),
        "signatures": ['camel trençkot sezonunu', 'sonbahar yaprakları, sıcak bir kahve'],
        "caption": 'Sonbahar yaprakları, sıcak bir kahve ve Nişantaşı sokakları... 🍂☕ Camel trençkot sezonunu resmen açtım! Havalar hafif serinleyince sokak yürüyüşleri bana inanılmaz ilham veriyor. Sizin en sevdiğiniz sonbahar kombini ne? 🤎👇',
        "tags": '#nişantaşı #sonbahar #trençkot #sokakstili #kahvekeyfi #streetfashion #canantuna #reels #autumnvibes'
    },
    {
        "id": 'gece_kirmizi_italyan_restoran',
        "category": 'gece',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_red_dress_restaurant.jpg'),
        "signatures": ['kırmızı her kadının gardırobunda', 'hafif italyan ezgileri'],
        "caption": 'Kırmızı her kadının gardırobunda en az bir kere olmalı bence... ❤️✨ Mum ışığı, güzel bir akşam yemeği ve hafif İtalyan ezgileri. Kırmızı kombinimi nasıl buldunuz aşklar? 🍷👇',
        "tags": '#kırmızıelbise #gecedaveti #zarafet #dinner #italyan #lifestyle #canantuna #gününkaresi'
    },
    {
        "id": 'is_zumrut_blazer_executive',
        "category": 'sokak',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_emerald_blazer_office.jpg'),
        "signatures": ["zümrüt yeşili blazer'ımın", 'yeni projeler, yeni toplantılar ve yüksek'],
        "caption": "Yeni projeler, yeni toplantılar ve yüksek hedefler! 💼💚 Zümrüt yeşili blazer'ımın verdiği özgüveni çok seviyorum. Kadın girişimciler ve iş kadınları burada mı? Gücünüzü gösterin! 🚀✨",
        "tags": '#businesswoman #blazer #kariyer #ofisstili #kombin #girişimci #canantuna #stil'
    },
    {
        "id": 'sokak_alacati_sari_elbise',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_alacati_yellow_dress.jpg'),
        "signatures": ['alaçatı sokakları, pembe begonviller', 'yazdan kalan sarı sıcak anlar'],
        "caption": 'Begonviller, Alaçatı sokakları ve sarı keten elbisemin enerjisi... 🌸☀️ Soğuk günlerde bile içimi ısıtan en tatlı karelerden biri. En çok özlediğiniz tatil beldesi neresi? 💛👇',
        "tags": '#alaçatı #yazadönüş #tb #çeşme #sarıkombin #yazmodası #canantuna #enerji #reels'
    },
    {
        "id": 'spor_lila_park_fitness',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_lilac_fitness_park.jpg'),
        "signatures": ['sabah koşusu ve park esnemesi', 'lila spor takımımın enerjisine'],
        "caption": 'Sabah koşusu ve park esnemesi tamamlandı! 💜🌿 Lila spor takımımın enerjisine bayıldım. Güne erken başlamak ve ter atmak gün boyu zinde tutuyor. Bugün kendiniz için ne yaptınız? 💪🔥',
        "tags": '#fitness #sabahsporu #lilatakım #gymgirl #motivasyon #sağlıklıyaşam #canantuna #reels'
    },
    {
        "id": 'tatil_kapadokya_balonlar',
        "category": 'tatil',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_cappadocia_terrace.jpg'),
        "signatures": ["kapadokya'da gün doğumu masal", 'gökyüzündeki balonları izlerken'],
        "caption": "Kapadokya'da gün doğumu masal gibi... 🎈✨ Gökyüzündeki balonları izlerken sıcacık kahvemi yudumlamak bana inanılmaz bir huzur verdi. Hayatınızda mutlaka görmeniz gereken yerler listenize ekleyin derim! Siz Kapadokya'ya gittiniz mi aşklar? ☕🌅👇",
        "tags": '#kapadokya #cappadocia #gündoğumu #balon #seyahat #travelblogger #canantuna #huzur'
    },
    {
        "id": 'sabah_bebek_kruvasan_kahve',
        "category": 'ev',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bebek_cafe.jpg'),
        "signatures": ['sabah kahvesi ve taze kruvasan klasiği', 'bebek sahilinde güne mis gibi'],
        "caption": 'Sabah kahvesi ve taze kruvasan klasiği! 🥐☕ Bebek sahilinde güne mis gibi başladım. Tatlı krizine girenler burada mı? Kendinize güzel bir gün hediye edin aşklar 🌸💛',
        "tags": '#bebek #kahvekeyfi #kruvasan #günaydın #istanbul #lifestyle #canantuna #gününkaresi'
    },
    {
        "id": 'tatil_ege_yat_turu',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_yacht_summer.jpg'),
        "signatures": ['rüzgar saçımda, masmavi deniz önümde', "ege'nin o masmavi sularında"],
        "caption": 'Masmavi koylar ve deniz esintisi... 🌊🛥️ Bazen her şeyi geride bırakıp ufka doğru açılmak ruhu yeniliyor. Deniz tutkunları kimler bakalım? 💙👇',
        "tags": '#yazadönüş #throwback #tb #yatturu #deniz #tatil #yazözlemi #canantuna #reels #summervibes'
    },
    {
        "id": 'gece_bogaz_cati_terasi',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_rooftop_sunset.jpg'),
        "signatures": ['altın saatler (golden hour) ve boğaz', 'gün batarken bu şehir bambaşka'],
        "caption": 'Altın saatler (Golden hour) ve Boğaz manzarası... 🌇✨ Gün batarken bu şehir bambaşka bir büyüye bürünüyor. Akşam planınız ne canlar? 🍷❤️',
        "tags": '#goldenhour #günbatımı #istanbul #boğaz #rooftop #zarafet #canantuna #reels'
    },
    {
        "id": 'tatil_bodrum_beach',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_bodrum_beach_1792678870147.jpg'),
        "signatures": ['deniz, güneş ve biraz kafa dinlemece', 'bodrum bana her zaman çok iyi geliyor', 'deniz mi havuz mu deseler'],
        "caption": "Bodrum'un o sıcak güneşi ve kumsalı... ☀️🌊 Deniz mi havuz mu deseler siz hangisini seçerdiniz? 🌊👇",
        "tags": '#yazadönüş #throwback #tb #bodrum #tatil #beachvibes #güneş #yaz #canantuna #reels'
    },
    {
        "id": 'sokak_karakoy_yagmur',
        "category": 'sokak',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_karakoy_street_portrait_1792678880948.jpg'),
        "signatures": ['yağmurda ıslanmayı seven kaç kişiyiz', 'karaköy sokaklarında yürüyüş yapıp'],
        "caption": 'Yağmurda ıslanmayı seven kaç kişiyiz? 🌧️🌂 Karaköy sokaklarında yürüyüş yapıp kahvemi aldım. Yağmurlu havalar bana inanılmaz ilham veriyor... ✨',
        "tags": '#karaköy #istanbul #yağmur #trenchcoat #sokakmodası #canantuna #lifestyle'
    },
    {
        "id": 'spor_pilates_reformer',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_pilates_portrait_1792678899801.jpg'),
        "signatures": ['reformer seansı bitti, ter atıldı', 'vücuduna iyi bakmak kendine yapabileceğin'],
        "caption": 'Reformer seansı bitti, ter atıldı! 💪🧘\u200d♀️ Vücuduna iyi bakmak kendine yapabileceğin en büyük iyilik. Bugün spora vakit ayırdınız mı canlar? 🔥👇',
        "tags": '#pilates #reformer #fitgirl #spor #sağlıklıyaşam #canantuna #gymmotivation'
    },
    {
        "id": 'gece_bogaz_aksam_yemegi',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_bosphorus_night_1792678913579.jpg'),
        "signatures": ["istanbul geceleri ve boğaz'ın ışıkları", 'bazen sadece durup bu şehrin tadını'],
        "caption": "İstanbul geceleri ve Boğaz'ın ışıkları... 🌉✨ Bazen sadece durup bu şehrin tadını çıkarmak gerekiyor. Akşamınız nasıl geçiyor aşklar? 🍷❤️",
        "tags": '#boğaz #istanbul #iyigeceler #şekerim #canantuna #gecehayatı #dinner'
    },
    {
        "id": 'sokak_araba_selfie',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_driver_selfie_1792678924695.jpg'),
        "signatures": ['istanbul trafiği klasiği: kırmızı ışıkta', 'şarkımı açtım enerjimi düşürmüyorum'],
        "caption": 'İstanbul trafiği klasiği: Kırmızı ışıkta selfie çekilir! 🚗💨 Şarkımı açtım enerjimi düşürmüyorum. Trafikte olanlara sabırlar diliyorum 🙈🎧',
        "tags": '#istanbul #trafik #selfie #carselfie #gününkaresi #canantuna #enerji'
    },
    {
        "id": 'ev_balkon_ciplak_ayak',
        "category": 'ev',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_cozy_balcony_portrait_1792678939456.jpg'),
        "signatures": ['balkonda sabah kahvesi, serin hava', 'bütün gün böyle oturabilirim'],
        "caption": 'Balkonda sabah kahvesi, serin hava ve sessizlik... ☕🌿 Bütün gün böyle oturabilirim. Güne güzel bir başlangıç yaptık, sizde durumlar ne? 🌸👇',
        "tags": '#günaydın #kahvekeyfi #huzur #evhali #balkonkeyfi #canantuna #gününkaresi'
    },
    {
        "id": 'sokak_nisantasi_kafe',
        "category": 'sokak',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tana_nisantasi_cafe_1792666291150.jpg'),
        "signatures": ['nişantaşı sokakları ve buz gibi bir filtre', "kombinimi nasıl buldunuz? 🕶️✨ nişantaşı'nda"],
        "caption": 'Nişantaşı sokakları ve buz gibi bir filtre kahve... ☕🕶️ Enerjim tavan! Bugün kendiniz için ne yaptınız aşklar? 👇✨',
        "tags": '#nişantaşı #istanbul #kahvekeyfi #sokakmodası #canantuna #lifestyle'
    },
    {
        "id": 'ev_sabah_kahvesi',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_morning_lifestyle_1792660779429.jpg'),
        "signatures": ['güne kahvesiz başlayamayanlar el kaldırsın', 'bugünün mottosu: gülümse ve anı yaşa'],
        "caption": 'Güne kahvesiz başlayamayanlar el kaldırsın! ☕☀️ Bugünün mottosu: Gülümse ve anı yaşa! Harika bir gün olsun hepimize 🌸💛',
        "tags": '#günaydın #sabahkahvesi #evhali #huzur #canantuna #pozitifenerji'
    },
    {
        "id": 'sokak_kis_sicak_kahve',
        "category": 'sokak',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_winter_street_1792666325312.jpg'),
        "signatures": ['hava buz gibi ama içimizi ısıtan', 'kar görünce çocuk gibi sevinenler'],
        "caption": 'Hava buz gibi ama içimizi ısıtan kahvemiz var ❄️☕ Karlı günlerde sokakta yürümek bana hep masal gibi gelir. Siz kış insanı mısınız? ☃️🤍',
        "tags": '#kış #kar #soğuk #kahvekeyfi #canantuna #wintervibes'
    },
    {
        "id": 'spor_gym_ayna_selfie',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_fitness_selfie_1792663898849.jpg'),
        "signatures": ['bahane yok, disiplin var', 'bugünkü bacak & kalça antrenmanı bitti'],
        "caption": 'Bahane yok, disiplin var! 🔥💪 Bugünkü antrenmanı tamamladım. Aynadaki değişimi görmek en büyük motivasyonum! Siz başladınız mı? 🏋️\u200d♀️',
        "tags": '#fitness #gymmotivation #fitgirl #disiplin #spor #canantuna #workout'
    },
    {
        "id": 'spor_sonrasi_hali_dinlenme',
        "category": 'spor',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_post_workout_1792664056043.jpg'),
        "signatures": ['bacak gününden sonra halıya', 'halıya serilenler derneği'],
        "caption": 'Bacak gününden sonra halıya serilenler derneği başkanı seçildim sanırım! 🙈😂 Yorulduk ama değdi. Şimdi güzel bir dinlenme zamanı 💆\u200d♀️✨',
        "tags": '#postworkout #fitlife #dinlenme #yorgunluk #canantuna #gymgirl'
    },
    {
        "id": 'ev_pazar_rahatligi',
        "category": 'ev',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_cozy_livingroom_png_1792663231002.jpg'),
        "signatures": ['evde battaniye ve sıcak bir çay', 'hiçbir şey yapmamak da ruhuna'],
        "caption": 'Evde battaniye ve sıcak bir çay modundayım bugün... 🛋️📖 Bazen hiçbir şey yapmamak da ruhuna çok iyi gelir. Bugün evde misiniz dışarıda mı? 🍵👇',
        "tags": '#evkeyfi #huzur #cozyvibes #dinlenme #canantuna #haftasonu'
    },
    {
        "id": 'ev_gunesli_balkon_selfie',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tuna_selfie_1792665280198.jpg'),
        "signatures": ['güneş açtıysa enerjimiz de yerine gelir', 'yepyeni hedefler, güzel başlangıçlar'],
        "caption": 'Güneş açtıysa enerjimiz de yerine gelir! ☀️🌸 Yepyeni hedefler, güzel başlangıçlar... Gününüz harika geçsin canlar! 💖✨',
        "tags": '#güneş #pozitifenerji #selfie #balkonkeyfi #canantuna #gününkaresi'
    },
    {
        "id": 'lifestyle_vanity_mirror_makyaj',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_vanity_mirror.jpg'),
        "signatures": ['hazırlanırken aynaya bir bakış', 'günün enerjisini yakalama anı'],
        "caption": 'Hazırlanırken aynaya bir bakış ve günün enerjisini yakalama anı... ✨💄 Kendinize değer verdiğiniz her an çok kıymetli. Akşam planları yapıldı mı canlar? 💋👠',
        "tags": '#vanity #grwm #lifestyle #makyaj #güzellik #canantuna #mirrorselfie'
    },
    {
        "id": 'spor_kortta_tenis_padel',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tennis_court.jpg'),
        "signatures": ['kortta maç bitti ama enerji hala tavan', 'spor sadece bedenine değil ruhuna'],
        "caption": 'Kortta maç bitti ama enerji hala tavan! 🎾🔥 Spor sadece bedenine değil ruhuna da iyi gelen en güzel terapi. Bugün hareket ettik mi? 💪✨',
        "tags": '#tennis #padel #tenis #fitgirl #sportystyle #canantuna #fitnessmotivation'
    },
    {
        "id": 'tatil_sonsuzluk_havuzu_gunbatimi',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_infinity_pool.jpg'),
        "signatures": ['gün batımında sonsuzluğa karşı durup', 'yazdan kalan sıcacık anlar', 'güneşi böyle batırmayı özleyenler'],
        "caption": 'Sonsuzluk havuzunda güneşi batırdığımız o huzurlu akşamüstü... 🌅🌊 Bir kahve alıp manzaraya karşı dalıp gitmeyi özleyenler kimler? ☕💛',
        "tags": '#tb #yazadönüş #sunset #infinitypool #tatil #yazözlemi #canantuna #travelgram #goldenhour #reels'
    },
    {
        "id": 'kultur_cagdas_sanat_galerisi',
        "category": 'sokak',
        "type": 'photo',
        "image_path": os.path.join(IMAGES_DIR, 'canan_art_gallery.jpg'),
        "signatures": ['sanatın içinde kaybolduğum', 'renklerin hikayesini dinlediğim'],
        "caption": 'Sanatın içinde kaybolduğum, renklerin hikayesini dinlediğim bir gün... 🎨🖼️ Modern sanat bana her zaman yeni bakış açıları kazandırıyor. Galerileri gezmeyi sevenler burda mı? 🤍✨',
        "tags": '#artgallery #sanat #istanbul #modernart #kultur #canantuna #streetstyle #ootd'
    },
    {
        "id": 'hobi_somine_dag_evi',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_fireplace_chalet.jpg'),
        "signatures": ['dışarıda lapa lapa kar, içeride çıtırdayan', 'çıtırdayan şömine ateşi'],
        "caption": 'Dışarıda lapa lapa kar, içeride çıtırdayan şömine ateşi... ❄️🔥 Kışın en sevdiğim yanı bu sıcak sığınaklar. Bir fincan sıcak kahve ve huzur... Siz kış insanı mısınız yoksa yaz aşığı mı? Yorumlarda buluşalım! ☕✨',
        "tags": '#kış #şömine #dağevi #huzur #cozyvibes #canantuna #wintervibes #reels'
    },
    {
        "id": 'sokak_bebek_sonbahar_yuruyusu',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bebek_autumn_walk.jpg'),
        "signatures": ['bebek sahilinde hafif bir boğaz esintisi', "istanbul'un sonbaharı bana her zaman"],
        "caption": "Bebek sahilinde hafif bir Boğaz esintisi ve elimde sıcak kahvem... 🌊☕ İstanbul'un sonbaharı bana her zaman yeni kararlar ve taze umutlar getirir. Bugün kendinize bir iyilik yapıp yürüyüşe çıktınız mı canlar? 🍂💛",
        "tags": '#bebek #istanbul #boğaz #sonbahar #trenchcoat #sokakmodasıkombin #canantuna #lifestyle #reels'
    },
    {
        "id": 'gece_mum_isiginda_aksam_yemegi',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_candlelight_dinner.jpg'),
        "signatures": ['istanbul ışıl ışıl ayaklarımızın altında', 'kadehlerimizi güzelliklere ve hayallerimize'],
        "caption": 'İstanbul ışıl ışıl ayaklarımızın altında... 🌃✨ Bazen sadece durmak, bu anın tadını çıkarmak ve iyi ki demek gerekir. Bu gece kadehlerimizi güzelliklere ve hayallerimize kaldırıyoruz! 🥂💙',
        "tags": '#istanbul #gece #rooftop #dinner #zarafet #canantuna #gecehayatı #reels'
    },
    {
        "id": 'lifestyle_kitap_kafe_karakoy',
        "category": 'lifestyle',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bookstore_cafe.jpg'),
        "signatures": ['kitap kokusu, taze demlenmiş bir latte', "karaköy'ün bu huzurlu köşesinde"],
        "caption": "Kitap kokusu, taze demlenmiş bir latte ve yeni projeler... 📚☕ Karaköy'ün bu huzurlu köşesinde saatlerin nasıl geçtiğini anlamıyorum. Bu aralar hangi kitabı okuyorsunuz, bana öneriniz var mı? 📖💭",
        "tags": '#kitap #kafe #karaköy #lifestyle #kahvekeyfi #canantuna #bookstagram #reels'
    },
    {
        "id": 'kis_uludag_kayak_zirve_teras',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_ski_terrace.jpg'),
        "signatures": ['zirvede hava tertemiz, güneş pırıl pırıl', 'termostan sıcak çay içmenin keyfi'],
        "caption": 'Zirvede hava tertemiz, güneş pırıl pırıl! ⛷️❄️ Karların üzerinde termostan sıcak çay içmenin keyfi hiçbir şeyde yok. Beyaz örtü bana inanılmaz enerji veriyor! Kayak yapmayı sevenler burada mı? 🏔️💙',
        "tags": '#uludağ #kayak #kıştatili #zirve #snow #kar #canantuna #travelgram #reels'
    },
    {
        "id": 'ev_pazar_mutfak_granola',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_kitchen_morning.jpg'),
        "signatures": ['pazar sabahı mutfakta taze kahve kokusu', 'renkli meyveler... 🍓☕ kendime vakit'],
        "caption": 'Pazar sabahı mutfakta taze kahve kokusu ve renkli meyveler... 🍓☕ Kendime vakit ayırdığım en tatlı saatler. Güne nasıl başlarsanız öyle gider; gülümsemeyi unutmayın güzellikler! 🌸✨',
        "tags": '#pazarkahvaltısı #evhali #sağlıklıyaşam #mutfak #granola #canantuna #morningvibes #reels'
    },
    {
        "id": 'lifestyle_termal_spa_dinlenme',
        "category": 'lifestyle',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_spa_wellness.jpg'),
        "signatures": ['bütün haftanın yorgunluğunu geride bırakma', 'sıcak su buharı ve bitki çayı'],
        "caption": 'Bütün haftanın yorgunluğunu geride bırakma terapisi... 🧖\u200d♀️🌿 Sıcak su buharı ve bitki çayı ruhuma o kadar iyi geldi ki. Bedeninizi dinlendirmeyi ve şımartmayı ihmal etmeyin canlar! 💧✨',
        "tags": '#spa #wellness #kendinezamanayır #dinlenme #sağlık #canantuna #selfcare #reels'
    },
    {
        "id": 'sokak_bogaz_koprusu_araba',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_car_bosphorus_bridge.jpg'),
        "signatures": ['köprüden geçerken güneş tam batış', 'trafik bile olsa bu manzaraya değer'],
        "caption": 'Köprüden geçerken güneş tam batış anında yüzüme vuruyor... 🚗🌅 En sevdiğim şarkı çalıyor ve İstanbul yine büyülemeye devam ediyor. Trafik bile olsa bu manzaraya değer! Sizde akşam nasıl geçiyor? 🎶💫',
        "tags": '#istanbul #boğazköprüsü #goldenhour #günbatımı #carvibes #canantuna #gününkaresi #reels'
    },
    {
        "id": 'sokak_karakoy_mural_grafiti',
        "category": 'sokak',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_karakoy_mural.jpg'),
        "signatures": ['karaköy sokaklarındaki bu renkli duvar', 'duvar sanatı enerjimi ikiye katladı'],
        "caption": 'Karaköy sokaklarındaki bu renkli duvar sanatı enerjimi ikiye katladı! 🎨☕ Sokak modasını ve canlı renkleri çok seviyorum. Günün kombini nasıl olmuş kızlar? Yorumları görelim! 💚👟',
        "tags": '#karaköy #sokakmodası #streetstyle #ootd #grafiti #canantuna #lifestyle #reels'
    },
    {
        "id": 'is_levent_plaza_yonetim',
        "category": 'is',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_executive_office.jpg'),
        "signatures": ['günün son toplantısı bitti ve arkamda', 'parlayan levent silüeti'],
        "caption": 'Günün son toplantısı bitti ve arkamda gün batımıyla parlayan Levent silüeti... 💼🌇 Disiplin ve vizyon bir araya gelince imkansız diye bir şey kalmıyor. Hayallerinizin peşini asla bırakmayın! 🚀🤍',
        "tags": '#business #işkadını #motivasyon #levent #başarı #canantuna #career #reels'
    },
    {
        "id": 'tatil_ciragan_sarayi_kahvalti',
        "category": 'tatil',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_ciragan_palace.jpg'),
        "signatures": ["çırağan sarayı'nın deniz kenarındaki", "boğaz'ın mavisi ve saray havası"],
        "caption": "Çırağan Sarayı'nın deniz kenarındaki terasında masalsı bir sabah... 🏰🌊 Boğaz'ın mavisi ve saray havası insanın ruhuna dokunuyor. İstanbul'da en sevdiğiniz tarihi mekan neresi? 💙✨",
        "tags": '#çırağansarayı #boğaz #istanbul #lüksyaşam #saray #canantuna #travel #reels'
    },
    {
        "id": 'lifestyle_moda_sahil_gunbatimi',
        "category": 'lifestyle',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_moda_sunset.jpg'),
        "signatures": ['moda sahilinde çimlere serilip', 'anadolu yakasının bu dinginliğini'],
        "caption": 'Moda sahilinde çimlere serilip gün batımını izlemek paha biçilemez... 🌅🍂 Akustik tınılar, serin rüzgar ve hafif sıcak bir çay. Anadolu yakasının bu dinginliğini çok seviyorum! 🧡🎶',
        "tags": '#moda #kadıköy #günbatımı #sahil #huzur #canantuna #akustik #reels'
    },
    {
        "id": 'lifestyle_otel_lobi_orkide',
        "category": 'lifestyle',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_hotel_lobby.jpg'),
        "signatures": ['zarafet detaylarda gizlidir', 'dev orkideler ve sıcacık bir lobi'],
        "caption": 'Zarafet detaylarda gizlidir... ☕🌸 Dev orkideler ve sıcacık bir lobi sohbeti. Kendinizi iyi hissettiren mekanlarda vakit geçirmek enerjinizi anında tazeliyor. Keyifli bir akşam olsun! 🤍✨',
        "tags": '#zarafet #lifestyle #lüks #otel #kahvesohbeti #canantuna #ootd #reels'
    },
    {
        "id": 'ev_kis_pencere_sicak_cikolata',
        "category": 'ev',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_winter_window.jpg'),
        "signatures": ['camın kenarına kıvrılıp yağan karı', 'bol köpüklü sıcak çikolata'],
        "caption": 'Camın kenarına kıvrılıp yağan karı izlemek ve elinde bol köpüklü sıcak çikolata... 🍫❄️ Peri masalı gibi bir akşam. Kış akşamlarının bu tatlı nostaljisini kimler seviyor? 🕯️🤍',
        "tags": '#kışakşamı #sıcakçikolata #evkeyfi #nostalji #kar #canantuna #cozynight #reels'
    },
    {
        "id": 'spor_kort_tenis_mola',
        "category": 'spor',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_tennis_bench.jpg'),
        "signatures": ['tenis maçında son set bitti', 'ter su içindeyiz ama mutluluk'],
        "caption": 'Tenis maçında son set bitti, ter su içindeyiz ama mutluluk paha biçilemez! 🎾💪 Spor yapmak günün tüm stresini silip süpürüyor. Bugün hareket ettiniz mi canlar? Haydi harekete geçin! 🔥👟',
        "tags": '#tenis #kort #fitgirl #sporaşkı #motivasyon #canantuna #workout #reels'
    },
    {
        "id": 'gece_galata_kulesi_sokak',
        "category": 'gece',
        "type": 'video',
        "image_path": os.path.join(IMAGES_DIR, 'canan_galata_night.jpg'),
        "signatures": ['galata sokaklarında akşam yürüyüşü', 'arkamda asırların şahidi kule'],
        "caption": "Galata sokaklarında akşam yürüyüşü ve arkamda asırların şahidi kule... 🗼🌙 Taş sokakların tarihi kokusu büyüleyici. Galata'ya her geldiğimde ilk kez görüyormuş gibi aşık oluyorum! 🖤✨",
        "tags": '#galata #galatakulesi #istanbulgeceleri #tarih #geceyürüyüşü #canantuna #reels'
    },
    {
        "id": 'oje_zumrut_yesil_kadife_koltuk',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Zümrüt yeşili ojem ve elbisem nasıl olmuş?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_emerald_polish_velvet.jpg'),
        "signatures": ['zümrüt yeşili ojemi sürerken elbisemle', 'kadife koltukta bakım saati'],
        "caption": 'Bu akşam farklılık yapıp zümrüt yeşili oje denedim ve elbisemle uyumuna bayıldım! 💅💚 Sizce koyu yeşil mi yoksa klasik kırmızı mı daha çok yakışıyor? 4 kareyi de izleyip kararınızı yoruma yazın! ✨👇',
        "tags": '#oje #pedikür #zümrütyeşili #bakım #evhali #zarafet #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_yakut_kirmizi_pencere_kenari',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Gün batımında yakut kırmızısı oje keyfi!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_ruby_polish_window.jpg'),
        "signatures": ['pencere kenarında gün batımı ve yakut kırmızısı', 'ojemi yeni tazeledim kurumalarını bekliyorum'],
        "caption": 'Pencere kenarında gün batımını izlerken yakut kırmızısı ojemi tazeledim... 🌅💅 Kurumalarını beklerken size küçük bir selam göndermek istedim! Bu tonu beğendiniz mi? ❤️👇',
        "tags": '#kırmızıoje #günbatımı #pedikür #bakımzamanı #evkeyfi #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_bebek_pembesi_koltuk_sabah',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Bugün bebek pembesi oje seçtim, yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_baby_pink_couch.jpg'),
        "signatures": ['ipek sabahlığımla koltuğa geçtim bebek pembesi', 'açık ton oje sevenler burada mı'],
        "caption": 'Sabah kahvemden hemen sonra ipek sabahlığımla koltuğa geçtim ve bebek pembesi oje sürdüm! 🌸💅 Açık ve zarif tonları sevenler burada mı? 10 üzerinden kaç puan verirsiniz? 🥰👇',
        "tags": '#pembeoje #bakım #sabahkeyfi #pedikür #evhali #zarif #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_bordo_hali_aksam_isigi',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Akşam ışığında koyu bordo oje asaleti!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_bordeaux_rug_evening.jpg'),
        "signatures": ['yumuşacık halının üzerinde akşam dinlenmesi', 'koyu bordo ojenin yeri her zaman ayrı'],
        "caption": 'Yumuşacık halının üzerinde akşam dinlenmesi... 🕯️🍷 Koyu bordo ojenin asaleti ve yeri bende her zaman ayrı. Sizce bordo mu daha iddialı yoksa parlak kırmızı mı? Yorumlarda buluşalım! ✨👇',
        "tags": '#bordooje #akşamkeyfi #evhali #pedikür #bakım #şıklık #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_gumus_halhal_teras_gunes',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Gümüş halhalım ve kırmızı ojem nasıl duruyor?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_silver_anklet_terrace.jpg'),
        "signatures": ['terasta güneşlenirken ince gümüş halhalım', 'turkuaz elbise ve kırmızı oje uyumu'],
        "caption": 'Güneşli terasta dinlenirken ince gümüş halhalım ve kırmızı ojemin uyumuna bayıldım! ☀️💎 Halhal takmayı çok seviyorum, sizce zarif durmuş mu? Görüşlerinizi bekliyorum! 💙👇',
        "tags": '#halhal #teras #kırmızıoje #tatil #yazkeyfi #bakım #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_parlak_kirmizi_uzanma_koltugu',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Parlak kırmızı ojemden vazgeçemiyorum!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_glossy_red_chaise.jpg'),
        "signatures": ['uzanma koltuğunda ayaklarımızı uzatıp bakım', 'parlak kırmızı ojeden asla vazgeçemem'],
        "caption": 'Günün yorgunluğunu uzanma koltuğunda ayaklarımızı uzatarak atıyoruz... 💅❤️ Ne kadar farklı renk denesem de parlak kırmızı ojeden asla vazgeçemiyorum! Sizce de en güzeli bu değil mi? 😉👇',
        "tags": '#kırmızıoje #pedikür #dinlenme #evkeyfi #bakımlıkadın #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_mor_lila_yatak_bakim',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Lila gecelik ve koyu mor oje uyumuna puanınız kaç?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_violet_polish_bed.jpg'),
        "signatures": ['lila ipek geceliğimle uyumlu koyu mor oje', 'yatakta gece bakımı tamamlandı'],
        "caption": 'Bu gece lila ipek geceliğimle tam uyumlu koyu mor bir oje sürdüm! 💜💅 Renk uyumuna dikkat edenler bu detayı beğendi mi bakalım? Yorumlarınızı tek tek okuyorum! ✨👇',
        "tags": '#moroje #lila #gecebakımı #pedikür #evhali #uyum #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_seftali_balkon_kahve',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Balkonda sabah kahvesi ve şeftali tonu ojem!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_peach_pedi_balcony.jpg'),
        "signatures": ['balkonda sabah kahvem ve şeftali tonu', 'beyaz keten gömlek elbise rahatlığı'],
        "caption": 'Güneşli balkonda sabah kahvem, beyaz keten elbisem ve yeni sürdüğüm şeftali tonu ojem... ☕🍑 Doğal ve sıcak tonları sevenler için harika bir seçim oldu. Güne nasıl başladınız? ☀️👇',
        "tags": '#balkonkeyfi #sabahkahvesi #pedikür #oje #doğalgüzellik #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_koyu_kirmizi_yastik_pozu',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Yatakta dinlenme vakti! Hangi kare daha güzel?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_crimson_pillow_pose.jpg'),
        "signatures": ['yastıklara gömülüp dinlenme saati geldi', 'siyah saten ve kırmızı oje ikilisi'],
        "caption": 'Yastıklara gömülüp tüm günün stresini unutma saati geldi! 🖤💅 Siyah saten ve kırmızı oje ikilisi her zaman favorim. Videodaki 4 kareden sizin favoriniz hangisi oldu? (1-2-3-4) 😉👇',
        "tags": '#iyiaksamlar #saten #kırmızıoje #evhali #dinlenme #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_kiraz_ayna_onu_bakim',
        "category": 'ev',
        "type": 'video',
        "bold": True,
        "hook": 'Ayna önünde bakım hazırlığı! Kırmızı yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_cherry_mirror_floor.jpg'),
        "signatures": ['boy aynasının karşısına geçip kiraz kırmızısı', 'kırmızı bluz ve kırmızı oje uyumu'],
        "caption": 'Boy aynasının karşısına geçip kiraz kırmızısı ojemi sürdüm! 🍒💅 Kırmızı bluzumla harika bir takım oldular. Bakımlı olmayı seven herkesi yorumlara bekliyorum! ❤️👇',
        "tags": '#ayna #kirazkırmızısı #oje #bakım #evkombin #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_altin_sandalet_havuz_kenari',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Akşamüstü havuz kenarında serinleme vakti!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_gold_sandals_pool.jpg'),
        "signatures": ['altın sandaletlerimi çıkardım ayaklarımı havuza', 'akşamüstü havuz suyunun serinliği'],
        "caption": 'Altın sandaletlerimi kenara çıkardım, ayaklarımı ılık havuz suyuna bıraktım... 💦✨ Akşamüstü havuz başının bu huzurlu atmosferini çok seviyorum. Yanımda kimler olmak isterdi? 🌅👇',
        "tags": '#havuzbaşı #tatil #kırmızıoje #günbatımı #yazakşamı #canantuna #reels #keşfet'
    },
    {
        "id": 'oje_french_pedikur_sampanya_elbise',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'French pedikür mü yoksa Kırmızı oje mi? Karar sizin!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_feet_french_polish_sofa.jpg'),
        "signatures": ['şampanya rengi saten elbisemle french pedikür', 'sizce french mi yoksa kırmızı oje mi'],
        "caption": 'Şampanya rengi saten elbisemle bu kez zarif bir French pedikür tercih ettim! 🥂✨ Çok merak ediyorum; sizce French mi daha çekici yoksa klasik kırmızı oje mi? Yorumlarda oylayalım! 👇',
        "tags": '#frenchpedikür #oje #satenelbise #zarafet #anket #canantuna #reels #keşfet'
    },
    {
        "id": 'sik_kirmizi_kadife_otel_gece',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Kırmızı kadife elbisemle geceye hazırım!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_red_velvet_evening.jpg'),
        "signatures": ['kırmızı kadife mini elbisemle akşam davetine', 'kırmızı rengin enerjisi bambaşka'],
        "caption": 'Kırmızı kadife mini elbisemle akşam davetine hazırım! ❤️✨ Kırmızı rengin insana verdiği özgüven ve enerji gerçekten bambaşka. Bu akşamki kombinime 10 üzerinden kaç verirsiniz? 😉👇',
        "tags": '#kırmızıelbise #kadife #geceşıklığı #davet #kombin #canantuna #reels #keşfet'
    },
    {
        "id": 'sik_siyah_saten_balkon_sehir',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Şehir ışıkları ve siyah saten şıklığı!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_satin_balcony.jpg'),
        "signatures": ['balkondan şehrin ışıltısını izlerken siyah saten', 'gece esintisi ve huzur dolu bir akşam'],
        "caption": 'Balkondan şehrin ışıltısını izlerken hafif gece esintisinin tadını çıkarıyorum... 🌃🖤 Siyah saten elbisenin zarafeti her ortama yakışıyor. Hangi şehirden beni takip ediyorsunuz? Yorumlara yazın! 👇',
        "tags": '#siyahsaten #balkon #şehirışıkları #gece #zarafet #canantuna #reels #keşfet'
    },
    {
        "id": 'tatil_beyaz_loca_deniz_keyfi',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Deniz kenarı locada yaz esintisi!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_white_bikini_cabana.jpg'),
        "signatures": ['turkuaz denizin karşısında beyaz locada', 'beyaz plaj takımım ve kırmızı ojem'],
        "caption": 'Turkuaz denizin tam karşısında, bembeyaz locada rüzgarın ve güneşin keyfini çıkarıyorum! 🏖️🤍 Beyaz plaj takımım nasıl olmuş? Tatil özlemi çekenler yoruma el kaldırsın! ☀️👇',
        "tags": '#plaj #loca #akdeniz #tatil #yaz #beyazkombin #canantuna #reels #keşfet'
    },
    {
        "id": 'spor_lavanta_takim_ev_pilates',
        "category": 'spor',
        "type": 'video',
        "bold": True,
        "hook": 'Lavanta spor takımım ve sabah enerjisi!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_lavender_gym_set.jpg'),
        "signatures": ['lavanta rengi spor takımımla yoga matında', 'yalınayak evde egzersiz gibisi yok'],
        "caption": 'Lavanta rengi spor takımımla sabah egzersizini tamamladım! 🧘‍♀️💜 Evde yalınayak matın üzerinde spor yapmak hem bedeni hem ruhu dinlendiriyor. Formumu korumak için her gün 40 dakika! 💪👇',
        "tags": '#pilates #evdespor #fit #motivasyon #sağlıklıyaşam #canantuna #reels #keşfet'
    },
    {
        "id": 'gece_altin_payetli_elbise_lounge',
        "category": 'gece',
        "type": 'photo',
        "bold": True,
        "hook": 'Altın payetli elbisemle ışıltılı bir akşam!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_gold_sequin_night.jpg'),
        "signatures": ['altın payetli mini elbisemle bu akşam', 'ışıltıyı ve şık mekanları sevenler'],
        "caption": 'Altın payetli mini elbisemle bu akşam biraz parlamaya karar verdim! ✨🥂 Şık bir mekanda güzel müzik eşliğinde dinlenmek harika geliyor. Elbisemi beğendiniz mi? 💛👇',
        "tags": '#altınelbise #payet #gecehayatı #şıklık #zarafet #canantuna #lifestyle'
    },
    {
        "id": 'ev_zumrut_ipek_yatak_aksam',
        "category": 'ev',
        "type": 'photo',
        "bold": True,
        "hook": 'Zümrüt yeşili ipek pijama takımım nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_emerald_silk_bed.jpg'),
        "signatures": ['loş abajur ışığında zümrüt yeşili ipek', 'evde de şık ve bakımlı olmayı seviyorum'],
        "caption": 'Loş abajur ışığında dinlenme vakti... 💚✨ Evde yalnızken bile şık ve bakımlı olmayı çok seviyorum. Zümrüt yeşili ipek takımım sizce nasıl olmuş? Huzurlu geceler! 🌙👇',
        "tags": '#ipekpijama #evşıklığı #bakım #iyigeceler #huzur #canantuna #lifestyle'
    },
    {
        "id": 'tatil_mercan_mini_elbise_iskele',
        "category": 'tatil',
        "type": 'video',
        "bold": True,
        "hook": 'Ahşap iskelede gün batımı ve mercan elbisem!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_coral_mini_sunset.jpg'),
        "signatures": ['ahşap iskelede yalınayak gün batımı yürüyüşü', 'mercan rengi yazlık elbisem'],
        "caption": 'Ahşap iskelede yalınayak gün batımı yürüyüşü... 🌅🧡 Mercan rengi elbisem güneşin son ışıklarıyla birleşince ortaya bu kare çıktı! Gün batımını deniz kenarında izlemeyi sevenler kimler? ✨👇',
        "tags": '#iskele #günbatımı #mercan #yazelbisesi #yalınayak #canantuna #reels #keşfet'
    },
    {
        "id": 'ev_lacivert_saten_deri_koltuk',
        "category": 'gece',
        "type": 'video',
        "bold": True,
        "hook": 'Lacivert saten elbisemle akşam keyfi!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_navy_satin_couch.jpg'),
        "signatures": ['krem rengi koltukta lacivert saten elbisemle', 'size küçük bir göz kırpışı bırakıyorum'],
        "caption": 'Krem rengi koltukta lacivert saten elbisemle akşam keyfi yaparken size küçük bir göz kırpışı bırakıyorum! 😉💙 Lacivert tonları esmer/buğday tene sizce nasıl gidiyor? Yorumları bekliyorum! 👇',
        "tags": '#lacivert #satenelbise #evkeyfi #akşam #zarafet #canantuna #reels #keşfet'
    },
    {
        "id": 'tatil_siyah_mayo_jakuzi_günbatımı',
        "category": 'tatil',
        "type": 'photo',
        "bold": True,
        "hook": 'Açık hava jakuzisinde gün batımı huzuru!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_black_bikini_jacuzzi.jpg'),
        "signatures": ['açık hava jakuzisinde gün batımına karşı', 'sıcak su ve serin akşam rüzgarı'],
        "caption": 'Açık hava jakuzisinde gün batımına karşı tüm yorgunluğu geride bırakıyorum... 💦🌅 Sıcak su ve hafif akşam esintisi bir arada muhteşem oluyor. Keyifli akşamlar! 🖤✨',
        "tags": '#jakuzi #spa #günbatımı #tatil #dinlenme #canantuna #lifestyle'
    },
    {
        "id": 'gece_bordo_korse_teras_yemek',
        "category": 'gece',
        "type": 'photo',
        "bold": True,
        "hook": 'Mum ışığında akşam yemeği! Kombinim nasıl?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_burgundy_corset_dinner.jpg'),
        "signatures": ['mum ışığında terasta akşam yemeği', 'bordo korse bluz ve mini etek takımım'],
        "caption": 'Mum ışığında, Boğaz manzaralı terasta şık bir akşam yemeği... 🕯️🍷 Bordo korse bluz ve mini etek takımımı bu gece için özel seçtim. Şıklığa önem verenlerden tam not alır mıyız? ❤️👇',
        "tags": '#akşamyemeği #teras #bordo #kombin #şıklık #canantuna #lifestyle'
    },
    {
        "id": 'ev_pembe_ipek_sabahlik_pencere',
        "category": 'ev',
        "type": 'photo',
        "bold": True,
        "hook": 'Güneşli bir sabahtan herkese günaydın!',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_pink_silk_morning.jpg'),
        "signatures": ['pencereden süzülen sabah güneşi ve ilk kahvem', 'pudra pembesi ipek sabahlığımla'],
        "caption": 'Pencereden süzülen sabah güneşi, elimde sıcak kahvem ve pudra pembesi ipek sabahlığım... ☕🌸 Güne erken ve pozitif başlamayı çok seviyorum. Herkese harika bir gün olsun! ☀️👇',
        "tags": '#günaydın #sabahkahvesi #ipeksabahlık #pozitifenerji #evhali #canantuna'
    },
    {
        "id": 'ev_zeytin_yesili_elbise_ayna',
        "category": 'lifestyle',
        "type": 'photo',
        "bold": True,
        "hook": 'Çıkmadan önce son ayna kontrolü! Yakışmış mı?',
        "image_path": os.path.join(IMAGES_DIR, 'canan_bold_olive_mini_mirror.jpg'),
        "signatures": ['evden çıkmadan önce giyinme odasında son ayna', 'zeytin yeşili mini elbisem nasıl olmuş'],
        "caption": 'Evden çıkmadan önce giyinme odasında son ayna kontrolü! 🪞💚 Zeytin yeşili mini elbisem ve henüz ayakkabılarımı giymeden yalınayak halimle bir kare aldım. Kombin onaylandı mı? 😉👇',
        "tags": '#aynaselfiesi #kombin #ootd #yeşilelbise #şıklık #canantuna #lifestyle'
    },
]


def get_scenario_by_id(scenario_id: str) -> dict:
    for s in SCENARIOS:
        if s["id"] == scenario_id:
            return s
    return SCENARIOS[0]
