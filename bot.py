import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать!\n\n"
        "⚽ EF27tj — официальный бот канала.\n"
        "🔥 Бот работает!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Команды:\n"
        "/start — запустить бота\n"
        "/help — помощь"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 EF27tjBot запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()