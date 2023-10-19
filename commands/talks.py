import datetime
from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user"""
    
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name="data", help="Retorna a data e hora atual")
    async def send_date(self, ctx):
        data = datetime.datetime.now()
        formato = data.strftime("%d/%m/%Y as %H:%M:%S")
        channel = self.bot.get_channel(1149718651289735188)
        await channel.send(formato)
        
    @commands.command(name="oi", help="Diz oi.")
    async def send_hello(self, ctx):
        name = ctx.author.name
        resposta = "Olá, " + name
        await ctx.send(resposta)
            
def setup(bot):
    bot.add_cog(Talks(bot))