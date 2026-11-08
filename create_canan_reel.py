import os
import sys
import textwrap
import subprocess
import random
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
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

DEFAULT_MUSIC = os.path.join(MUSIC_DIR, "aesthetic_lofi.mp3")


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

    fname = os.path.basename(image_path).lower()

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
                "Bu renk ojeyi beğendin mi tatlım?"
            ]
            return random.choice(feet_done_hooks)

    if any(k in fname for k in ("bikini", "swim", "pool", "yacht", "beach", "sunbed", "hammock", "shower")):
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
        "Bu elbiseyle dışarı çıkılır mı tatlım?",
        "Sence bu renk bana yakışmış mı?",
        "Tarzıma 10 üzerinden kaç veriyorsun?"
    ]
    return random.choice(general_hooks)


def create_overlay_png(text: str, out_png_path: str, y_pos: int = 1470):
    """
    1080x1920 şeffaf katman üzerine, asla ekrandan taşmayan (maksimum 900px genişlik),
    ufak, zarif, yarı saydam koyu kapsül içinde net beyaz Türkçe etkileşim yazısı çizer.
    """
    canvas = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font = _load_font(size=31)

    clean_text = "".join(ch for ch in text if ord(ch) < 0x1F000).strip()
    if not clean_text:
        clean_text = "Sence nasıl olmuş? Yorumda buluşalım!"

    lines = textwrap.wrap(clean_text, width=34)
    if len(lines) > 2:
        lines = lines[:2]

    line_bboxes = [draw.textbbox((0, 0), ln, font=font) for ln in lines]
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
        draw.text((tx + 2, curr_y + 2), ln, font=font, fill=(0, 0, 0, 210))
        draw.text((tx, curr_y), ln, font=font, fill=(255, 255, 255, 255))
        curr_y += lh + 10

    canvas.save(out_png_path, "PNG")
    return out_png_path


