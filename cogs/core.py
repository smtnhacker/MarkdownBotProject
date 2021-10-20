import discord
from discord.ext import commands

import util.parsers as parsers
import util.image as imageUtil

class CoreCog(commands.Cog, name = 'core'):
  def __init__(self, bot):
    self.bot = bot
  
  @staticmethod
  async def _send_md2pdf(ctx, content):

    # remove invalid shortcuts
    content = content.replace('\\rarr', '\\rightarrow')
    print(content)

    if not 'numbered' in ctx.message.content:
      content = '\pagenumbering{gobble}\n' + content

    crop = False if 'uncrop' in ctx.message.content else True

    for idx, binary_pic in parsers.md2img(content):
      if crop:
        binary_pic = imageUtil.trimSpaces(binary_pic)
      picture = discord.File(fp=binary_pic, filename=f'img_{idx}.jpg')
      await ctx.channel.send(file=picture)
  
  @commands.command(aliases=['c'])
  async def conv(self, ctx):
    """
    Markdown Message to JPEG Conversion

    Command Format:
      ?conv [optional arguments]
      
      Possible arguments:
      - numbered
          Adds a page number to the bottom of the page. Make
          sure to add uncrop to ensure that the size is A4
      - uncrop
          Makes the image A4 sized
      
    Note: It is recommended to put the message in a markdown
    codeblock to ensure that TeXit does not catch LaTex snippets.
    It's quite annoying.
    """

    await ctx.channel.send('Please enter Markdown code:')
    msg = await self.bot.wait_for('message', timeout = 120)
    
    content_raw = msg.content
    
    # parse content
    if content_raw.startswith('```md'):
      content_raw = content_raw[5:]
      if content_raw.endswith('```'):
        content_raw = content_raw[:-3]
    
    try:
      await self._send_md2pdf(ctx, content_raw)
    except Exception as e:
      exception = f'{type(e).__name__}: {e}'
      print(exception)
      await ctx.channel.send('Invalid file. It might contain shortcuts not currently accounted for')
  
  @commands.command(aliases=['cc'])
  async def cconv(self, ctx):

    # get attachment
    try:
      binary = await ctx.message.attachments[0].read()
      content = binary.decode('utf-8').encode('ascii', 'ignore').decode('utf-8')

      await self._send_md2pdf(ctx, content)

    except Exception as e:
      exception = f'{type(e).__name__}: {e}'
      print(exception)
      await ctx.channel.send('Invalid file. It might contain shortcuts not currently accounted for')

def setup(bot):
    bot.add_cog(CoreCog(bot))
