from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
DESTINATION_CHANNEL_ID = int(os.getenv("DESTINATION_CHANNEL_ID"))

async def clone_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg:
        return

    if msg.text:
        await context.bot.send_message(
            chat_id=DESTINATION_CHANNEL_ID,
            text=msg.text,
            entities=msg.entities
        )

    elif msg.photo:
        await context.bot.send_photo(
            chat_id=DESTINATION_CHANNEL_ID,
            photo=msg.photo[-1].file_id,
            caption=msg.caption,
            caption_entities=msg.caption_entities
        )

    elif msg.video:
        await context.bot.send_video(
            chat_id=DESTINATION_CHANNEL_ID,
            video=msg.video.file_id,
            caption=msg.caption,
            caption_entities=msg.caption_entities
        )

    elif msg.voice:
        await context.bot.send_voice(
            chat_id=DESTINATION_CHANNEL_ID,
            voice=msg.voice.file_id
        )

    elif msg.audio:
        await context.bot.send_audio(
            chat_id=DESTINATION_CHANNEL_ID,
            audio=msg.audio.file_id,
            caption=msg.caption
        )

    elif msg.document:
        await context.bot.send_document(
            chat_id=DESTINATION_CHANNEL_ID,
            document=msg.document.file_id,
            caption=msg.caption
        )

    elif msg.sticker:
        await context.bot.send_sticker(
            chat_id=DESTINATION_CHANNEL_ID,
            sticker=msg.sticker.file_id
        )

    elif msg.poll:
        await context.bot.send_poll(
            chat_id=DESTINATION_CHANNEL_ID,
            question=msg.poll.question,
            options=[o.text for o in msg.poll.options],
            is_anonymous=msg.poll.is_anonymous,
            allows_multiple_answers=msg.poll.allows_multiple_answers
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.Chat(SOURCE_CHANNEL_ID), clone_message))
    app.run_polling()
