import time

async def wait_response(bot, ctx, author, timeout):
    """Gets the response of the author.
    Waits for the response of the original sender for a
    given timeout interval and returns it, if it exists.
    Parameters
    -----------
    bot : discord.ext.commands.bot
        The discord bot!
    ctx : miniContext
        Contains important discord-related information
    author : abc.User
        Contains discord information on the author
    timeout : int
        Describes how long to wait, in seconds
    Returns
    ----------
    If the user is able to send a message fast enough, returns
    the message

    message : Message
    """

    timeout = timeout // 2 # account for double waiting
    end_time = time.perf_counter() + timeout
    while True:
        resp = await bot.wait_for('message', timeout=timeout)
        if resp.author == author:
            return resp
        if time.perf_counter() > end_time:
            break