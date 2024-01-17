import os
import discord,random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

mensaje = "Para memes de contaminacion auditiva pon meme1. Para memes de contaminacion hidrica pon meme2. Para memes de contaminacion marina pon meme3. Para memes de contaminacion urbana pon meme4"

bot = commands.Bot(command_prefix='/', intents=intents)

# @bot.command()
# async def meme(ctx):
#         # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
#         imagen = random.choice(os.listdir("images"))
#         with open(f"images/{imagen}","rb") as f:
#             meme = discord.File(f)
#             # A continuación, podemos enviar este archivo como parámetro.
#             await ctx.send(file=meme)

@bot.command()
async def meme(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        await ctx.send("Para memes de contaminacion auditiva pon meme1. Para memes de contaminacion hidrica pon meme2. Para memes de contaminacion marina pon meme3. Para memes de contaminacion urbana pon meme4")

@bot.command()
async def ayuda(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        await ctx.send("Para memes de contaminacion auditiva pon meme1. Para memes de contaminacion hidrica pon meme2. Para memes de contaminacion marina pon meme3. Para memes de contaminacion urbana pon meme4")

@bot.command()
async def meme1(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        imagen = random.choice(os.listdir("memes1"))
        with open(f"memes1/{imagen}","rb") as f:
            meme = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=meme)

@bot.command()
async def meme2(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        imagen = random.choice(os.listdir("memes2"))
        with open(f"memes2/{imagen}","rb") as f:
            meme = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=meme)

@bot.command()
async def meme3(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        imagen = random.choice(os.listdir("memes3"))
        with open(f"memes3/{imagen}","rb") as f:
            meme = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=meme)


@bot.command()
async def meme4(ctx):
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        imagen = random.choice(os.listdir("memes4"))
        with open(f"memes4/{imagen}","rb") as f:
            meme = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=meme)


bot.run("MTE4NzA5NjMzMTgzMjAwODgzNA.GmIyiA.JDj7lsg4a1xv8uRkDY3u3c9Yk7CUwcrZwnEkgw")