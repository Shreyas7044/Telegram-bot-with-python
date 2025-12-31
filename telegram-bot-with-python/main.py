from telegram.ext import Updater, CommandHandler

# Replace YOUR_TOKEN_HERE with your BotFather token
TOKEN = "YOUR_TOKEN_HERE"

def hello(update, context):
    update.message.reply_text("Hello, World")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hello", hello))

    print("Bot is running... Press CTRL + C to stop")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()