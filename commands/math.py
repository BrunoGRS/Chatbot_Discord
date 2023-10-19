from discord.ext import commands

class Math(commands.Cog):
    """Calculate math operations"""
    
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name="calcular", help="Calcula uma expressão matemática")
    async def calculate_expression(self, ctx, *expression):
        string = "".join(expression)
        resposta = eval(string)

        await ctx.send(f"A resposta é: {str(resposta)}")
            
def setup(bot):
    bot.add_cog(Math(bot))