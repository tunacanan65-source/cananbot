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


def get_short_hook_for_image(image_path: str, is_last_scene: bool = False, custom_hook: str = None) -> str:
    """Görselin temasına göre ekrana taşmayan, kısa ve yüksek etkileşimli cümle seçer."""
    if is_last_scene:
        final_hooks = [
            "1, 2, 3 yoksa 4. kare mi? Favorini yaz!",
            "En çok hangi karede gözün kaldı? Yoruma yaz!",
            "4 pozdan hangisi 10/10? Seç bakalım!",
            "İlk kare mi son kare mi? Yorumda buluşalım!"
        ]
        return random.choice(final_hooks)

    if custom_hook and len(custom_hook.strip()) <= 55:
        return custom_hook.strip()

    fname = os.path.basename(image_path).lower()

    if any(k in fname for k in ("feet", "polish", "pedi", "toes", "anklet")):
        feet_hooks = [
            "Yeni sürdüm, ojem nasıl olmuş?",
            "Ojemin rengi yakışmış mı? Puanın kaç?",
            "Bakım şart dedik, ojem nasıl görünüyor?",
            "Bu renk ojeyi beğendin mi tatlım?",
            "Ayak bakımım bitti, sence nasıl olmuş?"
        ]
        return random.choice(feet_hooks)

    if any(k in fname for k in ("bikini", "swim", "pool", "yacht", "beach", "sunbed", "hammock", "shower")):
        summer_hooks = [
            "Güneş mi daha sıcak yoksa bu poz mu?",
            "Bu fiziği korumak kolay değil tatlım!",
            "Deniz mi havuz mu? Sen hangisisin?",
            "Tatil modunu açtık, puanın kaç?"
        ]
        return random.choice(summer_hooks)

    if any(k in fname for k in ("gym", "pilates", "yoga", "fitness", "workout", "cycling", "tennis", "rug")):
        sport_hooks = [
            "Antrenman bitti, sence emeğime değmiş mi?",
            "Spor sonrası dinlenme, enerji nasıl?",
            "Bu spor takımının rengi yakışmış mı?",
            "Bahane yok, fiziğe yatırım var!"
        ]
        return random.choice(sport_hooks)

    if any(k in fname for k in ("satin", "silk", "lace", "cami", "slip", "robe", "bed", "bath")):
        lounge_hooks = [
            "Ev hali mi dışarı hali mi? Hangisi?",
            "Günün en huzurlu saatleri, nasılım?",
            "İpek rahatlığı diye bir gerçek var!",
            "Yanıma bir kahve alıp gelecek var mı?"
        ]
        return random.choice(lounge_hooks)

    general_hooks = [
        "Bu kombinle akşam yemeğine çıkılır mı?",
        "Sence bu renk bana yakışmış mı?",
        "Tarzıma 10 üzerinden kaç veriyorsun?",
        "Gözlüklerim ve kombinim nasıl olmuş?"
    ]
    return random.choice(general_hooks)


