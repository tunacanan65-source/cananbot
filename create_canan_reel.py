import os
import sys
import subprocess
import random
import imageio_ffmpeg

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
MUSIC_DIR = os.path.join(BASE_DIR, "assets", "music")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

DEFAULT_MUSIC = os.path.join(MUSIC_DIR, "aesthetic_lofi.mp3")

# 4 Farklı Sinematik Kamera Hareketi Şablonu (Ken Burns & Dynamic Tilt)
def get_motion_filter(style_index: int, total_frames: int) -> str:
    styles = [
        # 0: Yavaş & Zarif Zoom-In (Merkeze odaklanma)
        f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30",
        # 1: Yüze & Gözlere Odaklanma (Üst kadraj Ken-Burns)
        f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='ih/3-(ih/zoom/3)':d={total_frames}:s=1080x1920:fps=30",
        # 2: Yatay Sinematik Süzülüş (Gentle horizontal pan)
        f"zoompan=z='min(zoom+0.0006,1.10)':x='(iw-iw/zoom)*(on/{total_frames})':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30",
        # 3: Dikey & Çapraz Estetik Akış (Subtle vertical drift)
        f"zoompan=z='min(zoom+0.0005,1.08)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(on/{total_frames})':d={total_frames}:s=1080x1920:fps=30"
    ]
    return styles[style_index % len(styles)]


def pick_background_music() -> str:
    """Müzik klasöründeki telifsiz parçalardan birini seçer."""
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


def create_reels_video(
    image_path: str,
    voice_text: str = None,
    output_mp4: str = None,
    duration: float = 6.5,
    motion_index: int = None
) -> str:
    """
    1080x1920 dikey Reels formatında, 4 farklı sinematik hareket tarzı ve
    arka plan estetik müziğiyle ultra-kaliteli reels videosu üretir.
    """
    if not output_mp4:
        output_mp4 = os.path.join(OUTPUT_DIR, "reels_output.mp4")

    music_file = pick_background_music()
    if not music_file or not os.path.exists(music_file):
        raise FileNotFoundError(f"Arka plan müziği bulunamadı: {music_file}")

    total_frames = int(duration * 30)

    # Kamera hareketi seçimi
    if motion_index is None:
        motion_index = random.randint(0, 3)

    zoom_filter = get_motion_filter(motion_index, total_frames)
    print(f"🎥 Seçilen Sinematik Hareket Modu: {motion_index} | Müzik: {os.path.basename(music_file)}")

    filter_complex = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        f"{zoom_filter},"
        f"format=yuv420p[v];"
        f"[1:a]afade=t=in:ss=0:d=1,afade=t=out:st={duration-1.5}:d=1.5,volume=0.85[a]"
    )

    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1", "-i", image_path,
        "-ss", "0", "-t", str(duration), "-i", music_file,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "22",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(duration),
        output_mp4
    ]

    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        err_msg = proc.stderr.decode('utf-8', errors='ignore')[-300:]
        print(f"⚠️ FFmpeg Hatası: {err_msg}")
        raise RuntimeError(f"FFmpeg hatası: {err_msg}")

    print(f"✅ Sinematik Reels videosu üretildi: {output_mp4}")
    return output_mp4


if __name__ == "__main__":
    test_img = os.path.join(BASE_DIR, "assets", "images", "canan_ceramics_studio.jpg")
    if os.path.exists(test_img):
        out = os.path.join(OUTPUT_DIR, "test_ceramics_motion.mp4")
        create_reels_video(test_img, output_mp4=out, motion_index=1)
