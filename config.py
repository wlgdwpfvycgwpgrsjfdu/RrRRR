from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "8010050364:AAEkZcYHfKYyQpS_VfQRnvTwl-xs6IY2zVE")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1sAUHrdNkS-5iAVQF--vTjMOq8hOPV2e2VdcrR2Jgedjjud8gwKdz8dULTJshze0J68XxqKUyoSNtzK9xUodwTFelwBz1lkk3fzjRhfvKLB6TYpozvH5O65cqhjrcu9fvcU_3wGnBC3_G-1AHsF9Aqx0FWTKTq7MGLm4NnRsdqck_8WWhi8IQtYGAGvlJAiDi22t3ZCpbrR08cEctH0GhUTI4rNqamsfglIZgsgkXD0BO3suwelmAddkBcbPFzOAjjzv6ZbJsIKJvdlzH9pbDJvWaJ6q63t84QSt04VK94P1Y8avg1zbit9A9A6YlwbNSwDut8hxXQdy-UBRIvVpHufuD4=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Turki_1427H") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "sonng") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/wlgdwpfvycgwpgrsjfdu/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/+EopGVwVf1241NjY8") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_1_BOT") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "7265137398").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7265137398").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
