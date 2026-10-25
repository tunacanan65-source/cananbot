import os

# Canan Tuna AI Influencer Yapılandırması
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8591583248:AAHFjFXjE_NqzdDUNuwXVshiCzBMQ7rU5EE")
TELEGRAM_CHANNEL = os.environ.get("TELEGRAM_CHANNEL", "-1004438153704")  # @canantunaaa

# Yeni Bağımsız Sayfa: Canan tunau (Instagram'a bağlı resmi sayfa)
FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID", "1355526950985735")
# Süresiz Sistem Kullanıcısı Sayfa Tokeni (expires_at=0, kişisel hesap çıkışlarından ASLA etkilenmez)
FACEBOOK_ACCESS_TOKEN = os.environ.get("FACEBOOK_ACCESS_TOKEN", "EAAPkhml4r90BSZCghDQt11ySMJMra0vKXqY24H9UqfyiFklm5vExBKAuwZAIDHNLZAXStiocizdvZAc1ADKMrp76wIQ5VhCzKENs0K8TGv2UvzZBH045TzPANPTYr9xXoFJ0ug20XwGqQbSp7ppTez2BojkBn62kfFZApxOOTH2u7i9iK3b7Y5bHNGQL9GadJU2Cvl7UDW")
INSTAGRAM_ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID", "17841458805624158")

# Botun doğrudan Render sunucusu adresi (Meta video/resim çekimi için kendi yüksek hızlı CDN'imiz)
BASE_URL = os.environ.get("BASE_URL", "https://cananbot.onrender.com")
