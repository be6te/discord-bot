import discord
import random
import json
import json
from Utils.DefaultConfig import default_config
from discord.ext import commands
from googleapiclient.discovery import build
from googletrans import Translator

class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = 'AIzaSyCe_z6ou-41H0u7HS-hHtGaRx1GUyUiiLI'

    @commands.command()
    async def ggsearch_(self, ctx, *, search):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        
        bad_works = [
            "tits",
            "boobs",
            "fuck",
            "fuck niggers",
            "lana rhoades",
            "fucking",
            "bitch",
            "dick",
            "penis",
            "pene",
            "culo",
            "vagina",
            "tetas",
            "blowjob",
            "hentai",
            "ass"
        ]

        if ''.join(bad_works) in search:
            await ctx.send('No puedes buscar esto!')
        else:
            
            ran = random.randint(0, 10)
            
            resource = build("customsearch", "v1", developerKey=self.key).cse()
            result = resource.list(
                q=f"{search}", cx="ab93645237db9c697", searchType="image"
            ).execute()
            
            url = result["items"][ran]["link"]
            
            embed = discord.Embed(
                title = result['items'][ran]['title'],
                color = int(sv['server']['embedcolor'], 16),
                description = f"[{result['items'][ran]['title']}]({result['items'][ran]['link']})"
            )
            embed.set_image(url=url)
            msg = await ctx.send(embed=embed)
    
    @commands.command()
    async def translate(self, ctx, language, *, message):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        translator = Translator()
        translation = translator.translate(message, dest=language)

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'''**Mensaje original:**\n```{message}```\n**Traduccion:**\n```{translation.text}```
            '''
        )
        embed.set_author(name='Google Translate', icon_url=r'https://icon-library.com/images/google-icon/google-icon-26.jpg')
        embed.set_footer(text='Traducido a: {}'.format(language))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Google(bot))