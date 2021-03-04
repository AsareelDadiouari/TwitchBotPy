from twitchio.ext import commands
import os
from googletrans import Translator
import re

language = 'fr' # re.findall(r"[\w']+", open('settings.ini').read())[1]
translator = Translator()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=os.environ["TWITCH_OAUTH_TOKEN"], client_id=os.environ["TWITCH_CLIENT_ID"],
                         nick=os.environ['TWITCH_BOT_NAME'], prefix='!',
                         initial_channels=[os.environ['TWITCH_CHANNEL']])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'{self.nick} | ' + translator.translate(f"Logged into Twitch", dest={language}).text)
        await self.get_channel(os.environ['TWITCH_CHANNEL']).send(
            translator.translate(f"Welcome to my Stream", dest={language}).text)

    async def event_message(self, message):
        print(message.author.name + ' : ' + message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')
