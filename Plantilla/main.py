import os
import discord,random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def meme(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        imagen = random.choice(os.listdir(f"meme_bot/images"))
        with open(f"meme_bot/images/{imagen}","rb") as f:
            meme = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=meme)

bot.run("TOKEN")