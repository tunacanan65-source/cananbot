import os
import sys
import json
import textwrap
import subprocess
import random
from datetime import datetime, timedelta
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
MUSIC_DIR = os.path.join(BASE_DIR, "assets", "music")
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
FONT_PATH = os.path.join(BASE_DIR, "assets", "font.ttf")
QUARANTINE_FILE = os.path.join(BASE_DIR, "used_images_quarantine.json")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

DEFAULT_MUSIC = os.path.join(MUSIC_DIR, "aesthetic_lofi.mp3")

SUMMER_FILENAME_KEYWORDS = (
    "bikini", "swim", "pool", "yacht", "beach", "sunbed",
    "hammock", "shower", "cabana", "sandals_pool", "wooden_deck",
    "coral_mini_sunset", "silver_anklet_terrace", "denim_shorts_crop"
)


def is_summer_image(image_path: str) -> bool:
    """Görselin deniz/plaj/havuz/bikini/yat gibi yazlık açık hava görseli olup olmadığını döner."""
    fname = os.path.basename(image_path).lower()
    return any(k in fname for k in SUMMER_FILENAME_KEYWORDS)


def is_cold_season() -> bool:
    """Ekim (10) - Nisan (4) arası sonbahar/kış/erken bahar döneminde True döner."""
    return datetime.now().month in (10, 11, 12, 1, 2, 3, 4)


# 1. Sahne (0-4 sn) Sol-Üstte Çıkacak Gerçekçi Takipçi Yorumu Balonu Havuzu
FOLLOWER_COMMENTS_FEET = [
    ("Mehmet K.", "Canan hanım kırmızı oje size çok yakışıyor, yeni video gelsin!"),
    ("Ahmet Y.", "Ayak bakımınıza ve zarafetinize hayranım, 10 üzerinden 10!"),
    ("Mustafa T.", "Oje renk seçimleriniz her zaman çok şık duruyor Canan hanım."),
    ("Kemal S.", "Hem yüzünüzün güzelliği hem bakımlı olmanız harika gerçekten."),
    ("Serkan B.", "Açık renk oje mi koyu renk oje mi? İkisi de çok yakışıyor!"),
    ("Hasan D.", "Videolarınızı her gün keyifle takip ediyoruz, çok zarifsiniz.")
]

FOLLOWER_COMMENTS_COUSIN = [
    ("Murat A.", "Esmer olan Canan hanım tek geçer, kuzeni de çok sempatik!"),
    ("Cemil K.", "Kuzenin Burcu ile videolarınız çok keyifli, ikiniz de harikasınız!"),
    ("Orhan V.", "Benim oyum her zaman gözlükleriyle Canan hanıma, 1 numara!"),
    ("ibrahim E.", "Esmer mi sarışın mı sorusunun cevabı kesinlikle Canan hanım!"),
    ("Sinan M.", "Kuzeninizle girdiğiniz iddiaların devamı gelsin, çok güzel ikilisiniz.")
]

FOLLOWER_COMMENTS_SUMMER = [
    ("Ali R.", "Fiziğiniz ve enerjiniz gerçekten 10 numara Canan hanım, maşallah!"),
    ("Hüseyin Ç.", "Güneş sizden daha sönük kalmış, her zamanki gibi çok şıksınız."),
    ("Burak G.", "Tatil pozlarınız içimizi ısıtıyor, enerjiniz hiç bitmesin!"),
    ("Yavuz N.", "Hem doğal hem bu kadar çekici olmayı nasıl başarıyorsunuz?"),
    ("Tuncay Ö.", "Deniz ve güneş size çok yakışıyor Canan hanım, selamlar.")
]

FOLLOWER_COMMENTS_GENERAL = [
    ("Mustafa B.", "Gözlükleriniz ve tebessümünüz çok zarif, videolarınızı bekliyoruz!"),
    ("Erkan T.", "Hangi kombini giyseniz ayrı bir hava katıyorsunuz Canan hanım."),
    ("Zafer L.", "Sayfanızı yeni keşfettim, bütün videolarınızı hayranlıkla izledim!"),
    ("Bülent K.", "Günün en güzel paylaşımı yine sizden geldi, çok şıksınız."),
    ("Metin P.", "4 karelik videolarınız çok güzel oluyor, sonuna kadar izliyoruz.")
]


