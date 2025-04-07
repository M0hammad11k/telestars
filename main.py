from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8090137916:AAGIxEJJ0YyUkzFwXyxbJ_9iEkmCutT-CNo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 تلگرام پریمیوم", callback_data='premium')],
        [InlineKeyboardButton("⭐️ ارز استارز", callback_data='stars')]
    ]
    await update.message.reply_text("به ربات *تله‌استارز* خوش اومدی! یکی از گزینه‌ها رو انتخاب کن:", 
                                    parse_mode='Markdown', 
                                    reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'premium':
        premium_text = "اکانت تلگرام پریمیوم"
        premium_text += "▫️ ۳ ماهه: ۱,۴۰۰,۰۰۰ تومان"
        premium_text += "▫️ ۶ ماهه: ۱,۹۰۰,۰۰۰ تومان"
        premium_text += "▫️ یک ساله: ۳,۲۵۰,۰۰۰ تومان"
        await query.edit_message_text(premium_text, parse_mode='Markdown')
    
    elif query.data == 'stars':
        stars_text = "⭐️ *لیست استارز*"
        stars_text += "▫️ ۵۰ استارز: ۹۰,۰۰۰ تومان"
        stars_text += "▫️ ۷۵ استارز: ۱۲۵,۰۰۰ تومان"
        stars_text += "▫️ ۱۰۰ استارز: ۱۶۵,۰۰۰ تومان"
        stars_text += "▫️ ۱۵۰ استارز: ۲۴۵,۰۰۰ تومان"
        stars_text += "▫️ ۲۵۰ استارز: ۴۰۰,۰۰۰ تومان"
        stars_text += "▫️ ۳۵۰ استارز: ۵۵۵,۰۰۰ تومان"
        stars_text += "▫️ ۵۰۰ استارز: ۷۸۵,۰۰۰ تومان"
        stars_text += "▫️ ۷۵۰ استارز: ۱,۱۸۰,۰۰۰ تومان"
        stars_text += "▫️ ۱۰۰۰ استارز: ۱,۵۷۰,۰۰۰ تومان"
        await query.edit_message_text(stars_text, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("ربات آماده اجراست...")
    app.run_polling()