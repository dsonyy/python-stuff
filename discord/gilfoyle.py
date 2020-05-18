import discord
import random

bot = discord.Client()

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(msg):
    if any(mention.id == bot.user.id for mention in msg.mentions) or "Gilfoyle" in msg.content:
        f = open("whatWouldGilfoyleSay.txt", "r")
        text = []
        for line in f: text.append(line)
        await msg.channel.send(random.choice(text))

bot.run('token')