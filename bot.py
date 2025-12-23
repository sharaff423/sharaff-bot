import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# আপনার কনফিগারেশন
API_TOKEN = '8231020937:AAFUGdiVdnBmOXypsBoCfUhU9htT8kOyDZM'
BOT_USERNAME = 'SherAff_bot' 
APP_SHORT_NAME = 'app' # BotFather এ যে নাম দিয়েছেন
WEB_APP_URL = 'https://sheraff.infinityfree.me/login.php' # আপনার ওয়েবসাইটের লগইন লিংক

bot = telebot.TeleBot(API_TOKEN)

# ওয়েবহুক ক্লিয়ার করা (এরর ফিক্স)
try:
    bot.remove_webhook()
except:
    pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    # রেফারেল আইডি হ্যান্ডলিং
    text_parts = message.text.split()
    ref_id = "0"
    if len(text_parts) > 1 and text_parts[1].startswith('ref'):
        ref_id = text_parts[1].replace('ref', '')

    # বাটন তৈরি (সরাসরি মিনি অ্যাপ ওপেন হবে)
    markup = InlineKeyboardMarkup()
    
    # বাটন ১: অ্যাপ ওপেন করা
    btn_app = InlineKeyboardButton(
        text="🚀 অ্যাপ ওপেন করুন (Earn Money)", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(btn_app)
    
    # বাটন ২: চ্যানেল লিংক (অপশনাল)
    markup.add(InlineKeyboardButton("📢 জয়েন চ্যানেল", url="https://t.me/YOUR_CHANNEL"))

    # মেসেজ
    welcome_text = (
        f"স্বাগতম {first_name}! 👋\n\n"
        f"SharAff এর মাধ্যমে আয় করতে নিচের বাটনে ক্লিক করুন।\n\n"
        f"👇👇👇"
    )
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

print("✅ বট চালু হয়েছে! টেলিগ্রামে গিয়ে /start দিন।")
bot.infinity_polling()
