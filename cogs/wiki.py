from discord.ext import commands
import discord
from discord import app_commands
import requests

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="wiki", description="Durchsucht das SoT Wiki")
#Language Choice
    @app_commands.choices(language=[
        app_commands.Choice(name="Chinese (Simplified)", value="zh"),
        app_commands.Choice(name="Czech", value="cs"),
        app_commands.Choice(name="English", value="en"),
        app_commands.Choice(name="French", value="fr"),
        app_commands.Choice(name="German", value="de"),
        app_commands.Choice(name="Portuguese", value="pt"),
        app_commands.Choice(name="Spanish", value="es"),])
    
    async def wiki(self, interaction: discord.Interaction, search: str, page_anchor: str = None, language: app_commands.Choice[str] = None):
    #search formatting
        unformatted_search = search
        search = search.title()
        search = search.replace(" ", "_")

        search_text = "There is currently no text in this page. You can search for this page title in other pages, or search the related logs, but you do not have permission to create this page."

    #Check for Page Anchor
        if page_anchor == None:
            url = f"https://seaofthieves.fandom.com/wiki/{search}"
            combined_search = search
        elif page_anchor != None:
        #page anchor formatting
            unformatted_page_anchor = page_anchor
            page_anchor = page_anchor.title()
            page_anchor = page_anchor.replace(" ", "_")

            url = f"https://seaofthieves.fandom.com/wiki/{search}#{page_anchor}"
            combined_search = f"{search}#{page_anchor}"
    
    #Check for Language
        if page_anchor == "en":
            page_anchor = None
        elif language.value != None:
            url = f"https://seaofthieves.fandom.com/{language.value}/wiki/{combined_search}"
    #Check if Article exists
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            if search_text in page_content:
                await interaction.response.send_message(f"Geb bitte blubb Bescheid, wenn ich das hier ausgespuckt habe. Dann ist etwas mit mir falsch (Code: wiki03)") #ERROR CODE: wiki03
            else:
                await interaction.response.send_message(url)
    #That Article Doesn't Exist + Translations
        else:
        #Chinese (Simplified)
            if language.value == "zh":
                embed=discord.Embed(title="这篇文章并不存在。", 
                                    description=f"没有关于 **{search}** 的维基文章。确保拼写正确。您不必注意大小写，但一定不要忘记任何空格。", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Link to all articles", value="https://seaofthieves.fandom.com/zh/wiki/Special:%E6%89%80%E6%9C%89%E9%A1%B5%E9%9D%A2", inline=False)
        #Czech
            elif language.value == "cs":
                embed=discord.Embed(title="Tento článek neexistuje..", 
                                    description=f"Na wiki není **žádný** článek o **{search}**. Ujistěte se, že jste vše napsali správně. Nemusíte dbát na velká a malá písmena, ale ujistěte se, že jste nezapomněli na mezery.", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Odkaz na všechny články", value="https://seaofthieves.fandom.com/cs/wiki/Speci%C3%A1ln%C3%AD:V%C5%A1echny_str%C3%A1nky", inline=False)
        #French
            elif language.value == "fr":
                embed=discord.Embed(title="Cet article n'existe pas.", 
                                    description=f"Il n'y a **aucun** article wiki sur **{search}**. Assurez-vous que vous avez tout orthographié correctement. Vous n'avez pas besoin de faire attention aux majuscules et aux minuscules, mais assurez-vous de ne pas oublier d'espaces.", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Lien vers tous les articles", value="https://seaofthieves.fandom.com/fr/wiki/Sp%C3%A9cial:Toutes_les_pages", inline=False)
        #German"
            elif language.value == "de":
                embed=discord.Embed(title="Diesen Artikel gibt es nicht.", 
                                    description=f"Es gibt **keinen** Wiki-Artikel über **{search}**. Vergewisse dich bitte, dass du alles richtig geschrieben hast. Du musst nicht auf Groß- und Kleinschreibung achten, aber stelle bitte sicher, dass du keine Leerzeichen vergessen hast.", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Link zu allen Artikeln", value="https://seaofthieves.fandom.com/de/wiki/Spezial:Alle_Seiten", inline=False)
        #Portuguese
            elif language.value == "pt":
                embed=discord.Embed(title="Esse artigo não existe.", 
                                    description=f"Não existe **nenhum** artigo wiki sobre **{search}**. Certifica-te de que escreveste tudo corretamente. Não tens de prestar atenção às maiúsculas e minúsculas, mas certifica-te de que não te esqueces dos espaços..", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Ligação a todos os artigos", value="https://seaofthieves.fandom.com/pt/wiki/Especial:Todas_as_p%C3%A1ginas", inline=False)
        #Spanish
            elif language.value == "es":
                embed=discord.Embed(title="Ese artículo no existe.", 
                                    description=f"No hay **ningún** artículo wiki sobre **{search}**. Asegúrate de haber escrito todo correctamente. No tienes que prestar atención a las mayúsculas y minúsculas, pero asegúrate de no olvidar ningún espacio.", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Enlace a todos los artículos", value="https://seaofthieves.fandom.com/es/wiki/Especial:Todas", inline=False)
        #English (Default)
            else:
                embed=discord.Embed(title="That Article Doesn't Exist.", 
                                    description=f"There is **no** wiki article on **{search}**. Make sure you have spelled everything correctly. You don't have to pay attention to upper and lower case but make sure to not forget any spaces.", 
                                    color=0xc69c6d)
                embed.add_field(name="search", value=f"{unformatted_search}", inline=True)
                if page_anchor != None:
                    embed.add_field(name="page_anchor", value=f"{unformatted_page_anchor}", inline=True)
                elif page_anchor == None:
                    embed.add_field(name="page_anchor", value="-", inline=True)
                embed.add_field(name="Link to all articles", value="https://seaofthieves.fandom.com/wiki/Special:AllPages", inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Wiki(bot))
