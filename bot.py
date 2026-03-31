import telebot
import requests
import time

# আপনার দেওয়া তথ্য
TOKEN = '8667658046:AAEk5zCrSbRmI02wVwnAw0tVHwuMI2QtoEY'
MY_CHAT_ID = '7416528268'

bot = telebot.TeleBot(TOKEN)

def get_market_analysis():
    # এটি একটি ডেমো অ্যানালাইসিস লজিক
    # ভবিষ্যতে এখানে আসল মার্কেট ডেটার লিঙ্ক বসানো যাবে
    return {
        "pair": "EUR/USD",
        "signal": "BUY (UP) 🟢",
        "time": "1 MIN",
        "confidence": "80%"
    }

def start_bot():
    print("বট চালু হয়েছে...")
    while True:
        try:
            analysis = get_market_analysis()
            
            message = (
                f"📊 **QUOTEX AUTO SIGNAL**\n"
                f"━━━━━━━━━━━━━━━━━━\n"
                f"💎 **Market:** `{analysis['pair']}`\n"
                f"📈 **Action:** {analysis['signal']}\n"
                f"⏳ **Duration:** {analysis['time']}\n"
                f"🎯 **Confidence:** {analysis['confidence']}\n"
                f"━━━━━━━━━━━━━━━━━━\n"
                f"📢 *এখনই ট্রেড নিন (Demo Account)*"
            )
            
            bot.send_message(MY_CHAT_ID, message, parse_mode='Markdown')
            
            # প্রতি ৫ মিনিট পরপর সিগন্যাল পাঠাবে (আপনি চাইলে সময় কমাতে পারেন)
            time.sleep(300) 
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    start_bot()
