import discord
from discord.ext import commands

class Image(commands.Cog):
    """Create a random image"""
    
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name="imagem", help="Gera uma imagem aletória")
    async def create_image(self, ctx):
        
        url_imagem = "https://picsum.photos/1920/1080"
        embed = discord.Embed(title="Gerador de imagem", color=0x0000FF)
        
        embed.add_field(name="", value="Imagem gerada através de uma API")
        embed.set_image(url=url_imagem)
        
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Image(bot))