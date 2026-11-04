import os

"""
Canan Tuna - Genişletilmiş Otonom Yaşam Simülasyonu Senaryo Kütüphanesi (61 Benzersiz Senaryo)
Her senaryo kendine özel, sıfırdan üretilmiş BİRİNCİL GÖRSELİNE,
eski paylaşımları da tanıyan 'signatures' imzalarına ve alternatif taze açıklamalara ('alt_captions') sahiptir.
Tüm görseller assets/images/ altında bağımsız ve taşınabilir olarak saklanır.
"""

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")

SCENARIOS = [
    # --- 🌟 YEPYENİ 17 ÖZEL TASARIM SENARYO (TÜM RENKLER, KOMBİNLER & ÇEKİCİ POZLAR) ---
    {
        "id": "spor_bordo_gym_ayna_selfie",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_burgundy_gym_mirror.jpg"),
        "signatures": ["bordo spor takımım", "antrenman sonrası aynada kendime"],
        "caption": "Bordo spor takımım ve ben bugün salonda fırtına gibi estik! 🔥💪 Emek verilen her ter damlası fiziğime fazlasıyla değiyor. Bugün spora gidenler kimler bakalım? 😉👇",
        "alt_captions": [
            "Antrenman sonrası aynada kendime bakınca bütün yorgunluğum uçup gidiyor... 🍷✨ Bordo bana yakışmış mı aşklar, puanınız kaç? 🔥👇"
        ],
        "tags": "#fitness #gymgirl #bordotakım #fitbody #motivasyon #spor #canantuna #reels #mirrorselfie"
    },
    {
        "id": "ev_beyaz_triko_koltuk_keyfi",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_white_knit_couch.jpg"),
        "signatures": ["omzu açık beyaz trikom", "zümrüt koltuğuma kıvrıldım"],
        "caption": "Omzu açık beyaz trikom, sıcak çayım ve evimin huzuru... 🤍🍵 Dışarıdaki koşturmacadan kaçıp zümrüt koltuğuma kıvrıldım. Yanıma bir kahve alıp sohbete gelecek var mı? 😉✨",
        "alt_captions": [
            "Evde rahat ama şık olmayı sevenler kulübü! 🤍✨ Beyaz triko elbisemle akşam dinlenmesine geçtim, gününüz nasıl geçti canlar? 🌸👇"
        ],
        "tags": "#evhali #beyazelbise #triko #cozyvibes #zarafet #huzur #canantuna #lifestyle #reels"
    },
    {
        "id": "tatil_saks_mavisi_yat_gunbatimi",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_royal_blue_yacht_sunset.jpg"),
        "signatures": ["saks mavisi ve gün batımının", "güvertede rüzgarı dinlerken"],
        "caption": "Saks mavisi ve gün batımının büyüleyici uyumu... 💙🌅 Güvertede hafif esen rüzgarı dinlerken zaman dursun istedim. Mavinin bu tonunu benim kadar seven var mı? ✨👇",
        "alt_captions": [
            "Deniz üstünde batan güneşin verdiği o tatlı huzur... 🛥️💙 Arşivden içimi ısıtan en özel karelerden biri, nasıl buldunuz? 🌅👇"
        ],
        "tags": "#saksmavisi #günbatımı #yatturu #deniz #zarafet #summervibes #canantuna #reels"
    },
    {
        "id": "spor_cikolata_kahve_yoga_tulum",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_chocolate_brown_pilates.jpg"),
        "signatures": ["çikolata kahve tulumumla", "esneklik ve denge seansı"],
        "caption": "Çikolata kahve tulumumla esneklik ve denge seansı tamamlandı! 🍫🧘‍♀️ Vücudumu dinlendiren ve formda tutan en güzel saatler. Spor tulumumu nasıl buldunuz tatlım? ✨👇",
        "alt_captions": [
            "Matın üzerinde geçen her dakika bedenime ayrı bir enerji katıyor... 🤎💪 Kahve tonları bu sezon favorim, sizce nasıl durmuş? 👇"
        ],
        "tags": "#yoga #pilates #fitlife #kahvetonları #athleisure #esneklik #canantuna #reels"
    },
    {
        "id": "gece_siyah_saten_penthouse_balkon",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_black_satin_penthouse.jpg"),
        "signatures": ["siyah satenin asaleti", "penthouse terasında şehir"],
        "caption": "Siyah satenin asaleti ve ayaklarımın altında parlayan İstanbul gecesi... 🖤🍸 Penthouse terasında hafif müzik eşliğinde geceye başladık. Bu gece planlar ne bakalım? 😉✨",
        "alt_captions": [
            "Geceye siyah bir imza bırakalım... 🌃🖤 Şehir ışıkları mı daha parlak yoksa enerjimiz mi? Yorumları bekliyorum aşklar 👇"
        ],
        "tags": "#siyahsaten #geceşıklığı #istanbulgeceleri #penthouse #zarafet #canantuna #reels"
    },
    {
        "id": "sokak_haki_crop_etiler_yuruyus",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_olive_cargo_street.jpg"),
        "signatures": ["haki ve beyazın enerjisi", "etiler sokaklarında buzlu"],
        "caption": "Haki ve beyazın enerjisiyle Etiler sokaklarında buzlu kahve turu! 🌿☕ Hem spor hem çekici kombinleri günlük hayatta çok seviyorum. Tarzıma 10 üzerinden kaç veriyorsunuz? 😎👇",
        "alt_captions": [
            "Güneşli havayı yakalayınca sokaklara taşan enerji! 🍃🕶️ Bugünkü sokak stilimi beğendiniz mi canlar? 👇"
        ],
        "tags": "#sokakstili #etiler #bebek #kombin #streetfashion #ootd #canantuna #reels"
    },
    {
        "id": "ev_pembe_ipek_sabah_yatak_kahvalti",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_pink_silk_morning_bed.jpg"),
        "signatures": ["pudra pembesi ipek pijamam", "yatakta kruvasan ve latte"],
        "caption": "Pudra pembesi ipek pijamam, yatakta taze kruvasan ve latte keyfi... 🌸🥐 Bugün kendimi biraz şımartmaya karar verdim. Bana günaydın yok mu bakalım? 😉💕",
        "alt_captions": [
            "Sabah güneşinin odaya vurduğu en tatlı dakikalar... 💕☕ Güne böyle huzurlu başlamak gibisi yok, hepinize öpücükler! 🌸👇"
        ],
        "tags": "#günaydın #sabahkeyfi #ipekpijama #kahvaltı #evhali #canantuna #morningvibes #reels"
    },
    {
        "id": "gece_altin_payet_otel_daveti",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_gold_sequin_gala.jpg"),
        "signatures": ["şampanya altını ışıltısı", "avizelerin altında büyüleyici"],
        "caption": "Şampanya altını ışıltısı ve özel bir davet gecesi... ✨🥂 Avizelerin altında parlamayı seviyorum. Bu elbisenin sırt detayına bayıldım, sizce nasıl olmuş? 💛👇",
        "alt_captions": [
            "Özel gecelerde altın tonlarının yeri bende hep ayrı... 🌟🥂 Gözlerinizi alamadığınız o kare bu olsun mu? 😉👇"
        ],
        "tags": "#altınelbise #gala #gecedaveti #ışıltı #lüksyaşam #zarafet #canantuna #reels"
    },
    {
        "id": "ev_lavanta_hali_uzanma_keyfi",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_lavender_rug_stretch.jpg"),
        "signatures": ["lavanta takımım ve yumuşacık halı", "halıya uzanıp biraz mola"],
        "caption": "Esnetme hareketlerinden sonra yumuşacık halıya uzanıp biraz mola verdim... 💜✨ Lavanta takımım hem çok rahat hem de fiziği harika sarıyor. Kimler bugün tembellik modunda? 😉👇",
        "alt_captions": [
            "Evde antrenman biter, halı üstünde tatlı yorgunluk başlar! 💜🙈 Gözlerimin içine bakanlara selam olsun, gününüz nasıl geçiyor? 👇"
        ],
        "tags": "#lavanta #evsporu #fitgirl #halıkeyfi #çekicilik #motivasyon #canantuna #reels"
    },
    {
        "id": "sokak_kirmizi_trenckot_pastane",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_red_trench_rain_paris.jpg"),
        "signatures": ["kırmızı trençkotumla sokaklarda", "uzun çizmeler ve kırmızı"],
        "caption": "Kırmızı trençkotum ve uzun çizmelerimle sonbahar sokaklarında dikkatleri üzerimize çekelim biraz! ❤️👢 Serin havalarda koyu kırmızı giymeye bayılıyorum. Kombinim geçer not aldı mı? 🔥👇",
        "alt_captions": [
            "Butik pastane önünde kısa bir kahve molası... ❤️🥐 Kırmızı trençkot enerjisi diye bir gerçek var, katılıyor musunuz? 👇"
        ],
        "tags": "#kırmızıtrençkot #sonbaharmodası #çizmekombini #nişantaşı #tarz #canantuna #reels"
    },
    {
        "id": "tatil_turkuaz_havuz_sezlong",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_turquoise_poolside_lounger.jpg"),
        "signatures": ["turkuaz takımım ve palmiyeler", "şezlongda güneşin tadını"],
        "caption": "Turkuaz takımım, palmiyeler ve suyun verdiği o eşsiz dinginlik... 🩵🌴 Şezlongda uzanıp güneşin tadını çıkardığım anları hiçbir şeye değişmem. Turkuaz rengi bana yakışmış mı? ✨👇",
        "alt_captions": [
            "Sıcak bir tatil molası her zaman ruhu gençleştirir... 🌊🩵 Havuz başı stilime puanınız kaç aşklar? 👇"
        ],
        "tags": "#turkuaz #havuzbaşı #resortwear #tatilkeyfi #beachstyle #canantuna #reels"
    },
    {
        "id": "spor_antrasit_bisiklet_sahil_park",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_charcoal_cycling_park.jpg"),
        "signatures": ["bisikletimle sahil turu", "antrasit şort takımım"],
        "caption": "Güneşli havada bisikletimle sahil parkuru tamamlandı! 🚲🔥 Antrasit şort takımım ve bitmeyen enerjimle harika bir turdu. Benimle sahilde pedal çevirmeye var mısın? 😉👇",
        "alt_captions": [
            "Açık havada spor yapmanın tadı bambaşka! 🌿🚲 Bacak antrenmanını bugün sahilde bisikletle yaptık, nasıl görünüyor? 💪👇"
        ],
        "tags": "#bisiklet #sahilturu #bikershorts #fitlife #moda #enerji #canantuna #reels"
    },
    {
        "id": "lifestyle_terrakota_elbise_bahce_kafe",
        "category": "lifestyle",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_terracotta_pottery_cafe.jpg"),
        "signatures": ["tarçın rengi kruvaze elbisem", "çiçekli bahçe kafede"],
        "caption": "Tarçın rengi kruvaze elbisem ve çiçekler içinde huzurlu bir bahçe kafe... 🌺☕ Sıcak tonlar tenime çok uyuyor bence, siz ne dersiniz? Bir kahve ısmarlar mısınız bana? 😉🧡",
        "alt_captions": [
            "Begonvillerin altında buzlu latte ve tatlı bir tebessüm... 🧡🌸 Gününüz benimki kadar renkli geçsin canlar! 👇"
        ],
        "tags": "#kruvazeelbise #bahçekafe #tarçınrengi #zarafet #kahvekeyfi #canantuna #reels"
    },
    {
        "id": "lifestyle_lacivert_blazer_marina_yat_kulubu",
        "category": "is",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_navy_blazer_yacht_club.jpg"),
        "signatures": ["lacivert blazer ve beyaz", "marina yat kulübünde akşamüstü"],
        "caption": "Marina yat kulübünde akşamüstü buluşması... ⚓💙 Lacivert blazer ve beyaz kombininin o asil duruşuna bayılıyorum. Hem klasik hem çekici olmak tam benim tarzım! ✨👇",
        "alt_captions": [
            "Deniz kenarında şık bir akşamüstü toplantısı... 🛥️🤍 Lacivert-beyaz uyumu sizce de her zaman kazanmıyor mu? 👇"
        ],
        "tags": "#marina #yachtclub #blazer #oldmoney #şıklık #istanbul #canantuna #reels"
    },
    {
        "id": "ev_mint_yesili_mutfak_detoks_smoothie",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_mint_wellness_smoothie.jpg"),
        "signatures": ["mint yeşili spor takımım", "yeşil detoks smoothie"],
        "caption": "Mint yeşili spor takımım ve antrenman sonrası kendi ellerimle hazırladığım detoks smoothie! 🥑💚 Formumu korumak için mutfakta da disiplin şart. Sağlıklı beslenenler burada mı? ✨👇",
        "alt_captions": [
            "Sabah enerjisini yeşil içeceğimden, neşemi de sizden alıyorum! 💚🥤 Mint yeşili rengi nasıl buldunuz tatlım? 👇"
        ],
        "tags": "#smoothie #detoks #mintyeşili #sağlıklıyaşam #fitkitchen #canantuna #reels"
    },
    {
        "id": "gece_murver_mor_elbise_giyinme_odasi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_silver_mirror_dressing.jpg"),
        "signatures": ["mürdüm rengi kokteyl elbisem", "giyinme odasında son dokunuşlar"],
        "caption": "Giyinme odasında geceye hazırlanırken son dokunuşlar... 💜✨ Mürdüm rengi dar elbisem ve küpelerim hazır! Bakalım bu akşam nereye gidiyoruz, tahminleri alayım? 😉👠",
        "alt_captions": [
            "Ayna karşısında hazırlanmak benim için ayrı bir ritüel... 💄💜 Mürdüm tonu sizce de çok çekici değil mi? 👇"
        ],
        "tags": "#mürdüm #kokteylelbise #giyinmeodası #grwm #gecehazırlığı #canantuna #reels"
    },
    {
        "id": "is_gunbatimi_plaza_masasi",
        "category": "is",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_executive_sunset_desk.jpg"),
        "signatures": ["masamda gün batımı kahvesi", "yüksek katlardan şehri izlerken"],
        "caption": "Ofiste masamda gün batımı kahvesi ve yeni hedefler... ☕🌆 Yüksek katlardan şehri izlerken çalışmak bana ilham veriyor. İş çıkışı planlarınız hazır mı canlar? 💼✨",
        "alt_captions": [
            "Hem çalışkan hem bakımlı olmak bizim doğamızda var! 💼🌸 Günün yorgunluğunu bir kahveyle atıyoruz, sizde durumlar ne? 👇"
        ],
        "tags": "#ofisşıklığı #plaza #işkadını #günbatımı #motivasyon #canantuna #reels"
    },

    # --- 🏺 MEVCUT 44 SENARYO (TAM İMZA KORUMALI & YENİLENMİŞ ALTERNATİF AÇIKLAMALI) ---
    {
        "id": "hobi_seramik_atolyesi_heykel",
        "category": "sanat",
        "type": "video",
        "season": "all",
        "image_path": os.path.join(IMAGES_DIR, "canan_ceramics_studio.jpg"),
        "signatures": ["ellerim çamurlu ama ruhum", "seramik atölyesi molası"],
        "caption": "Ellerim çamurlu ama ruhum kuş gibi hafif... 🏺✨ Bugün kendime harika bir seramik atölyesi molası verdim. Kendi ellerinle çamura şekil vermek, sıfırdan bir şey yaratmak o kadar dinlendirici bir terapi ki! Siz en son kendiniz için ne zaman yeni bir şey denediniz? 🤍🌿",
        "tags": "#seramik #çömlek #atölye #hobi #sanat #ceramics #mindfulness #lifestyle #canantuna #reels"
    },
    {
        "id": "kis_uludag_dag_evi_kar",
        "category": "tatil",
        "type": "video",
        "season": "winter",
        "image_path": os.path.join(IMAGES_DIR, "canan_uludag_winter.jpg"),
        "signatures": ["uludağ'da ilk kar keyfi", "fincan sıcak çikolata gibisi yok"],
        "caption": "Uludağ'da ilk kar keyfi! ❄️☕ Beyazlar içinde sıcacık bir fincan sıcak çikolata gibisi yok... Dışarısı buz gibi ama ruhuma öyle iyi geldi ki anlatamam. Kış mevsimini ve kar tatilini sevenler kalpleri bıraksın! 🤍✨",
        "tags": "#uludağ #kartatili #kar #kışmodası #wintervibes #cozy #canantuna #reels #huzur"
    },
    {
        "id": "sonbahar_nisantasi_kahve_yuruyusu",
        "category": "sokak",
        "type": "video",
        "season": "autumn",
        "image_path": os.path.join(IMAGES_DIR, "canan_autumn_nisantasi.jpg"),
        "signatures": ["camel trençkot sezonunu", "sonbahar yaprakları, sıcak bir kahve"],
        "caption": "Sonbahar yaprakları, sıcak bir kahve ve Nişantaşı sokakları... 🍂☕ Camel trençkot sezonunu resmen açtım! Havalar hafif serinleyince sokak yürüyüşleri bana inanılmaz ilham veriyor. Sizin en sevdiğiniz sonbahar kombini ne? 🤎👇",
        "tags": "#nişantaşı #sonbahar #trençkot #sokakstili #kahvekeyfi #streetfashion #canantuna #reels #autumnvibes"
    },
    {
        "id": "gece_kirmizi_italyan_restoran",
        "category": "gece",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_red_dress_restaurant.jpg"),
        "signatures": ["kırmızı her kadının gardırobunda", "hafif italyan ezgileri"],
        "caption": "Kırmızı her kadının gardırobunda en az bir kere olmalı bence... ❤️✨ Mum ışığı, güzel bir akşam yemeği ve hafif İtalyan ezgileri. Kırmızı kombinimi nasıl buldunuz aşklar? 🍷👇",
        "tags": "#kırmızıelbise #gecedaveti #zarafet #dinner #italyan #lifestyle #canantuna #gününkaresi"
    },
    {
        "id": "is_zumrut_blazer_executive",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_emerald_blazer_office.jpg"),
        "signatures": ["zümrüt yeşili blazer'ımın", "yeni projeler, yeni toplantılar ve yüksek"],
        "caption": "Yeni projeler, yeni toplantılar ve yüksek hedefler! 💼💚 Zümrüt yeşili blazer'ımın verdiği özgüveni çok seviyorum. Kadın girişimciler ve iş kadınları burada mı? Gücünüzü gösterin! 🚀✨",
        "tags": "#businesswoman #blazer #kariyer #ofisstili #kombin #girişimci #canantuna #stil"
    },
    {
        "id": "sokak_alacati_sari_elbise",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_alacati_yellow_dress.jpg"),
        "signatures": ["alaçatı sokakları, pembe begonviller", "yazdan kalan sarı sıcak anlar"],
        "caption": "Begonviller, Alaçatı sokakları ve sarı keten elbisemin enerjisi... 🌸☀️ Soğuk günlerde bile içimi ısıtan en tatlı karelerden biri. En çok özlediğiniz tatil beldesi neresi? 💛👇",
        "tags": "#alaçatı #yazadönüş #tb #çeşme #sarıkombin #yazmodası #canantuna #enerji #reels"
    },
    {
        "id": "spor_lila_park_fitness",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_lilac_fitness_park.jpg"),
        "signatures": ["sabah koşusu ve park esnemesi", "lila spor takımımın enerjisine"],
        "caption": "Sabah koşusu ve park esnemesi tamamlandı! 💜🌿 Lila spor takımımın enerjisine bayıldım. Güne erken başlamak ve ter atmak gün boyu zinde tutuyor. Bugün kendiniz için ne yaptınız? 💪🔥",
        "tags": "#fitness #sabahsporu #lilatakım #gymgirl #motivasyon #sağlıklıyaşam #canantuna #reels"
    },
    {
        "id": "tatil_kapadokya_balonlar",
        "category": "tatil",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_cappadocia_terrace.jpg"),
        "signatures": ["kapadokya'da gün doğumu masal", "gökyüzündeki balonları izlerken"],
        "caption": "Kapadokya'da gün doğumu masal gibi... 🎈✨ Gökyüzündeki balonları izlerken sıcacık kahvemi yudumlamak bana inanılmaz bir huzur verdi. Hayatınızda mutlaka görmeniz gereken yerler listenize ekleyin derim! Siz Kapadokya'ya gittiniz mi aşklar? ☕🌅👇",
        "tags": "#kapadokya #cappadocia #gündoğumu #balon #seyahat #travelblogger #canantuna #huzur"
    },
    {
        "id": "sabah_bebek_kruvasan_kahve",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_bebek_cafe.jpg"),
        "signatures": ["sabah kahvesi ve taze kruvasan klasiği", "bebek sahilinde güne mis gibi"],
        "caption": "Sabah kahvesi ve taze kruvasan klasiği! 🥐☕ Bebek sahilinde güne mis gibi başladım. Tatlı krizine girenler burada mı? Kendinize güzel bir gün hediye edin aşklar 🌸💛",
        "tags": "#bebek #kahvekeyfi #kruvasan #günaydın #istanbul #lifestyle #canantuna #gününkaresi"
    },
    {
        "id": "tatil_ege_yat_turu",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_yacht_summer.jpg"),
        "signatures": ["rüzgar saçımda, masmavi deniz önümde", "ege'nin o masmavi sularında"],
        "caption": "Masmavi koylar ve deniz esintisi... 🌊🛥️ Bazen her şeyi geride bırakıp ufka doğru açılmak ruhu yeniliyor. Deniz tutkunları kimler bakalım? 💙👇",
        "tags": "#yazadönüş #throwback #tb #yatturu #deniz #tatil #yazözlemi #canantuna #reels #summervibes"
    },
    {
        "id": "gece_bogaz_cati_terasi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_rooftop_sunset.jpg"),
        "signatures": ["altın saatler (golden hour) ve boğaz", "gün batarken bu şehir bambaşka"],
        "caption": "Altın saatler (Golden hour) ve Boğaz manzarası... 🌇✨ Gün batarken bu şehir bambaşka bir büyüye bürünüyor. Akşam planınız ne canlar? 🍷❤️",
        "tags": "#goldenhour #günbatımı #istanbul #boğaz #rooftop #zarafet #canantuna #reels"
    },
    {
        "id": "tatil_bodrum_beach",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_bodrum_beach_1792678870147.jpg"),
        "signatures": ["deniz, güneş ve biraz kafa dinlemece", "bodrum bana her zaman çok iyi geliyor", "deniz mi havuz mu deseler"],
        "caption": "Bodrum'un o sıcak güneşi ve kumsalı... ☀️🌊 Deniz mi havuz mu deseler siz hangisini seçerdiniz? 🌊👇",
        "tags": "#yazadönüş #throwback #tb #bodrum #tatil #beachvibes #güneş #yaz #canantuna #reels"
    },
    {
        "id": "sokak_karakoy_yagmur",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_karakoy_street_portrait_1792678880948.jpg"),
        "signatures": ["yağmurda ıslanmayı seven kaç kişiyiz", "karaköy sokaklarında yürüyüş yapıp"],
        "caption": "Yağmurda ıslanmayı seven kaç kişiyiz? 🌧️🌂 Karaköy sokaklarında yürüyüş yapıp kahvemi aldım. Yağmurlu havalar bana inanılmaz ilham veriyor... ✨",
        "tags": "#karaköy #istanbul #yağmur #trenchcoat #sokakmodası #canantuna #lifestyle"
    },
    {
        "id": "spor_pilates_reformer",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_pilates_portrait_1792678899801.jpg"),
        "signatures": ["reformer seansı bitti, ter atıldı", "vücuduna iyi bakmak kendine yapabileceğin"],
        "caption": "Reformer seansı bitti, ter atıldı! 💪🧘‍♀️ Vücuduna iyi bakmak kendine yapabileceğin en büyük iyilik. Bugün spora vakit ayırdınız mı canlar? 🔥👇",
        "tags": "#pilates #reformer #fitgirl #spor #sağlıklıyaşam #canantuna #gymmotivation"
    },
    {
        "id": "gece_bogaz_aksam_yemegi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_bosphorus_night_1792678913579.jpg"),
        "signatures": ["istanbul geceleri ve boğaz'ın ışıkları", "bazen sadece durup bu şehrin tadını"],
        "caption": "İstanbul geceleri ve Boğaz'ın ışıkları... 🌉✨ Bazen sadece durup bu şehrin tadını çıkarmak gerekiyor. Akşamınız nasıl geçiyor aşklar? 🍷❤️",
        "tags": "#boğaz #istanbul #iyigeceler #şekerim #canantuna #gecehayatı #dinner"
    },
    {
        "id": "sokak_araba_selfie",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_driver_selfie_1792678924695.jpg"),
        "signatures": ["istanbul trafiği klasiği: kırmızı ışıkta", "şarkımı açtım enerjimi düşürmüyorum"],
        "caption": "İstanbul trafiği klasiği: Kırmızı ışıkta selfie çekilir! 🚗💨 Şarkımı açtım enerjimi düşürmüyorum. Trafikte olanlara sabırlar diliyorum 🙈🎧",
        "tags": "#istanbul #trafik #selfie #carselfie #gününkaresi #canantuna #enerji"
    },
    {
        "id": "ev_balkon_ciplak_ayak",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_cozy_balcony_portrait_1792678939456.jpg"),
        "signatures": ["balkonda sabah kahvesi, serin hava", "bütün gün böyle oturabilirim"],
        "caption": "Balkonda sabah kahvesi, serin hava ve sessizlik... ☕🌿 Bütün gün böyle oturabilirim. Güne güzel bir başlangıç yaptık, sizde durumlar ne? 🌸👇",
        "tags": "#günaydın #kahvekeyfi #huzur #evhali #balkonkeyfi #canantuna #gününkaresi"
    },
    {
        "id": "sokak_nisantasi_kafe",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tana_nisantasi_cafe_1792666291150.jpg"),
        "signatures": ["nişantaşı sokakları ve buz gibi bir filtre", "kombinimi nasıl buldunuz? 🕶️✨ nişantaşı'nda"],
        "caption": "Nişantaşı sokakları ve buz gibi bir filtre kahve... ☕🕶️ Enerjim tavan! Bugün kendiniz için ne yaptınız aşklar? 👇✨",
        "tags": "#nişantaşı #istanbul #kahvekeyfi #sokakmodası #canantuna #lifestyle"
    },
    {
        "id": "ev_sabah_kahvesi",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_morning_lifestyle_1792660779429.jpg"),
        "signatures": ["güne kahvesiz başlayamayanlar el kaldırsın", "bugünün mottosu: gülümse ve anı yaşa"],
        "caption": "Güne kahvesiz başlayamayanlar el kaldırsın! ☕☀️ Bugünün mottosu: Gülümse ve anı yaşa! Harika bir gün olsun hepimize 🌸💛",
        "tags": "#günaydın #sabahkahvesi #evhali #huzur #canantuna #pozitifenerji"
    },
    {
        "id": "sokak_kis_sicak_kahve",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_winter_street_1792666325312.jpg"),
        "signatures": ["hava buz gibi ama içimizi ısıtan", "kar görünce çocuk gibi sevinenler"],
        "caption": "Hava buz gibi ama içimizi ısıtan kahvemiz var ❄️☕ Karlı günlerde sokakta yürümek bana hep masal gibi gelir. Siz kış insanı mısınız? ☃️🤍",
        "tags": "#kış #kar #soğuk #kahvekeyfi #canantuna #wintervibes"
    },
    {
        "id": "spor_gym_ayna_selfie",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_fitness_selfie_1792663898849.jpg"),
        "signatures": ["bahane yok, disiplin var", "bugünkü bacak & kalça antrenmanı bitti"],
        "caption": "Bahane yok, disiplin var! 🔥💪 Bugünkü antrenmanı tamamladım. Aynadaki değişimi görmek en büyük motivasyonum! Siz başladınız mı? 🏋️‍♀️",
        "tags": "#fitness #gymmotivation #fitgirl #disiplin #spor #canantuna #workout"
    },
    {
        "id": "spor_sonrasi_hali_dinlenme",
        "category": "spor",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_post_workout_1792664056043.jpg"),
        "signatures": ["bacak gününden sonra halıya", "halıya serilenler derneği"],
        "caption": "Bacak gününden sonra halıya serilenler derneği başkanı seçildim sanırım! 🙈😂 Yorulduk ama değdi. Şimdi güzel bir dinlenme zamanı 💆‍♀️✨",
        "tags": "#postworkout #fitlife #dinlenme #yorgunluk #canantuna #gymgirl"
    },
    {
        "id": "ev_pazar_rahatligi",
        "category": "ev",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_cozy_livingroom_png_1792663231002.jpg"),
        "signatures": ["evde battaniye ve sıcak bir çay", "hiçbir şey yapmamak da ruhuna"],
        "caption": "Evde battaniye ve sıcak bir çay modundayım bugün... 🛋️📖 Bazen hiçbir şey yapmamak da ruhuna çok iyi gelir. Bugün evde misiniz dışarıda mı? 🍵👇",
        "tags": "#evkeyfi #huzur #cozyvibes #dinlenme #canantuna #haftasonu"
    },
    {
        "id": "ev_gunesli_balkon_selfie",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tuna_selfie_1792665280198.jpg"),
        "signatures": ["güneş açtıysa enerjimiz de yerine gelir", "yepyeni hedefler, güzel başlangıçlar"],
        "caption": "Güneş açtıysa enerjimiz de yerine gelir! ☀️🌸 Yepyeni hedefler, güzel başlangıçlar... Gününüz harika geçsin canlar! 💖✨",
        "tags": "#güneş #pozitifenerji #selfie #balkonkeyfi #canantuna #gününkaresi"
    },
    {
        "id": "lifestyle_vanity_mirror_makyaj",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_vanity_mirror.jpg"),
        "signatures": ["hazırlanırken aynaya bir bakış", "günün enerjisini yakalama anı"],
        "caption": "Hazırlanırken aynaya bir bakış ve günün enerjisini yakalama anı... ✨💄 Kendinize değer verdiğiniz her an çok kıymetli. Akşam planları yapıldı mı canlar? 💋👠",
        "tags": "#vanity #grwm #lifestyle #makyaj #güzellik #canantuna #mirrorselfie"
    },
    {
        "id": "spor_kortta_tenis_padel",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tennis_court.jpg"),
        "signatures": ["kortta maç bitti ama enerji hala tavan", "spor sadece bedenine değil ruhuna"],
        "caption": "Kortta maç bitti ama enerji hala tavan! 🎾🔥 Spor sadece bedenine değil ruhuna da iyi gelen en güzel terapi. Bugün hareket ettik mi? 💪✨",
        "tags": "#tennis #padel #tenis #fitgirl #sportystyle #canantuna #fitnessmotivation"
    },
    {
        "id": "tatil_sonsuzluk_havuzu_gunbatimi",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_infinity_pool.jpg"),
        "signatures": ["gün batımında sonsuzluğa karşı durup", "yazdan kalan sıcacık anlar", "güneşi böyle batırmayı özleyenler"],
        "caption": "Sonsuzluk havuzunda güneşi batırdığımız o huzurlu akşamüstü... 🌅🌊 Bir kahve alıp manzaraya karşı dalıp gitmeyi özleyenler kimler? ☕💛",
        "tags": "#tb #yazadönüş #sunset #infinitypool #tatil #yazözlemi #canantuna #travelgram #goldenhour #reels"
    },
    {
        "id": "kultur_cagdas_sanat_galerisi",
        "category": "sokak",
        "type": "photo",
        "image_path": os.path.join(IMAGES_DIR, "canan_art_gallery.jpg"),
        "signatures": ["sanatın içinde kaybolduğum", "renklerin hikayesini dinlediğim"],
        "caption": "Sanatın içinde kaybolduğum, renklerin hikayesini dinlediğim bir gün... 🎨🖼️ Modern sanat bana her zaman yeni bakış açıları kazandırıyor. Galerileri gezmeyi sevenler burda mı? 🤍✨",
        "tags": "#artgallery #sanat #istanbul #modernart #kultur #canantuna #streetstyle #ootd"
    },
    {
        "id": "hobi_somine_dag_evi",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_fireplace_chalet.jpg"),
        "signatures": ["dışarıda lapa lapa kar, içeride çıtırdayan", "çıtırdayan şömine ateşi"],
        "caption": "Dışarıda lapa lapa kar, içeride çıtırdayan şömine ateşi... ❄️🔥 Kışın en sevdiğim yanı bu sıcak sığınaklar. Bir fincan sıcak kahve ve huzur... Siz kış insanı mısınız yoksa yaz aşığı mı? Yorumlarda buluşalım! ☕✨",
        "tags": "#kış #şömine #dağevi #huzur #cozyvibes #canantuna #wintervibes #reels"
    },
    {
        "id": "sokak_bebek_sonbahar_yuruyusu",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_bebek_autumn_walk.jpg"),
        "signatures": ["bebek sahilinde hafif bir boğaz esintisi", "istanbul'un sonbaharı bana her zaman"],
        "caption": "Bebek sahilinde hafif bir Boğaz esintisi ve elimde sıcak kahvem... 🌊☕ İstanbul'un sonbaharı bana her zaman yeni kararlar ve taze umutlar getirir. Bugün kendinize bir iyilik yapıp yürüyüşe çıktınız mı canlar? 🍂💛",
        "tags": "#bebek #istanbul #boğaz #sonbahar #trenchcoat #sokakmodasıkombin #canantuna #lifestyle #reels"
    },
    {
        "id": "gece_mum_isiginda_aksam_yemegi",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_candlelight_dinner.jpg"),
        "signatures": ["istanbul ışıl ışıl ayaklarımızın altında", "kadehlerimizi güzelliklere ve hayallerimize"],
        "caption": "İstanbul ışıl ışıl ayaklarımızın altında... 🌃✨ Bazen sadece durmak, bu anın tadını çıkarmak ve iyi ki demek gerekir. Bu gece kadehlerimizi güzelliklere ve hayallerimize kaldırıyoruz! 🥂💙",
        "tags": "#istanbul #gece #rooftop #dinner #zarafet #canantuna #gecehayatı #reels"
    },
    {
        "id": "lifestyle_kitap_kafe_karakoy",
        "category": "lifestyle",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_bookstore_cafe.jpg"),
        "signatures": ["kitap kokusu, taze demlenmiş bir latte", "karaköy'ün bu huzurlu köşesinde"],
        "caption": "Kitap kokusu, taze demlenmiş bir latte ve yeni projeler... 📚☕ Karaköy'ün bu huzurlu köşesinde saatlerin nasıl geçtiğini anlamıyorum. Bu aralar hangi kitabı okuyorsunuz, bana öneriniz var mı? 📖💭",
        "tags": "#kitap #kafe #karaköy #lifestyle #kahvekeyfi #canantuna #bookstagram #reels"
    },
    {
        "id": "kis_uludag_kayak_zirve_teras",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_ski_terrace.jpg"),
        "signatures": ["zirvede hava tertemiz, güneş pırıl pırıl", "termostan sıcak çay içmenin keyfi"],
        "caption": "Zirvede hava tertemiz, güneş pırıl pırıl! ⛷️❄️ Karların üzerinde termostan sıcak çay içmenin keyfi hiçbir şeyde yok. Beyaz örtü bana inanılmaz enerji veriyor! Kayak yapmayı sevenler burada mı? 🏔️💙",
        "tags": "#uludağ #kayak #kıştatili #zirve #snow #kar #canantuna #travelgram #reels"
    },
    {
        "id": "ev_pazar_mutfak_granola",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_kitchen_morning.jpg"),
        "signatures": ["pazar sabahı mutfakta taze kahve kokusu", "renkli meyveler... 🍓☕ kendime vakit"],
        "caption": "Pazar sabahı mutfakta taze kahve kokusu ve renkli meyveler... 🍓☕ Kendime vakit ayırdığım en tatlı saatler. Güne nasıl başlarsanız öyle gider; gülümsemeyi unutmayın güzellikler! 🌸✨",
        "tags": "#pazarkahvaltısı #evhali #sağlıklıyaşam #mutfak #granola #canantuna #morningvibes #reels"
    },
    {
        "id": "lifestyle_termal_spa_dinlenme",
        "category": "lifestyle",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_spa_wellness.jpg"),
        "signatures": ["bütün haftanın yorgunluğunu geride bırakma", "sıcak su buharı ve bitki çayı"],
        "caption": "Bütün haftanın yorgunluğunu geride bırakma terapisi... 🧖‍♀️🌿 Sıcak su buharı ve bitki çayı ruhuma o kadar iyi geldi ki. Bedeninizi dinlendirmeyi ve şımartmayı ihmal etmeyin canlar! 💧✨",
        "tags": "#spa #wellness #kendinezamanayır #dinlenme #sağlık #canantuna #selfcare #reels"
    },
    {
        "id": "sokak_bogaz_koprusu_araba",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_car_bosphorus_bridge.jpg"),
        "signatures": ["köprüden geçerken güneş tam batış", "trafik bile olsa bu manzaraya değer"],
        "caption": "Köprüden geçerken güneş tam batış anında yüzüme vuruyor... 🚗🌅 En sevdiğim şarkı çalıyor ve İstanbul yine büyülemeye devam ediyor. Trafik bile olsa bu manzaraya değer! Sizde akşam nasıl geçiyor? 🎶💫",
        "tags": "#istanbul #boğazköprüsü #goldenhour #günbatımı #carvibes #canantuna #gününkaresi #reels"
    },
    {
        "id": "sokak_karakoy_mural_grafiti",
        "category": "sokak",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_karakoy_mural.jpg"),
        "signatures": ["karaköy sokaklarındaki bu renkli duvar", "duvar sanatı enerjimi ikiye katladı"],
        "caption": "Karaköy sokaklarındaki bu renkli duvar sanatı enerjimi ikiye katladı! 🎨☕ Sokak modasını ve canlı renkleri çok seviyorum. Günün kombini nasıl olmuş kızlar? Yorumları görelim! 💚👟",
        "tags": "#karaköy #sokakmodası #streetstyle #ootd #grafiti #canantuna #lifestyle #reels"
    },
    {
        "id": "is_levent_plaza_yonetim",
        "category": "is",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_executive_office.jpg"),
        "signatures": ["günün son toplantısı bitti ve arkamda", "parlayan levent silüeti"],
        "caption": "Günün son toplantısı bitti ve arkamda gün batımıyla parlayan Levent silüeti... 💼🌇 Disiplin ve vizyon bir araya gelince imkansız diye bir şey kalmıyor. Hayallerinizin peşini asla bırakmayın! 🚀🤍",
        "tags": "#business #işkadını #motivasyon #levent #başarı #canantuna #career #reels"
    },
    {
        "id": "tatil_ciragan_sarayi_kahvalti",
        "category": "tatil",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_ciragan_palace.jpg"),
        "signatures": ["çırağan sarayı'nın deniz kenarındaki", "boğaz'ın mavisi ve saray havası"],
        "caption": "Çırağan Sarayı'nın deniz kenarındaki terasında masalsı bir sabah... 🏰🌊 Boğaz'ın mavisi ve saray havası insanın ruhuna dokunuyor. İstanbul'da en sevdiğiniz tarihi mekan neresi? 💙✨",
        "tags": "#çırağansarayı #boğaz #istanbul #lüksyaşam #saray #canantuna #travel #reels"
    },
    {
        "id": "lifestyle_moda_sahil_gunbatimi",
        "category": "lifestyle",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_moda_sunset.jpg"),
        "signatures": ["moda sahilinde çimlere serilip", "anadolu yakasının bu dinginliğini"],
        "caption": "Moda sahilinde çimlere serilip gün batımını izlemek paha biçilemez... 🌅🍂 Akustik tınılar, serin rüzgar ve hafif sıcak bir çay. Anadolu yakasının bu dinginliğini çok seviyorum! 🧡🎶",
        "tags": "#moda #kadıköy #günbatımı #sahil #huzur #canantuna #akustik #reels"
    },
    {
        "id": "lifestyle_otel_lobi_orkide",
        "category": "lifestyle",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_hotel_lobby.jpg"),
        "signatures": ["zarafet detaylarda gizlidir", "dev orkideler ve sıcacık bir lobi"],
        "caption": "Zarafet detaylarda gizlidir... ☕🌸 Dev orkideler ve sıcacık bir lobi sohbeti. Kendinizi iyi hissettiren mekanlarda vakit geçirmek enerjinizi anında tazeliyor. Keyifli bir akşam olsun! 🤍✨",
        "tags": "#zarafet #lifestyle #lüks #otel #kahvesohbeti #canantuna #ootd #reels"
    },
    {
        "id": "ev_kis_pencere_sicak_cikolata",
        "category": "ev",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_winter_window.jpg"),
        "signatures": ["camın kenarına kıvrılıp yağan karı", "bol köpüklü sıcak çikolata"],
        "caption": "Camın kenarına kıvrılıp yağan karı izlemek ve elinde bol köpüklü sıcak çikolata... 🍫❄️ Peri masalı gibi bir akşam. Kış akşamlarının bu tatlı nostaljisini kimler seviyor? 🕯️🤍",
        "tags": "#kışakşamı #sıcakçikolata #evkeyfi #nostalji #kar #canantuna #cozynight #reels"
    },
    {
        "id": "spor_kort_tenis_mola",
        "category": "spor",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_tennis_bench.jpg"),
        "signatures": ["tenis maçında son set bitti", "ter su içindeyiz ama mutluluk"],
        "caption": "Tenis maçında son set bitti, ter su içindeyiz ama mutluluk paha biçilemez! 🎾💪 Spor yapmak günün tüm stresini silip süpürüyor. Bugün hareket ettiniz mi canlar? Haydi harekete geçin! 🔥👟",
        "tags": "#tenis #kort #fitgirl #sporaşkı #motivasyon #canantuna #workout #reels"
    },
    {
        "id": "gece_galata_kulesi_sokak",
        "category": "gece",
        "type": "video",
        "image_path": os.path.join(IMAGES_DIR, "canan_galata_night.jpg"),
        "signatures": ["galata sokaklarında akşam yürüyüşü", "arkamda asırların şahidi kule"],
        "caption": "Galata sokaklarında akşam yürüyüşü ve arkamda asırların şahidi kule... 🗼🌙 Taş sokakların tarihi kokusu büyüleyici. Galata'ya her geldiğimde ilk kez görüyormuş gibi aşık oluyorum! 🖤✨",
        "tags": "#galata #galatakulesi #istanbulgeceleri #tarih #geceyürüyüşü #canantuna #reels"
    }
]


def get_scenario_by_id(scenario_id: str) -> dict:
    for s in SCENARIOS:
        if s["id"] == scenario_id:
            return s
    return SCENARIOS[0]
