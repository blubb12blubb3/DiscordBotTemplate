from discord.ext import commands
import discord
from discord import app_commands


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Add Reactions for Polls")
    async def poll(self, interaction: discord.Interaction, msg: str):

        #check for a link and extract the message id
        if "discord" in msg:
            message_link = msg
            # Split the URL by slashes
            segments = msg.split("/")
            # Get the last segment (which is the string of numbers you want)
            msg = segments[-1]
        else:
            message_link = (f"https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{msg}")

        try:
            message = await self.bot.get_channel(interaction.channel_id).fetch_message(int(msg))
            await message.add_reaction(':white_check_mark:')
            await message.add_reaction(':negative_squared_cross_mark:')
            #add more reactions here if you want)
            await interaction.response.send_message(f"Command executed on message: {message_link}", ephemeral=True)
        except:
            await interaction.response.send_message(f"Command failed on message: {message_link}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Poll(bot))
