import discord
import requests
from discord.ext import commands

class Binance(commands.Cog):
    """Works with money"""
    
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(help="Traz a cotação de uma moeda. Precisa de 2 parâmetros (Moeda base/Moeda conversão)")
    async def binance(self, ctx, coin, base):
        
        embed = discord.Embed(title="Cotação",
            color= 0x0000FF)
        
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")

            if price:    
                embed.add_field(name="", value=f"O valor do par {coin}/{base} é $ {price}")
                await ctx.send(embed=embed)
            else: 
                embed.add_field(name="Resultado", value="Valor inválido")
                await ctx.send(embed=embed)
        except:
                await ctx.send("Ops.. Não consegui acessar a API")
        
def setup(bot):
    bot.add_cog(Binance(bot))