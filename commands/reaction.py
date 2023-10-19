import discord
from discord.ext import commands

class Reaction(commands.Cog):
    """Set a new guild"""
    
    def __init__(self, bot):
        self.bot=bot
               
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(843607311742009345)
            await user.add_roles(role)
        elif reaction.emoji == "🤟":
            role = user.guild.get_role(680232459362631719)
            await user.add_roles(role)
        elif reaction.emoji == "☠️":
            role = user.guild.get_role(801808711999029268)
            await user.add_roles(role)
            
    @commands.command(name="cargo", help="Distribui cargos")
    async def add_cargo(ctx):
        embed = discord.Embed(title="Cargos", description="Reaja para ganhar um cargo!!!", color=0x0000FF)
        embed.set_image(url='https://pin.it/4kRY0HG')
        embed.add_field(name="Emojis", value="Cargo 1 = 👍\n Cargo 2 = 🤟\n Cargo 3 = ☠️")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Reaction(bot))