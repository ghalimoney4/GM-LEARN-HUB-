import os
from flask import Flask
import threading
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot yana aiki!"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Barka da zuwa GM Learn Hub!\n\nNi Malamin Computer Science ne. Me kake so ka koya?\n\n1. Python\n2. Web Development\n3. Computer Basics\n\nRubuta misali: Ina son koyon Python")

@bot.message_handler(func=lambda m: True)
def reply(m):
    text = m.text.lower()
    if "python" in text:
        bot.reply_to(m, "Python harshe ne mai sauki. Bari mu fara:\n\n`print('Sannu Duniya')`\nWannan shine code na farko. Ka gwada?")
    elif "web" in text or "html" in text:
        bot.reply_to(m, "Web Development: Za mu koya HTML, CSS, JavaScript. Bari mu fara da HTML:\n\n<h1>Sannu</h1>")
    elif "sannu" in text or "slm" in text or "assalam" in text:
        bot.reply_to(m, "Wa alaikum salam! Barka da zuwa. Me kake so ka koya a Computer?")
    else:
        bot.reply_to(m, f"Tambayarka: {m.text}\n\nNi zan koya maka step-by-step. Ka ce min: Ina son koyon Python ko Web?")

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("Bot yana aiki...")
    bot.infinity_polling()
