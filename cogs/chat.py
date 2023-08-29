from discord.ext import commands
import discord
from discord import app_commands
import openai
import os


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="chat", description="ChatGPT")
    async def chat(self, interaction: discord.Interaction, user_question: str):
        openai.api_key = "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"

        response = openai.Completion.create(
            engine="davinci",  # You can experiment with different engines
            prompt=user_question,
            max_tokens=50  # Adjust the response length as needed
        )
        bot_response = response.choices[0].text.strip()
        await interaction.response.send_message(bot_response)
        

async def setup(bot):
    await bot.add_cog(Chat(bot))

