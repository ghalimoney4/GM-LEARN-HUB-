import os
from flask import Flask
import threading
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "GM Learn Hub Live!"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, 
"Assalamu Alaikum! Barka da zuwa GM LEARN HUB 📚\n\n"
"Me kake so ka koya yau?\n"
"1️⃣ Turanci (English)\n"
"2️⃣ Larabci (Arabic)\n"
"3️⃣ Python / Computer\n\n"
"Rubuta kawai: 'Ina son Turanci' ko 'Ina son Larabci'")

@bot.message_handler(func=lambda m: True)
def reply(m):
    txt = m.text.lower()

    if "turanci" in txt or "english" in txt or "ingilishi" in txt:
        bot.reply_to(m,
"🇬🇧 TURANCI - Darasi na 1:\n\n"
"Greetings:\n"
"Hello = Sannu\n"
"Good morning = Barka da safiya\n"
"How are you? = Ina kwana?\n"
"I'm fine = Ina lafiya\n\n"
"Ka rubuta 'Na gane' mu wuce gaba, ko 'Larabci' don canzawa.")

    elif "larabci" in txt or "arabic" in txt or "arab" in txt:
        bot.reply_to(m,
"🇸🇦 LARABCI - Darasi na 1:\n\n"
"As-salamu alaikum = Aminci ya tabbata a gareku\n"
"Wa alaikum salam = Aminci ya tabbata a gareku ma\n"
"Kayfa haluk? = Ina lafiyarka?\n"
"Bikhair = Lafiya lau\n\n"
"Ka rubuta 'Na gane' mu wuce gaba.")

    elif "python" in txt or "computer" in txt or "code" in txt:
        bot.reply_to(m,
"💻 PYTHON - Darasi na 1:\n\n"
"print('Sannu Duniya')\n"
"Wannan zai buga Sannu Duniya a kwamfuta.\n\n"
"Ka rubuta 'Na gane' mu wuce gaba.")

    elif "na gane" in txt or "gaba" in txt or "next" in txt:
        bot.reply_to(m,
"Masha Allah! 👏\n\n"
"Darasi na 2 ya zo nan ba da jimawa ba.\n"
"Yanzu ka zaba: Turanci, Larabci, ko Python?")

    elif "sannu" in txt or "slm" in txt or "assalam" in txt or "y" == txt.strip():
        bot.reply_to(m, "Wa alaikum salam! Me kake so ka koya? Rubuta Turanci, Larabci, ko Python.")

    else:
        bot.reply_to(m, f"Tambayarka: {m.text}\n\nNa gane. Ka rubuta daya daga cikin:\n- Ina son Turanci\n- Ina son Larabci\n- Ina son Python")

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
