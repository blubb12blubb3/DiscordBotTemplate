from discord.ext import commands
import discord
from discord import app_commands


class Abstimmung(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="abstimmung", description="Reagiert auf gewollte Nachricht mit Emojis")
    async def abstimmung(self, interaction: discord.Interaction, message_id: str):
        try:
            message = await self.bot.get_channel(interaction.channel_id).fetch_message(int(message_id))
            await message.add_reaction(':yes:1141686591853703218')
            await message.add_reaction(':no:1141686610723876975')
            await interaction.response.send_message("Command ausgeführt", ephemeral=True)
        except:
            await interaction.response.send_message("Command fehlgeschlagen", ephemeral=True)
        #falls ich noch was senden möchte response.followup

async def setup(bot):
    await bot.add_cog(Abstimmung(bot))
