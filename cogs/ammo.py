from discord.ext import commands
import discord
from discord import app_commands


class Ammo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ammo", description="Tip for SoT")
    async def ammo(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Embed Title", description="Embed Description", color=0x8f8f8f)
        #embed.set_author(name="blubb12blubb3", url="http//youtube.com", icon_url="https://seaofthieves.fandom.com/wiki/Fortune_Emote_Set?file=Fortune_Emote_Set.png")
        embed.set_image(url="./images/yarr.png")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Ammo(bot))