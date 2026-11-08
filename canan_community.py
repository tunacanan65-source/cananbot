import os
import sys
import json
import random
import requests
import config

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
REPLIED_FILE = os.path.join(BASE_DIR, "replied_comments.json")

# Paylaşım yapıldığı saniye Canan'ın kendi gönderisinin altına bıraktığı ilk yorumlar
FIRST_COMMENTS_VIDEO = [
    "Yorumların hepsini tek tek okuyorum, en samimi yorumu yapanın profiline gizlice bakacağım 👀🔥",
    "Sizce 1, 2, 3 yoksa 4. kare mi daha güzel olmuş? Seçiminizi aşağıya bekliyorum tatlım 👇💅",
    "Ojemin rengine ve kombinime 10 üzerinden kaç veriyorsunuz? Dürüst olun ama 🙈💋",
    "Son kareye kadar izleyenler kendisini belli etsin, favoriniz kaçıncı kare oldu? 👇✨",
    "Açık renk oje mi yoksa koyu renk oje mi? Sizin favoriniz hangisi, yoruma yazın bakalım 👇🔥",
    "Buraya bir kalp bırakan herkese benden de kocaman öpücükler, yorumlarda buluşalım mı? 🥰✨"
]

FIRST_COMMENTS_PHOTO = [
    "Yorumların hepsini tek tek okuyorum, en tatlı yorumu yapanın profilini inceleyeceğim 👀💋",
    "Bu kombinime ve enerjime 10 üzerinden kaç veriyorsunuz tatlım? Yoruma yazın 👇🔥",
    "Bugün enerjim çok yüksek, bana eşlik edecek olanlar yoruma bir kalp bıraksın 🥰✨",
    "Sence bu tarz bana yakışmış mı? Samimi fikrini aşağıya bekliyorum 👇💅"
]

# Takipçi yorumunun içeriğine göre Canan'ın vereceği akıllı & flörtöz cevaplar
REPLIES_OJE_FEET = [
    "Beğenmene çok sevindim tatlım, bir sonraki ojem hangi renk olsun sence? 💅🥰",
    "Çok teşekkür ederim, ayak bakımına ve ojelerime çok özen gösteriyorum 🙈✨",
    "Ojemin rengini beğenmen beni çok mutlu etti canım, senin favori rengin ne? 💅💋",
    "Bakımlı olmayı seviyorum diyelim tatlım, çok teşekkür ederim güzel yorumun için! 🥰🔥"
]

REPLIES_SCENE_CHOICE = [
    "Harika seçim tatlım, gözün kesinlikle güzelden anlıyor! 🔥🥰",
    "Benim de gizli favorim tam olarak o kareydi, zevklerimiz çok benziyor! ✨💋",
    "Sonuna kadar dikkatle izlemişsin, bayıldım seçimine canım! 🥰💅",
    "O kareyi çekerken ben de çok keyif almıştım, beğenmene çok sevindim! 🔥✨"
]

REPLIES_GENERAL = [
    "Çok tatlısın, güzel enerjin bana kadar geldi teşekkür ederim! 🥰✨",
    "Yorumun yüzümü güldürdü tatlım, iyi ki varsın! 🔥💋",
    "Çok teşekkür ederim canım, peki senin favori karen hangisi oldu? 👀✨",
    "Güzel sözlerin için çok teşekkürler tatlım, kalp bıraktım sana! ❤️🥰",
    "Senin güzel bakan gözlerin öyle görmüş canım, çok mutlu ettin beni! 🙈💋",
    "Harikasın tatlım, yorumlarda seni görmek çok güzel! ✨🥰"
]

BAD_WORDS = (
    "aptal", "salak", "gerizekalı", "orospu", "fahişe", "piç", "amk", "aq",
    "sik", "yarrak", "göt", "kaşar", "escort", "eskort", "fake", "yapay", "bot"
)


