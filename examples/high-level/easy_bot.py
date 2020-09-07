from vkbottle.bot import Bot, Message
import os

bot = Bot(os.environ["token"])

@bot.on.message(text="/съесть <item>")
async def vbml_handler(message: Message, item: str):
    await message.answer(f"Ты съел <<{item}>>!")

bot.run_forever()
