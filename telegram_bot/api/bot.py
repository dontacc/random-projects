import os
import django
import sys
import time
import asyncio

sys.path.append("/Users/mac/Desktop/pingi_task/user_authentication")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_authentication.settings")
django.setup()

from typing import Final
from telegram.ext import CommandHandler, MessageHandler, filters, Application, ContextTypes
from telegram import Update
from django.core.cache import cache


# commands
async def start_command(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '<b>Welcome to the Car Sales Listing Bot!\n'
        'Let\'s get some details about the car you\'re selling.\n'
        'What is your car type?</b>',
        parse_mode='HTML',
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لطفا پیام خود را بنویسید")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom command")


async def convert_message(update, context):
    user_id = update.message.from_user.id
    cache.set(user_id, {"is_waiting": True}, 20)
    # context.user_data[user_id] = "waiting_for_user"
    await update.message.reply_text("لطفا متن پیام خود را بنویسید")


class BotHandler:
    channel_id = "@pingi_arian"

    @staticmethod
    async def wait_and_delete(context, sent_message_id):
        await asyncio.sleep(5)
        await context.bot.delete_message(chat_id=BotHandler.channel_id, message_id=sent_message_id)

    @staticmethod
    async def delete_sender_message(context, message_id):
        await context.bot.delete_message(
            chat_id=BotHandler.channel_id,
            message_id=message_id
        )

    @staticmethod
    def handle_response(text: str, sender_first_name) -> tuple:
        text: list = text.split("\n")
        main_keys = ["اولویت", "عنوان", "توضیحات", "کاربر", "اطلاعات"]
        sender = "نام فرستنده " + sender_first_name
        if "" in text:
            text.remove("")

        if len(main_keys) == len(text):
            main_template = {key: value for key, value in zip(main_keys, text)}
            full_text = ""
            for key, value in main_template.items():
                full_text += f"<b>{key}</b>: {value}\n"

            return True, (full_text + sender)
        else:
            warning_text = "ساختار متن باید به این صورت باشد"
            keys = ""
            for key in main_keys:
                keys += f"{key}:\n"

            return False, f"⚠️\n<b>{warning_text}\n{keys}\n{sender}</b>\n⚠️"

    @staticmethod
    async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
        sender_first_name = update.channel_post.author_signature
        sender_message_id = update.channel_post.message_id
        channel_id = "@pingi_arian"

        if update.channel_post.photo:
            text_from_channel = update.channel_post.caption
            file_id = update.channel_post.photo[-1].file_id
            status, response = BotHandler.handle_response(text_from_channel, sender_first_name)
            if status:
                await context.bot.send_photo(
                    chat_id=channel_id,
                    photo=file_id,
                    caption=response,
                    parse_mode="HTML"
                )
                await BotHandler.delete_sender_message(context, message_id=sender_message_id)
            else:
                sent_message = await context.bot.send_message(
                    chat_id=channel_id,
                    text=response,
                    parse_mode="HTML",
                )
                await BotHandler.delete_sender_message(context, message_id=sender_message_id)
                await asyncio.create_task(BotHandler.wait_and_delete(context, sent_message.id))
        else:
            text_from_channel = update.channel_post.text
            status, response = BotHandler.handle_response(text_from_channel, sender_first_name)
            sent_message = await context.bot.send_message(
                chat_id="@pingi_arian",
                text=response,
                parse_mode="HTML",
            )
            await BotHandler.delete_sender_message(context, message_id=sender_message_id)

            if status is not True:
                asyncio.create_task(BotHandler.wait_and_delete(context, sent_message.id))


Token: Final = "7790012955:AAGJIGPz-75X3iBlJ7KI4rLiW7-N2ErQvCU"
app = Application.builder().token(Token).build()
print("app is running")
# Commands
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("custom", custom_command))
app.add_handler(CommandHandler("convertor", convert_message))

# Messages
app.add_handler(MessageHandler(filters.PHOTO, BotHandler.handle_message))
app.add_handler(MessageHandler(filters.TEXT, BotHandler.handle_message))
print("polling ...")
app.run_polling(poll_interval=1)
