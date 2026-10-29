import os
import telebot
from groq import Groq

# Dauko lambobin sirri daga Environment Variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Fara aiki da Groq da Telegram Bot
client = Groq(api_key=GROQ_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Aika sakon zuwa ga Groq (zaka iya amfani da model kamar llama-3.3-70b-versatile ko llama3-8b-8192)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message.text,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        # Mayar da amsar zuwa Telegram
        bot.reply_to(message, chat_completion.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, "Yi hakuri, an samu matsala wajen sarrafa sakonka.")
        print(f"Matsala: {e}")

print("Bot din da ke amfani da Groq yana aiki...")
bot.infinity_polling()
