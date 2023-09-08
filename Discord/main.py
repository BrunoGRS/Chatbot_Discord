import discord
from discord.ext import commands, tasks
import datetime

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Estou pronto")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "palavrão" in message.content:
        await message.channel.send(f'Por favor, {message.author}, não ofenda os demais integrantes do discord')

        await message.delete()

    await bot.process_commands(message)

@bot.command(name="data")
async def send_date(ctx):
    data = datetime.datetime.now()
    formato = data.strftime("%d/%m/%Y as %H:%M:%S")
    channel = bot.get_channel(1149718651289735188)
    await channel.send(formato)

@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):

    string = "".join(expression)
    resposta = eval(string)

    await ctx.send(f"A resposta é: {str(resposta)}")

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    resposta = "Olá, " + name

    await ctx.send(resposta)


@bot.event
async def join_user(ctx):
    name = ctx.join.user

    mensagem = "Seja Bem - vindo " + name + "!"

    channel = bot.get_channel(1149718651289735188)

    await channel.send(mensagem)

bot.run("MTE0OTM3NzE5NzE0MDg4NTYwNQ.GEN6De._Z37vKKptbokVmX-ucBwL9EdK89t48Txkv6sds")