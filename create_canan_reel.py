import os
import sys
import subprocess
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

def create_reels_video(image_path: str, voice_text: str = None, output_mp4: str = None, duration: float = 6.5) -> str:
    """
    1080x1920 dikey Reels formatında, sinematik yumuşak hareketli ve
    arkada telifsiz kısık sesli estetik müzikli video üretir.
    Robotik yapay zeka sesi kaldırılmıştır; gerçek influencer video estetiğindedir.
    """
    if not output_mp4:
        output_mp4 = os.path.join(OUTPUT_DIR, "reels_output.mp4")

    music_file = DEFAULT_MUSIC
    if not os.path.exists(music_file):
        raise FileNotFoundError(f"Arka plan müziği bulunamadı: {music_file}")

    total_frames = int(duration * 30)

    # 1. Sinematik yumuşak zoom / süzülme (Ken Burns)
    # 2. @canantuna_official estetik filigranı
    filter_complex = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        f"zoompan=z='min(zoom+0.0006,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1080x1920:fps=30,"
        f"drawtext=text='@canantuna_official':fontcolor=white@0.85:fontsize=38:x=50:y=h-140:box=1:boxcolor=black@0.4:boxborderw=12,"
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

    print(f"🎬 Estetik Reels videosu renderlanıyor ({duration:.1f} saniye, telifsiz müzikli)...")
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"FFmpeg hatası: {proc.stderr.decode('utf-8', errors='ignore')[-300:]}")

    print(f"✅ Video başarıyla oluşturuldu: {output_mp4}")
    return output_mp4

if __name__ == "__main__":
    test_img = r"C:\Users\celik\.gemini\antigravity\brain\eb5ca554-1024-44cf-8a0d-c56a293b0854\canan_tuna_bodrum_beach_1792678870147.jpg"
    out = os.path.join(OUTPUT_DIR, "test_aesthetic_reels.mp4")
    create_reels_video(test_img, output_mp4=out)