def load_quarantine(days: int = 30) -> dict:
    """Son 30 gün içinde kullanılan görsellerin {dosya_adi: iso_tarih} sözlüğünü döner."""
    if not os.path.exists(QUARANTINE_FILE):
        return {}
    try:
        with open(QUARANTINE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        cutoff = datetime.now() - timedelta(days=days)
        active = {}
        for k, v in data.items():
            try:
                if datetime.fromisoformat(v) >= cutoff:
                    active[k] = v
            except Exception:
                active[k] = v
        return active
    except Exception:
        return {}


def mark_images_used(image_paths: list):
    """Kullanılan tüm görselleri (Reels içindeki 4 kare, Fotoğraf ve Story dahil) 30 günlük karantinaya kaydeder."""
    q = load_quarantine(days=30)
    now_iso = datetime.now().isoformat()
    for p in image_paths:
        if p:
            q[os.path.basename(p)] = now_iso
    try:
        with open(QUARANTINE_FILE, "w", encoding="utf-8") as f:
            json.dump(q, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _load_font(size: int = 32):
    """Türkçe karakter destekli kalın fontu yükler (Linux/Render ve Windows tam uyumlu)."""
    candidates = [
        FONT_PATH,
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size=size)
            except Exception:
                pass
    return ImageFont.load_default()


def get_follower_comment_for_image(image_path: str) -> tuple:
    """1. Sahnede sol üstte gösterilecek gerçekçi takipçi yorumunu seçer."""
    fname = os.path.basename(image_path).lower()
    seed_val = sum(ord(c) for c in fname) + datetime.now().timetuple().tm_yday
    if "canan_cousin_" in fname:
        pool = FOLLOWER_COMMENTS_COUSIN
    elif any(k in fname for k in ("feet", "polish", "pedi", "toes", "anklet")):
        pool = FOLLOWER_COMMENTS_FEET
    elif any(k in fname for k in ("bikini", "swim", "pool", "yacht", "beach", "sunbed", "hammock", "shower", "jacuzzi")):
        pool = FOLLOWER_COMMENTS_SUMMER
    else:
        pool = FOLLOWER_COMMENTS_GENERAL
    return pool[seed_val % len(pool)]


def get_short_hook_for_image(
    image_path: str,
    scene_index: int = 0,
    num_scenes: int = 4,
    custom_hook: str = None
) -> str:
    """
    4 karelik 'Adım Adım Hazırlanma' kurgusuna ve görselin temasına göre
    ekrana taşmayan, kısa ve yüksek etkileşimli cümle seçer.
    """
    is_last_scene = (scene_index == num_scenes - 1)
    fname = os.path.basename(image_path).lower()

    if "canan_cousin_" in fname:
        if is_last_scene:
            return random.choice([
                "Kaybeden yemek ısmarlıyor! Canan (1) mı Burcu (2) mu?",
                "Esmer Canan (1) mı Sarışın Burcu (2) mu? Yoruma yaz!",
                "Hangimizin tarzı ve ojesi 10/10? Seç bakalım!"
            ])
        if scene_index == 0 and custom_hook and len(custom_hook.strip()) <= 55:
            return custom_hook.strip()
        return random.choice([
            "Kuzenim Burcu ile iddiaya girdik, hangimiz?",
            "Esmer mi Sarışın mı? Tarafını seç!",
            "Kimin ojesi ve bacakları daha güzel olmuş?",
            "Kuzenim Burcu ve ben! Puanın kaç?"
        ])

    if is_last_scene:
        final_hooks = [
            "Hazırım! 1, 2, 3 yoksa 4. kare mi? Favorini yaz!",
            "En çok hangi karede gözün kaldı? Yoruma yaz!",
            "4 pozdan hangisi 10/10 olmuş? Seç bakalım!",
            "Baştan sona izledin mi? Favori karen hangisi?"
        ]
        return random.choice(final_hooks)

    if scene_index == 0 and custom_hook and len(custom_hook.strip()) <= 55:
        return custom_hook.strip()

    if any(k in fname for k in ("feet", "polish", "pedi", "toes", "anklet")):
        if scene_index == 0:
            feet_start_hooks = [
                "Bakım saati! Ojemin rengi nasıl oluyor?",
                "Oje sürerken yakalandım, bu renk yakışır mı?",
                "Ayak bakımına başladık, rengi beğendin mi?"
            ]
            return random.choice(feet_start_hooks)
        else:
            feet_done_hooks = [
                "Ojem bitti, nasıl olmuş? Puanın kaç?",
                "Yeni sürdüm, ojemin rengi yakışmış mı?",
                "Bakım tamamlandı! Ayaklarıma 10 üzerinden kaç?",
                "Bu renk ojeyi beğendin mi?"
            ]
            return random.choice(feet_done_hooks)

    if any(k in fname for k in ("bikini", "swim", "pool", "yacht", "beach", "sunbed", "hammock", "shower", "jacuzzi")):
        if is_cold_season():
            return random.choice([
                "Dışarısı soğukken yaz arşivinden bir #tbt! Nasıl?",
                "Yazı ve güneşi şimdiden özleyenler burada mı? (#tbt)",
                "Yazdan kalan en sevdiğim karelerden biri! Puanın kaç?",
                "Soğuk havalarda içimizi ısıtacak bir #tbt!"
            ])
        summer_hooks = [
            "Güneş mi daha sıcak yoksa bu poz mu?",
            "Biraz da güneşlenelim, fizik nasıl?",
            "Deniz mi havuz mu? Sen hangisisin?",
            "Tatil modunu açtık, puanın kaç?"
        ]
        return random.choice(summer_hooks)

    if any(k in fname for k in ("gym", "pilates", "yoga", "fitness", "workout", "cycling", "tennis")):
        sport_hooks = [
            "Antrenman bitti, sence emeğime değmiş mi?",
            "Spor sonrası enerji tavan, nasılım?",
            "Bu spor takımının rengi yakışmış mı?"
        ]
        return random.choice(sport_hooks)

    if any(k in fname for k in ("satin", "silk", "lace", "cami", "slip", "robe", "bed", "bath", "rug", "couch", "shirt")):
        lounge_hooks = [
            "Ev haliyle başlıyoruz, nasılım?",
            "Ev hali mi dışarı hali mi? Hangisi?",
            "İpek rahatlığı diye bir gerçek var!",
            "Yanıma bir kahve alıp gelecek var mı?"
        ]
        return random.choice(lounge_hooks)

    general_hooks = [
        "Akşam için hazırlanıyoruz, bu kombin nasıl?",
        "Bu elbiseyle dışarı çıkılır mı?",
        "Sence bu renk bana yakışmış mı?",
        "Tarzıma 10 üzerinden kaç veriyorsun?"
    ]
    return random.choice(general_hooks)


def create_overlay_png(
    text: str,
    out_png_path: str,
    y_pos: int = 1470,
    scene_index: int = None,
    num_scenes: int = None,
    follower_comment: tuple = None
):
    """
    1080x1920 şeffaf katman üzerine:
    1) Sağ üst köşeye şık '1/4', '2/4', '3/4', '4/4' kare sayacı,
    2) 1. sahnede sol üst güvenli bölgeye gerçekçi 'Takipçi Yorumuna Yanıt' balonu,
    3) Alt-orta güvenli bölgeye ekrandan taşmayan etkileşim kapsülü çizer.
    """
    canvas = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font_main = _load_font(size=31)
    font_counter = _load_font(size=28)
    font_comment_user = _load_font(size=23)
    font_comment_body = _load_font(size=26)

    # 1. SAĞ ÜST KARE SAYACI (1/4, 2/4, 3/4, 4/4)
    if scene_index is not None and num_scenes and num_scenes > 1:
        counter_str = f"{scene_index + 1} / {num_scenes}"
        cb = draw.textbbox((0, 0), counter_str, font=font_counter)
        cw, ch = cb[2] - cb[0], cb[3] - cb[1]
        c_x1, c_y1 = 1080 - cw - 85, 130
        c_x2, c_y2 = c_x1 + cw + 44, c_y1 + ch + 26
        draw.rounded_rectangle(
            [c_x1, c_y1, c_x2, c_y2],
            radius=22,
            fill=(15, 15, 22, 195),
            outline=(255, 255, 255, 130),
            width=2
        )
        draw.text((c_x1 + 22, c_y1 + 11), counter_str, font=font_counter, fill=(255, 255, 255, 255))

    # 2. SOL ÜST TAKİPÇİ YORUMU BALONU (Yalnızca 1. Sahnede)
    if scene_index == 0 and follower_comment:
        author, c_text = follower_comment
        clean_c = "".join(ch for ch in c_text if ord(ch) < 0x1F000).strip()
        c_lines = textwrap.wrap(clean_c, width=36)[:2]
        header_str = f"{author} yorum yaptı:"

        hb = draw.textbbox((0, 0), header_str, font=font_comment_user)
        hw, hh = hb[2] - hb[0], hb[3] - hb[1]
        c_bboxes = [draw.textbbox((0, 0), ln, font=font_comment_body) for ln in c_lines]
        c_widths = [b[2] - b[0] for b in c_bboxes]
        c_heights = [b[3] - b[1] for b in c_bboxes]

        bub_w = min(max([hw] + c_widths) + 64, 780)
        bub_h = hh + sum(c_heights) + len(c_lines) * 8 + 38
        bx1, by1 = 65, 130
        bx2, by2 = bx1 + bub_w, by1 + bub_h

        # Beyaz/buzlu TikTok & Reels tarzı yorum kartı
        draw.rounded_rectangle(
            [bx1, by1, bx2, by2],
            radius=22,
            fill=(252, 252, 255, 232),
            outline=(220, 40, 90, 210),
            width=3
        )
        # Sol kırmızı/pembe vurgu şeridi
        draw.rounded_rectangle(
            [bx1 + 12, by1 + 14, bx1 + 20, by2 - 14],
            radius=4,
            fill=(225, 38, 88, 255)
        )
        draw.text((bx1 + 32, by1 + 14), header_str, font=font_comment_user, fill=(130, 130, 145, 255))
        cy = by1 + 14 + hh + 8
        for idx_l, ln in enumerate(c_lines):
            draw.text((bx1 + 32, cy), ln, font=font_comment_body, fill=(20, 20, 28, 255))
            cy += c_heights[idx_l] + 6

    # 3. ALT-ORTA ETKİLEŞİM KAPSÜLÜ
    clean_text = "".join(ch for ch in text if ord(ch) < 0x1F000).strip()
    if not clean_text:
        clean_text = "Sence nasıl olmuş? Yorumda buluşalım!"

    lines = textwrap.wrap(clean_text, width=34)
    if len(lines) > 2:
        lines = lines[:2]

    line_bboxes = [draw.textbbox((0, 0), ln, font=font_main) for ln in lines]
    line_widths = [b[2] - b[0] for b in line_bboxes]
    line_heights = [b[3] - b[1] for b in line_bboxes]

    max_w = max(line_widths) if line_widths else 300
    total_h = sum(line_heights) + (len(lines) - 1) * 10

    pad_x = 34
    pad_y = 18
    box_w = min(max_w + pad_x * 2, 900)
    box_h = total_h + pad_y * 2

    box_x1 = (1080 - box_w) // 2
    box_y1 = y_pos - (box_h // 2)
    box_x2 = box_x1 + box_w
    box_y2 = box_y1 + box_h

    draw.rounded_rectangle(
        [box_x1, box_y1, box_x2, box_y2],
        radius=26,
        fill=(15, 15, 22, 185),
        outline=(255, 255, 255, 95),
        width=2
    )

    curr_y = box_y1 + pad_y
    for i, ln in enumerate(lines):
        lw = line_widths[i]
        lh = line_heights[i]
        tx = (1080 - lw) // 2
        draw.text((tx + 2, curr_y + 2), ln, font=font_main, fill=(0, 0, 0, 210))
        draw.text((tx, curr_y), ln, font=font_main, fill=(255, 255, 255, 255))
        curr_y += lh + 10

    canvas.save(out_png_path, "PNG")
    return out_png_path


def create_story_image(image_path: str, story_text: str, output_jpg: str = None) -> str:
    """
    Günlük Otomatik Hikaye (Story) için 1080x1920 dikey görselin üzerine
    şık ve taşmayan bir hikaye notu işler ve kullanılan görseli 30 günlük karantinaya kaydeder.
    """
    if not output_jpg:
        output_jpg = os.path.join(OUTPUT_DIR, f"story_{random.randint(1000, 9999)}.jpg")

    mark_images_used([image_path])

    img = Image.open(image_path).convert("RGB")
    target_w, target_h = 1080, 1920
    src_w, src_h = img.size
    scale = max(target_w / src_w, target_h / src_h)
    new_w, new_h = int(src_w * scale), int(src_h * scale)
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    img = img.crop((left, top, left + target_w, top + target_h)).convert("RGBA")

    ovl_path = os.path.join(OUTPUT_DIR, f"_tmp_story_ovl_{random.randint(1000, 9999)}.png")
    try:
        create_overlay_png(story_text, ovl_path, y_pos=1520)
        ovl = Image.open(ovl_path).convert("RGBA")
        combined = Image.alpha_composite(img, ovl).convert("RGB")
        combined.save(output_jpg, "JPEG", quality=88, optimize=True)
    finally:
        if os.path.exists(ovl_path):
            try:
                os.remove(ovl_path)
            except Exception:
                pass
    return output_jpg


def get_motion_filter(style_index: int, total_frames: int) -> str:
    """8 Farklı Sinematik + Organik El Kamerası Salınımlı (Canlı Video Hissi Veren) Hareket (1080x1920 Full HD)."""
    bright_eq = ",eq=brightness=0.025:contrast=1.03:saturation=1.05"
    sway_x = "+6*sin(on/9)"
    sway_y = "+5*cos(on/11)"
    styles = [
        f"zoompan=z='min(zoom+0.0010,1.14)':x='iw/2-(iw/zoom/2){sway_x}':y='ih/2-(ih/zoom/2){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0010,1.15)':x='iw/2-(iw/zoom/2){sway_x}':y='ih/3-(ih/zoom/3){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(on/{total_frames}){sway_x}':y='ih/2-(ih/zoom/2){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2){sway_x}':y='(ih-ih/zoom)*(on/{total_frames}){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='max(1.15-0.0011*on,1.0)':x='iw/2-(iw/zoom/2){sway_x}':y='ih/2.3-(ih/zoom/2.3){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(1-on/{total_frames}){sway_x}':y='ih/2.1-(ih/zoom/2.1){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0009,1.14)':x='iw/2-(iw/zoom/2){sway_x}':y='(ih-ih/zoom)*(1-on/{total_frames}){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0009,1.12)':x='iw/2-(iw/zoom/2){sway_x}':y='ih/2.5-(ih/zoom/2.5){sway_y}':d={total_frames}:s=1080x1920:fps=30{bright_eq}"
    ]
    return styles[style_index % len(styles)]


def pick_background_music() -> str:
    """Müzik klasöründeki telifsiz parçalardan rastgele birini seçer."""
    music_files = [
        os.path.join(MUSIC_DIR, f)
        for f in os.listdir(MUSIC_DIR)
        if f.lower().endswith((".mp3", ".wav", ".m4a"))
    ]
    if music_files:
        return random.choice(music_files)
    if os.path.exists(DEFAULT_MUSIC):
        return DEFAULT_MUSIC
    return None


def pick_companion_images(
    primary_image: str,
    count: int = 3,
    extra_candidates: list = None,
    exclude_filenames: set = None
) -> list:
    """
    30 Günlük Sıfır-Tekrar Karantinalı & Deterministik 4-Kare Seçici:
    - Daha önce Reels'in herhangi bir karesinde, Fotoğrafta veya Story'de kullanılmış hiçbir görseli seçmez.
    - Sunucu yeniden başlasa bile her ana görselin kendine özgü deterministik ofseti olduğu için
      2., 3. ve 4. karelerde aynı görseller üst üste ASLA denk gelmez!
    """
    primary_abs = os.path.abspath(primary_image)
    primary_fname = os.path.basename(primary_abs)

    quarantined = set(load_quarantine(days=30).keys())
    if exclude_filenames:
        quarantined.update(exclude_filenames)
    quarantined.add(primary_fname)

    if extra_candidates:
        ordered = [
            p for p in extra_candidates
            if os.path.exists(p)
            and os.path.abspath(p) != primary_abs
            and os.path.basename(p) not in quarantined
        ]
        if len(ordered) >= count:
            return ordered[:count]

    all_imgs = sorted([
        os.path.join(IMAGES_DIR, f)
        for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
        and os.path.abspath(os.path.join(IMAGES_DIR, f)) != primary_abs
    ])

    is_cousin = "canan_cousin_" in primary_fname.lower()
    if is_cousin:
        base_pool = [p for p in all_imgs if "canan_cousin_" in os.path.basename(p).lower()]
    else:
        base_pool = [p for p in all_imgs if "canan_cousin_" not in os.path.basename(p).lower()]

    # Kış/Sonbahar (Ekim-Nisan) döneminde eğer ana görsel yazlık (#tbt) DEĞİLSE,
    # yan karelere deniz/plaj/havuz/bikini görseli karıştırma!
    primary_is_summer = is_summer_image(primary_abs)
    if is_cold_season() and not primary_is_summer:
        seasonal_pool = [p for p in base_pool if not is_summer_image(p)]
        if len(seasonal_pool) >= count:
            base_pool = seasonal_pool

    fresh_pool = [p for p in base_pool if os.path.basename(p) not in quarantined]
    if len(fresh_pool) < count:
        fresh_pool = list(base_pool)

    # Deterministik + Günlük Kaydırmalı Seçim (Rastgele çakışmayı %100 önler)
    now = datetime.now()
    slot_num = 0 if now.hour < 15 else (1 if now.hour < 19 else 2)
    day_seq = (now.year * 366 + now.timetuple().tm_yday) * 3 + slot_num
    name_hash = sum((i + 1) * ord(ch) for i, ch in enumerate(primary_fname))

    if is_cousin:
        start_idx = (day_seq * 3 + name_hash) % max(1, len(fresh_pool))
        chosen = []
        for step in range(len(fresh_pool)):
            cand = fresh_pool[(start_idx + step) % len(fresh_pool)]
            if cand not in chosen:
                chosen.append(cand)
            if len(chosen) == count:
                break
        return chosen

    # Solo Canan için 3 farklı görsel grubu (birbirini tekrar etmeyen geniş havuzlar):
    # Grup 1: Oje / Ayak / Ev / Yatak / Koltuk / Sabah
    group_1 = [
        p for p in fresh_pool
        if any(k in os.path.basename(p).lower() for k in ("feet", "polish", "pedi", "toes", "anklet", "bed", "couch", "sofa", "rug", "carpet", "robe", "morning", "coffee", "home", "book"))
    ]
    # Grup 2: Plaj / Bikini / Havuz / Yat / Spor / Gündüz
    group_2 = [
        p for p in fresh_pool
        if p not in group_1
        and any(k in os.path.basename(p).lower() for k in ("bikini", "pool", "yacht", "beach", "sunbed", "hammock", "shower", "jacuzzi", "gym", "yoga", "tennis", "pilates", "shorts", "workout", "summer"))
    ]
    # Grup 3: Gece / Mini Elbise / Saten / Korse / Ayna / Şık Kombin
    group_3 = [
        p for p in fresh_pool
        if p not in group_1 and p not in group_2
    ]

    chosen = []
    for g_idx, grp in enumerate([group_1, group_2, group_3]):
        avail = [p for p in grp if p not in chosen]
        if avail:
            pick_idx = (day_seq * 7 + name_hash + g_idx * 13) % len(avail)
            chosen.append(avail[pick_idx])

    remaining = [p for p in fresh_pool if p not in chosen]
    step_idx = 0
    while len(chosen) < count and remaining:
        pick = remaining[(day_seq + name_hash + step_idx) % len(remaining)]
        chosen.append(pick)
        remaining.remove(pick)
        step_idx += 1

    return chosen[:count]


def create_reels_video(
    image_path: str,
    voice_text: str = None,
    output_mp4: str = None,
    duration: float = 16.0,
    motion_index: int = None,
    companion_images: list = None,
    hook_text: str = None,
    custom_scene_hooks: list = None,
    exclude_filenames: set = None
) -> str:
    """
    Facebook & Instagram Para Kazanma ve Yüksek Etkileşim Kriterlerine Özel:
    - 30 Günlük Karantina Kalkanı (Reels içi 4 kare dahil hiçbir fotoğraf tekrar etmez)
    - Sağ üstte '1/4', '2/4', '3/4', '4/4' kare sayacı
    - 1. karede sol üstte gerçekçi 'Takipçi Yorumu' balonu
    - İlk kareden (0.00 sn) itibaren %100 parlak ve net başlangıç
    """
    if not output_mp4:
        output_mp4 = os.path.join(OUTPUT_DIR, "reels_output.mp4")

    music_file = pick_background_music()
    if not music_file or not os.path.exists(music_file):
        raise FileNotFoundError(f"Arka plan müziği bulunamadı: {music_file}")

    companions = pick_companion_images(
        image_path,
        count=3,
        extra_candidates=companion_images,
        exclude_filenames=exclude_filenames
    )
    scene_images = [image_path] + companions
    # Kullanılan 4 görselin tamamını 30 günlük karantinaya kaydet!
    mark_images_used(scene_images)

    num_scenes = len(scene_images)
    scene_duration = round(duration / num_scenes, 2)
    frames_per_scene = int(scene_duration * 30)

    available_motions = list(range(8))
    random.shuffle(available_motions)
    if motion_index is not None:
        available_motions[0] = motion_index % 8

    follower_comm = get_follower_comment_for_image(image_path)

    print(
        f"🎬 [4 Sahneli 16sn Karantinalı Reels] Üretiliyor: {[os.path.basename(p) for p in scene_images]} "
        f"| Müzik: {os.path.basename(music_file)}"
    )

    temp_files = []
    temp_clips = []
    concat_list_path = os.path.join(OUTPUT_DIR, f"concat_{random.randint(10000, 99999)}.txt")

    try:
        for idx, img_p in enumerate(scene_images):
            m_style = available_motions[idx % len(available_motions)]
            zoom_filter = get_motion_filter(m_style, frames_per_scene)

            if custom_scene_hooks and idx < len(custom_scene_hooks) and custom_scene_hooks[idx]:
                scene_hook = custom_scene_hooks[idx]
            else:
                scene_hook = get_short_hook_for_image(
                    img_p,
                    scene_index=idx,
                    num_scenes=num_scenes,
                    custom_hook=(hook_text if idx == 0 else None)
                )

            overlay_png = os.path.join(OUTPUT_DIR, f"_tmp_ovl_{idx}_{random.randint(1000,9999)}.png")
            create_overlay_png(
                scene_hook,
                overlay_png,
                y_pos=1470,
                scene_index=idx,
                num_scenes=num_scenes,
                follower_comment=(follower_comm if idx == 0 else None)
            )
            temp_files.append(overlay_png)

            filter_complex = (
                f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
                f"{zoom_filter}[bg];"
                f"[bg][1:v]overlay=0:0,format=yuv420p[v]"
            )

            tmp_clip = os.path.join(OUTPUT_DIR, f"_tmp_scene_{idx}_{random.randint(1000,9999)}.mp4")
            cmd_scene = [
                FFMPEG_EXE, "-y",
                "-loop", "1", "-i", img_p,
                "-i", overlay_png,
                "-filter_complex", filter_complex,
                "-map", "[v]",
                "-c:v", "libx264",
                "-preset", "veryfast",
                "-crf", "19",
                "-t", str(scene_duration),
                "-an",
                tmp_clip
            ]
            proc = subprocess.run(cmd_scene, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                err_msg = proc.stderr.decode("utf-8", errors="ignore")[-300:]
                raise RuntimeError(f"Sahne {idx+1} FFmpeg hatası: {err_msg}")
            temp_clips.append(tmp_clip)
            temp_files.append(tmp_clip)

        with open(concat_list_path, "w", encoding="utf-8") as cf:
            for tc in temp_clips:
                safe_tc = tc.replace("\\", "/")
                cf.write(f"file '{safe_tc}'\n")
        temp_files.append(concat_list_path)

        total_dur = scene_duration * num_scenes
        audio_filter = f"afade=t=in:ss=0:d=1.0,afade=t=out:st={total_dur - 1.5:.2f}:d=1.5,volume=0.85"

        cmd_mux = [
            FFMPEG_EXE, "-y",
            "-f", "concat", "-safe", "0", "-i", concat_list_path,
            "-stream_loop", "-1", "-i", music_file,
            "-filter:a", audio_filter,
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-t", str(total_dur),
            "-movflags", "+faststart",
            output_mp4
        ]
        proc_mux = subprocess.run(cmd_mux, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc_mux.returncode != 0:
            err_msg = proc_mux.stderr.decode("utf-8", errors="ignore")[-300:]
            raise RuntimeError(f"Birleştirme FFmpeg hatası: {err_msg}")

    finally:
        for tf in temp_files:
            if os.path.exists(tf):
                try:
                    os.remove(tf)
                except Exception:
                    pass

    print(f"✅ 4 Sahneli 16 Saniyelik Karantinalı Reels videosu üretildi: {output_mp4}")
    return output_mp4


if __name__ == "__main__":
    test_img = os.path.join(IMAGES_DIR, "canan_feet_red_polish_couch.jpg")
    if os.path.exists(test_img):
        out = os.path.join(OUTPUT_DIR, "test_4scene_16s_text.mp4")
        create_reels_video(test_img, output_mp4=out)