def create_overlay_png(text: str, out_png_path: str):
    """
    1080x1920 şeffaf katman üzerine, asla ekrandan taşmayan (maksimum 820px genişlik),
    ufak, zarif, yarı saydam koyu kapsül içinde net beyaz Türkçe etkileşim yazısı çizer.
    """
    canvas = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    font = _load_font(size=31)

    # Emojileri temizle (standart TTF fontlarda kare çıkmaması için sadece saf Türkçe metin + noktalama)
    clean_text = "".join(ch for ch in text if ord(ch) < 0x1F000).strip()
    if not clean_text:
        clean_text = "Sence nasıl olmuş? Yorumda buluşalım!"

    # Satır sarma: maksimum 34 karakter (1080px içinde ~740px genişlik, kenarlardan 170px güvenli boşluk)
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
    # Alt-orta güvenli bölge (y=1470: hem yüzü/vücudu/ayakları kapatmaz hem Instagram/FB alt yazı alanına çarpmaz)
    box_y1 = 1470 - (box_h // 2)
    box_x2 = box_x1 + box_w
    box_y2 = box_y1 + box_h

    # Yarı saydam şık kapsül arka plan + ince zarif çerçeve
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
        # Hafif gölge
        draw.text((tx + 2, curr_y + 2), ln, font=font, fill=(0, 0, 0, 210))
        draw.text((tx, curr_y), ln, font=font, fill=(255, 255, 255, 255))
        curr_y += lh + 10

    canvas.save(out_png_path, "PNG")
    return out_png_path


def get_motion_filter(style_index: int, total_frames: int) -> str:
    """8 Farklı Sinematik Kamera Hareketi (1080x1920 Full HD)."""
    styles = [
        f"zoompan=z='min(zoom+0.0010,1.14)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0010,1.15)':x='iw/2-(iw/zoom/2)':y='ih/3-(ih/zoom/3)':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(on/{total_frames})':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(on/{total_frames})':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='max(1.15-0.0011*on,1.0)':x='iw/2-(iw/zoom/2)':y='ih/2.3-(ih/zoom/2.3)':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0008,1.12)':x='(iw-iw/zoom)*(1-on/{total_frames})':y='ih/2.1-(ih/zoom/2.1)':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0009,1.14)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/{total_frames})':d={total_frames}:s=1080x1920:fps=30",
        f"zoompan=z='min(zoom+0.0009,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2.5-(ih/zoom/2.5)':d={total_frames}:s=1080x1920:fps=30,eq=saturation=1.06:contrast=1.02"
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
    Ana görsele eşlik edecek 3 farklı çekici/cesur Canan Tuna görseli seçer.
    Önceliği 'feet', 'bold', 'bikini', 'yacht', 'pool', 'satin', 'mini', 'rug', 'gym', 'silk', 'corset' görsellerine verir.
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

    primary_name = os.path.basename(primary_abs).lower()
    feet_pool = [p for p in pool if "canan_feet_" in os.path.basename(p).lower()]
    new_bold_pool = [p for p in pool if os.path.basename(p).lower().startswith(("canan_feet_", "canan_bold_"))]

    if "canan_feet_" in primary_name and len(feet_pool) >= 1 and len(new_bold_pool) >= count:
        # İlk sahne oje sürerken ise 2. sahnede bitmiş oje/ayak pozu, 3 ve 4. sahnede cesur bacak/kombin pozu gelsin
        second_feet = random.choice(feet_pool)
        other_bold = [p for p in new_bold_pool if p != second_feet]
        return [second_feet] + random.sample(other_bold, count - 1)

    source_pool = new_bold_pool if len(new_bold_pool) >= count else pool
    if len(source_pool) >= count:
        return random.sample(source_pool, count)
    chosen = list(source_pool)
    while len(chosen) < count and pool:
        chosen.append(random.choice(pool))
    return chosen


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
    - 4 farklı çekici Canan Tuna görseli (4 x 4.0 sn = 16.0 saniye)
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
        f"🎬 [4 Sahneli 16sn Etkileşimli Reels] Üretiliyor: {[os.path.basename(p) for p in scene_images]} "
        f"| Müzik: {os.path.basename(music_file)}"
    )

    temp_files = []
    temp_clips = []
    concat_list_path = os.path.join(OUTPUT_DIR, f"concat_{random.randint(10000, 99999)}.txt")

    try:
        for idx, img_p in enumerate(scene_images):
            m_style = available_motions[idx % len(available_motions)]
            zoom_filter = get_motion_filter(m_style, frames_per_scene)

            is_last = (idx == num_scenes - 1)
            scene_hook = get_short_hook_for_image(
                img_p,
                is_last_scene=is_last,
                custom_hook=(hook_text if idx == 0 else None)
            )

            overlay_png = os.path.join(OUTPUT_DIR, f"_tmp_ovl_{idx}_{random.randint(1000,9999)}.png")
            create_overlay_png(scene_hook, overlay_png)
            temp_files.append(overlay_png)

            fade_in = "fade=t=in:st=0:d=0.35," if idx > 0 else "fade=t=in:st=0:d=0.25,"
            fade_out = f"fade=t=out:st={scene_duration - 0.35:.2f}:d=0.35,"

            filter_complex = (
                f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
                f"{zoom_filter}[bg];"
                f"[bg][1:v]overlay=0:0,{fade_in}{fade_out}format=yuv420p[v]"
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

    print(f"✅ 4 Sahneli 16 Saniyelik Etkileşim Yazılı Reels videosu üretildi: {output_mp4}")
    return output_mp4


if __name__ == "__main__":
    test_img = os.path.join(IMAGES_DIR, "canan_royal_blue_yacht_sunset.jpg")
    if os.path.exists(test_img):
        out = os.path.join(OUTPUT_DIR, "test_4scene_16s_text.mp4")
        create_reels_video(test_img, output_mp4=out)
