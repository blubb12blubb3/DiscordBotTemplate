from discord.ext import commands
import discord
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Hiermit kannst du checken, ob und wie schnell der Bot erreichbar ist")
    async def ping(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message(f'Pong! Ich habe {round (self.bot.latency * 1000)} ms gebraucht, um zu antworten')
        except:
            await interaction.response.send_message(f'Der Bot konnte nicht erreicht werden oder blubb hat diesen Command kaputt gemacht')

async def setup(bot):
    await bot.add_cog(Ping(bot))
