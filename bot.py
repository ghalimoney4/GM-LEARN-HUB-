import os
import telebot
from groq import Groq
from flask import Flask
import threading

# Karbo keys daga Render Environment - idan babu sai ya dauki na GitHub
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN", "9060610285:AAERTYVEDXFxxx")
GROQ_KEY = os.getenv("GROQ_KEY", "gsk_YiJbfdoXvkIhUT9OSIdwGdyIxxx")

client = Groq(api_key=GROQ_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "GM LEARN HUB Bot is Live!"

@bot.message_handler(func=lambda m: True)
def handle(m):
    try:
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Kai malamin Hausa ne."},
                {"role": "user", "content": m.text}
            ]
        )
        bot.reply_to(m, chat.choices[0].message.content)
    except:
        bot.reply_to(m, "Yi hakuri, akwai matsala. Sake gwadawa.")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