def _load_replied() -> set:
    if os.path.exists(REPLIED_FILE):
        try:
            with open(REPLIED_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()


def _save_replied(replied_set: set):
    try:
        items = list(replied_set)[-1500:]
        with open(REPLIED_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False)
    except Exception:
        pass


def _pick_smart_reply(comment_text: str) -> str:
    low = comment_text.lower()
    if any(k in low for k in ("oje", "ayak", "tırnak", "pedikür", "kırmızı", "bordo", "renk", "parmak")):
        return random.choice(REPLIES_OJE_FEET)
    if any(k in low for k in ("1", "2", "3", "4", "kare", "birinci", "ikinci", "üçüncü", "dördüncü", "son", "hepsi")):
        return random.choice(REPLIES_SCENE_CHOICE)
    return random.choice(REPLIES_GENERAL)


def _is_own_or_unsafe_comment(text: str, author_name: str = "", author_id: str = "") -> bool:
    if not text or len(text.strip()) < 2:
        return True
    low = text.lower().strip()
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    if author_id and str(author_id) == str(page_id):
        return True
    if author_name and "canan" in author_name.lower():
        return True
    for fc in FIRST_COMMENTS_VIDEO + FIRST_COMMENTS_PHOTO:
        if fc[:22].lower() in low:
            return True
    for bw in BAD_WORDS:
        if bw in low:
            return True
    return False


def post_first_comment_instagram(media_id: str, is_video: bool = True) -> bool:
    """Paylaşılan Instagram gönderisinin altına anında Canan'ın ilk etkileşim yorumunu bırakır."""
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    if not media_id or not token:
        return False
    msg = random.choice(FIRST_COMMENTS_VIDEO if is_video else FIRST_COMMENTS_PHOTO)
    try:
        r = requests.post(
            f"https://graph.facebook.com/v21.0/{media_id}/comments",
            data={"message": msg, "access_token": token},
            timeout=15
        ).json()
        if "id" in r:
            print(f"📌 [Instagram İlk Yorum] Başarıyla sabitlendi: {msg}")
            return True
        print(f"⚠️ [Instagram İlk Yorum Uyarısı]: {r}")
    except Exception as e:
        print(f"⚠️ [Instagram İlk Yorum İstisnası]: {e}")
    return False


def post_first_comment_facebook(post_id: str, is_video: bool = True) -> bool:
    """Paylaşılan Facebook Reels/Fotoğraf gönderisinin altına anında Canan'ın ilk yorumunu bırakır."""
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    if not post_id or not token:
        return False
    msg = random.choice(FIRST_COMMENTS_VIDEO if is_video else FIRST_COMMENTS_PHOTO)
    try:
        r = requests.post(
            f"https://graph.facebook.com/v21.0/{post_id}/comments",
            data={"message": msg, "access_token": token},
            timeout=15
        ).json()
        if "id" in r:
            print(f"📌 [Facebook İlk Yorum] Başarıyla bırakıldı: {msg}")
            return True
        print(f"⚠️ [Facebook İlk Yorum Uyarısı]: {r}")
    except Exception as e:
        print(f"⚠️ [Facebook İlk Yorum İstisnası]: {e}")
    return False


def check_and_reply_comments():
    """
    Instagram ve Facebook'taki son gönderilerin altına gelen takipçi yorumlarını tarar
    ve henüz yanıtlanmamış olanlara Canan Tuna ağzından samimi/flörtöz cevap verir.
    """
    token = getattr(config, "FACEBOOK_ACCESS_TOKEN", "")
    ig_id = getattr(config, "INSTAGRAM_ACCOUNT_ID", "17841458805624158")
    page_id = getattr(config, "FACEBOOK_PAGE_ID", "1355526950985735")
    if not token:
        return

    replied_ids = _load_replied()
    new_replies_count = 0

    # 1. INSTAGRAM YORUMLARI
    if ig_id:
        try:
            ig_url = (
                f"https://graph.facebook.com/v21.0/{ig_id}/media"
                f"?fields=id,comments.limit(15){{id,text,username,replies{{id}}}}"
                f"&limit=6&access_token={token}"
            )
            resp = requests.get(ig_url, timeout=15).json()
            for media in resp.get("data", []):
                comments = media.get("comments", {}).get("data", [])
                for c in comments:
                    cid = c.get("id")
                    ctext = c.get("text", "")
                    cuser = c.get("username", "")
                    existing_replies = c.get("replies", {}).get("data", [])

                    if not cid or cid in replied_ids or existing_replies:
                        continue
                    if _is_own_or_unsafe_comment(ctext, author_name=cuser):
                        replied_ids.add(cid)
                        continue

                    reply_msg = _pick_smart_reply(ctext)
                    if cuser:
                        reply_msg = f"@{cuser} {reply_msg}"

                    r_rep = requests.post(
                        f"https://graph.facebook.com/v21.0/{cid}/replies",
                        data={"message": reply_msg, "access_token": token},
                        timeout=15
                    ).json()
                    replied_ids.add(cid)
                    if "id" in r_rep:
                        new_replies_count += 1
                        print(f"💬 [IG Yorum Yanıtlandı] @{cuser}: '{ctext[:30]}' -> '{reply_msg}'")
        except Exception as e:
            print(f"⚠️ [IG Yorum Tarama Uyarısı]: {e}")

    # 2. FACEBOOK YORUMLARI
    if page_id:
        try:
            fb_url = (
                f"https://graph.facebook.com/v21.0/{page_id}/published_posts"
                f"?fields=id,comments.limit(15){{id,message,from,comments{{id}}}}"
                f"&limit=6&access_token={token}"
            )
            resp_fb = requests.get(fb_url, timeout=15).json()
            for post in resp_fb.get("data", []):
                comments = post.get("comments", {}).get("data", [])
                for c in comments:
                    cid = c.get("id")
                    ctext = c.get("message", "")
                    from_obj = c.get("from") or {}
                    cuser = from_obj.get("name", "")
                    cuid = from_obj.get("id", "")
                    existing_replies = c.get("comments", {}).get("data", [])

                    if not cid or cid in replied_ids or existing_replies:
                        continue
                    if _is_own_or_unsafe_comment(ctext, author_name=cuser, author_id=cuid):
                        replied_ids.add(cid)
                        continue

                    # Önce yorumu beğen
                    try:
                        requests.post(
                            f"https://graph.facebook.com/v21.0/{cid}/likes",
                            data={"access_token": token},
                            timeout=10
                        )
                    except Exception:
                        pass

                    reply_msg = _pick_smart_reply(ctext)
                    r_rep = requests.post(
                        f"https://graph.facebook.com/v21.0/{cid}/comments",
                        data={"message": reply_msg, "access_token": token},
                        timeout=15
                    ).json()
                    replied_ids.add(cid)
                    if "id" in r_rep:
                        new_replies_count += 1
                        print(f"💬 [FB Yorum Yanıtlandı] {cuser}: '{ctext[:30]}' -> '{reply_msg}'")
        except Exception as e:
            print(f"⚠️ [FB Yorum Tarama Uyarısı]: {e}")

    _save_replied(replied_ids)
    if new_replies_count > 0:
        print(f"✅ Toplam {new_replies_count} yeni takipçi yorumuna samimi yanıt verildi!")
