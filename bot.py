import os
import telebot
import google.generativeai as genai

# Dauko Token din Telegram da Gemini API Key daga Environment Variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Tabbatar an saka su
if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
    print("Kuskure: Da fatan za a saita TELEGRAM_TOKEN da GEMINI_API_KEY a Render.")

# Saiti Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash") # Zaka iya amfani da wannan ko gemini-pro

# Saiti Telegram Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Idan wani ya tura sako
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Aika sakon zuwa ga Gemini sannan a karbi amsa
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Yi hakuri, na samu dan karamin matsala wajen sarrafa wannan sakon.")
        print(f"Matsala: {e}")

print("Bot din yana aiki yanzu...")
bot.infinity_polling()
