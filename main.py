import os, sys, asyncio, platform
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

import config

bot = commands.Bot(command_prefix=config.BOT_PREFIX)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="?start"))

@bot.command()
async def start(ctx):
  embed = nextcord.Embed(
    title = "Welcome to Markdown to Image",
    color = 0xecffa8,
  )
  embed.add_field(
    name = "Command:",
    value = "`?conv` - to start converting",
    inline = False,
  )
  embed.set_author(name='Chamba Bois')
  await ctx.send(embed = embed)

if __name__ == '__main__':
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      extension = file[:-3]
      try:
        bot.load_extension(f'cogs.{extension}')
        print(config.MSG_COG_LOAD_SUCCESS.format(extension))
      except Exception as e:
        exception = f"{type(e).__name__}: {e}"
        print(config.MSG_COG_LOAD_ERROR.format(extension, exception))
  load_dotenv()
  bot.run(os.environ['TOKEN'])
