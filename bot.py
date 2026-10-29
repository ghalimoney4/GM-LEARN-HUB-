import telebot
from groq import Groq

TELEGRAM_TOKEN = "9060610285:AAERTYVEDXF1U6OOWmkif4jxIYR5LVBkwvs"
GROQ_KEY = "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"

client = Groq(api_key=GROQ_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(m):
    try:
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Kai ne GM Academy Bot. Malami ne na Addinin Musulunci akan mazhabar Malikiyya, da koyar da Turanci da Larabci."},
                {"role": "user", "content": m.text}
            ]
        )
        bot.reply_to(m, chat.choices[0].message.content)
    except:
        bot.reply_to(m, "Yi hakuri, akwai matsala.")

bot.infinity_polling()
