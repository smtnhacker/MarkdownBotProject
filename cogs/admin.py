from nextcord.ext import commands
import config

class AdminCog(commands.Cog, name = 'admin'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    async def load(self, ctx, extension):
        """Loads a module"""
        print(f'I recieved an order from my boss to load {extension}. Will try.')
        try:
            self.bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(config.MSG_COG_LOAD_ERROR.format(exception))
        else:
            print(config.MSG_COG_LOAD_SUCCESS.format(extension))
            await ctx.channel.send(config.MSG_COG_LOAD_SUCCESS.format(extension))
    
    @commands.command(hidden=True)
    async def unload(self, ctx, extension):
        """Unloads a module"""
        print(f'I recieved an order from my boss to unload {extension}. Will try.')
        try:
            self.bot.unload_extension(f'cogs.{extension}')
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(config.MSG_COG_UNLOAD_ERROR.format(extension, exception))
        else:
            print(config.MSG_COG_UNLOAD_SUCCESS.format(extension))
            await ctx.channel.send(config.MSG_COG_UNLOAD_SUCCESS.format(extension))
    
    @commands.command(hidden=True)
    async def reload(self, ctx, extension):
        """Reloads a module"""
        print(f'I recieved an order from my boss to reload {extension}. Will try.')
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            self.bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(config.MSG_COG_RELOAD_ERROR.format(extension, exception))
        else:
            print(config.MSG_COG_RELOAD_SUCCESS.format(extension))
            await ctx.channel.send(config.MSG_COG_RELOAD_SUCCESS.format(extension))

def setup(bot):
    bot.add_cog(AdminCog(bot))