def create_story_image(image_path: str, story_text: str, output_jpg: str = None) -> str:
    """
    Günlük Otomatik Hikaye (Story) için 1080x1920 dikey görselin üzerine
    şık ve taşmayan bir hikaye notu ("Günaydın tatlım", "İyi geceler, uyuyan var mı?") işler.
    """
    if not output_jpg:
        output_jpg = os.path.join(OUTPUT_DIR, f"story_{random.randint(1000, 9999)}.jpg")

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
    """8 Farklı Sinematik Kamera Hareketi + Canlı/Aydınlık Renk Dokunuşu (1080x1920 Full HD)."""
    bright_eq = ",eq=brightness=0.025:contrast=1.03:saturation=1.05"
    styles = [
        f"zoompan=z='min(zoom+0.0010,1.14)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0010,1.15)':x='iw/2-(iw/zoom/2)':y='ih/3-(ih/zoom/3)':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(on/{total_frames})':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(on/{total_frames})':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='max(1.15-0.0011*on,1.0)':x='iw/2-(iw/zoom/2)':y='ih/2.3-(ih/zoom/2.3)':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(1-on/{total_frames})':y='ih/2.1-(ih/zoom/2.1)':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0009,1.14)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/{total_frames})':d={total_frames}:s=1080x1920:fps=30{bright_eq}",
        f"zoompan=z='min(zoom+0.0009,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2.5-(ih/zoom/2.5)':d={total_frames}:s=1080x1920:fps=30{bright_eq}"
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


def pick_companion_images(primary_image: str, count: int = 3, extra_candidates: list = None) -> list:
    """
    4 Karede 'Adım Adım Hazırlanma' (Öncesi/Sonrası Hikaye Kurgusu):
    İzleyiciyi 16 saniye boyunca ekranda tutmak için sahneleri hikaye sırasıyla seçer:
    - Eğer 1. kare oje/ayak bakımı ise:
      2. kare -> Bitmiş oje/pedikür pozu
      3. kare -> Plaj / Bikini / Spor / Gündüz bacak pozu
      4. kare -> Gece mini elbise / korse / saten final pozu
    - Eğer 1. kare başka bir poz ise:
      2. kare -> Oje / ayak bakımı pozu (her Reels'te mutlaka oje/ayak sahnesi yer alır)
      3. kare -> Plaj / Bikini / Spor pozu
      4. kare -> Gece mini elbise / korse / saten final pozu
    """
    primary_abs = os.path.abspath(primary_image)
    if extra_candidates:
        pool = [p for p in extra_candidates if os.path.exists(p) and os.path.abspath(p) != primary_abs]
    else:
        all_imgs = [
            os.path.join(IMAGES_DIR, f)
            for f in os.listdir(IMAGES_DIR)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
        pool = [p for p in all_imgs if os.path.abspath(p) != primary_abs]

    feet_pool = [p for p in pool if "canan_feet_" in os.path.basename(p).lower()]
    day_glam_pool = [
        p for p in pool
        if os.path.basename(p).lower().startswith("canan_bold_")
        and any(k in os.path.basename(p).lower() for k in ("bikini", "pool", "yacht", "beach", "sunbed", "hammock", "shower", "gym", "yoga", "tennis", "shorts"))
    ]
    night_glam_pool = [
        p for p in pool
        if os.path.basename(p).lower().startswith("canan_bold_")
        and any(k in os.path.basename(p).lower() for k in ("mini", "corset", "satin", "backless", "plunge", "cutout", "chainmail", "mesh", "halter", "bodycon", "leather", "velvet", "silk"))
    ]
    all_bold_pool = [p for p in pool if os.path.basename(p).lower().startswith(("canan_feet_", "canan_bold_"))]

    chosen = []
    if len(feet_pool) >= 1:
        chosen.append(random.choice(feet_pool))
    if len(day_glam_pool) >= 1:
        c_day = [p for p in day_glam_pool if p not in chosen]
        if c_day:
            chosen.append(random.choice(c_day))
    if len(night_glam_pool) >= 1:
        c_night = [p for p in night_glam_pool if p not in chosen]
        if c_night:
            chosen.append(random.choice(c_night))

    fallback_source = [p for p in (all_bold_pool or pool) if p not in chosen]
    while len(chosen) < count and fallback_source:
        pick = random.choice(fallback_source)
        chosen.append(pick)
        fallback_source.remove(pick)

    return chosen[:count]


def create_reels_video(
    image_path: str,
    voice_text: str = None,
    output_mp4: str = None,
    duration: float = 16.0,
    motion_index: int = None,
    companion_images: list = None,
    hook_text: str = None
) -> str:
    """
    Facebook & Instagram Para Kazanma ve Yüksek Etkileşim Kriterlerine Özel:
    - 4 karede 'Adım Adım Hazırlanma' kurgusu (4 x 4.0 sn = 16.0 saniye)
    - İlk kareden (0.00 sn) itibaren %100 parlak ve net başlangıç (karanlık başlangıç yok)
    - Her sahnede ekrana taşmayan, ufak ve şık etkileşim sorusu (Pillow PNG katmanı)
    - 1080x1920 Full HD (CRF 19) + telifsiz arka plan müziği
    """
    if not output_mp4:
        output_mp4 = os.path.join(OUTPUT_DIR, "reels_output.mp4")

    music_file = pick_background_music()
    if not music_file or not os.path.exists(music_file):
        raise FileNotFoundError(f"Arka plan müziği bulunamadı: {music_file}")

    companions = pick_companion_images(image_path, count=3, extra_candidates=companion_images)
    scene_images = [image_path] + companions
    num_scenes = len(scene_images)
    scene_duration = round(duration / num_scenes, 2)
    frames_per_scene = int(scene_duration * 30)

    available_motions = list(range(8))
    random.shuffle(available_motions)
    if motion_index is not None:
        available_motions[0] = motion_index % 8

    print(
        f"🎬 [4 Sahneli 16sn Hikaye Kurgulu Reels] Üretiliyor: {[os.path.basename(p) for p in scene_images]} "
        f"| Müzik: {os.path.basename(music_file)}"
    )

    temp_files = []
    temp_clips = []
    concat_list_path = os.path.join(OUTPUT_DIR, f"concat_{random.randint(10000, 99999)}.txt")

    try:
        for idx, img_p in enumerate(scene_images):
            m_style = available_motions[idx % len(available_motions)]
            zoom_filter = get_motion_filter(m_style, frames_per_scene)

            scene_hook = get_short_hook_for_image(
                img_p,
                scene_index=idx,
                num_scenes=num_scenes,
                custom_hook=(hook_text if idx == 0 else None)
            )

            overlay_png = os.path.join(OUTPUT_DIR, f"_tmp_ovl_{idx}_{random.randint(1000,9999)}.png")
            create_overlay_png(scene_hook, overlay_png)
            temp_files.append(overlay_png)

            # İlk kareden itibaren %100 parlak ve net başlasın (karanlık başlangıç olmasın)
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

    print(f"✅ 4 Sahneli 16 Saniyelik Hikaye Kurgulu Reels videosu üretildi: {output_mp4}")
    return output_mp4


if __name__ == "__main__":
    test_img = os.path.join(IMAGES_DIR, "canan_feet_red_polish_couch.jpg")
    if os.path.exists(test_img):
        out = os.path.join(OUTPUT_DIR, "test_4scene_16s_text.mp4")
        create_reels_video(test_img, output_mp4=out)
