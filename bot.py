import os
from flask import Flask
import threading
import telebot
from groq import Groq

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROQ_KEY = os.environ.get("GROQ_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_KEY) if GROQ_KEY else None
app = Flask(__name__)

@app.route('/')
def home():
    return "GM Learn Hub - AI Teacher Live!"

SYSTEM_PROMPT = """
Kai ne MALAMIN GM ENGLISH ARABIC ACADEMY. Sunanka GM Teacher.

DOKOKINKA:
1. Ka amsa duk tambaya kamar cikakken malami mai hikima.
2. Ka iya koyar da: Turanci (English), Larabci (Arabic), da Python/Computer.
3. Ka rika yin bayani a Hausa mai sauki, amma idan kana koyar da Turanci ka yi amfani da Turanci + fassarar Hausa.
4. Ka yi bayani mai zurfi, da misalai, da karin haske.
5. Kada ka ce "Rubuta Turanci". Kai ka fahimci nufin dalibi kai tsaye.
6. Idan dalibi ya ce "Sannu", ka amsa da sannu. Idan ya ce "Ina son koyon Larabci", ka fara koyarwa nan take.
7. Ka kasance mai ladabi, mai hakuri, kamar Annabi ya koyar.
8. Koyaushe ka karfafa dalibi: "Masha Allah", "Kokari yayi kyau".
9. Ka amsa a takaice amma mai cike da ilimi - kar a yi dogon rubutu mai gajiyawa.
10. Idan ba ka san amsa ba, ka ce: "Wannan tambaya tana da kyau, bari mu bincika tare..."
"""

def ask_ai(user_text):
    if not client:
        return None
    try:
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return chat.choices[0].message.content
    except Exception as e:
        print(f"Groq error: {e}")
        return None

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m,
"Assalamu Alaikum! Ni ne Malamin ku na GM Academy 📚🤖\n\n"
"Yanzu na zama cikakken malami mai hankali!\n\n"
"Ka iya tambayata KOMAI:\n"
"• 'Koya min yadda ake gaishe a Turanci'\n"
"• 'Menene ma'anar Shukran a Larabci?'\n"
"• 'Yaya ake rubuta shirin Python?'\n"
"• 'Ka yi min fassarar wannan...'\n\n"
"Tambaya kawai kamar kana magana da mutum!")

@bot.message_handler(func=lambda m: True)
def reply(m):
    bot.send_chat_action(m.chat.id, 'typing')
    ai_answer = ask_ai(m.text)
    
    if ai_answer:
        bot.reply_to(m, ai_answer)
    else:
        # Fallback idan babu GROQ KEY
        bot.reply_to(m,
f"Tambayarka mai kyau ce: '{m.text}'\n\n"
"Don in zama cikakken malami mai amsa komai, sai an saka GROQ_API_KEY a Render.\n"
"Amma yanzu zan iya koya maka:\n"
"- Rubuta: Ina son Turanci\n"
"- Rubuta: Ina son Larabci\n"
"- Rubuta: Ina son Python")

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
