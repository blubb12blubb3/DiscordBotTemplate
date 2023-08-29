import discord
from discord.ext import commands

class NeinDoch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None
        self.nein_user = None

    @commands.Cog.listener() # Das gleiche wie in bot.event
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower() == 'nein':
            if self.last_user != message.author:
                self.nein_user = message.author
                self.last_user = message.author

        elif message.content.lower() == 'doch': # Check for "Doch"
            if self.nein_user == self.last_user and self.last_user != message.author: # 2 Person check
                await message.channel.send('Oh!')
                self.last_user = None
                self.nein_user = None

async def setup(bot): # Cog Setup
    await bot.add_cog(NeinDoch(bot))