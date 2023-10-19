from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from discord.ext import commands

class Manager(commands.Cog):
    """Manage the bot"""
    
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Estou pronto")

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author == self.bot.user:
            return
        
        if 'palavrão' == message:
            await message.channel.send(f'Por favor, {message.author}, não ofenda os demais integrantes do discord')
            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Por favor informe todos os parâmetros necessários do comando!. Digite !help para mais auxilio.")
        if isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe!. Digite !help para mais auxilio.")
        else:
            raise error
             
def setup(bot):
    bot.add_cog(Manager(bot))