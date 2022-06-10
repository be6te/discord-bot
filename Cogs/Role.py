import discord
import json
import random
import animec
import requests
from Utils.DefaultConfig import default_config
from discord.ext import commands
from main import bot

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = '852754636615188483.8aijgBUc92Nk8lnBF15v'
        
        self.shoot_endpoint = [
            'https://www.beete.xyz/gif/shoot/shoot1.gif',
            'https://www.beete.xyz/gif/shoot/shoot2.gif',
            'https://www.beete.xyz/gif/shoot/shoot3.gif',
            'https://www.beete.xyz/gif/shoot/shoot4.gif',
            'https://www.beete.xyz/gif/shoot/shoot5.gif',
            'https://www.beete.xyz/gif/shoot/shoot6.gif',
            'https://www.beete.xyz/gif/shoot/shoot7.gif',
            'https://www.beete.xyz/gif/shoot/shoot8.gif',
            'https://www.beete.xyz/gif/shoot/shoot9.gif',
            'https://www.beete.xyz/gif/shoot/shoot10.gif',
            'https://www.beete.xyz/gif/shoot/shoot11.gif',
            'https://www.beete.xyz/gif/shoot/shoot12.gif',
            'https://www.beete.xyz/gif/shoot/shoot13.gif'
        ]

        self.kill_endpoint = [
            'https://www.beete.xyz/gif/Kill/Kill.gif',
            'https://www.beete.xyz/gif/Kill/Kill2.gif',
            'https://www.beete.xyz/gif/Kill/Kill3.gif',
            'https://www.beete.xyz/gif/Kill/Kill4.gif',
            'https://www.beete.xyz/gif/Kill/Kill5.gif',
            'https://www.beete.xyz/gif/Kill/Kill6.gif',
            'https://www.beete.xyz/gif/Kill/Kill7.gif'
        ]

        self.peek_endpoint = [
            'https://www.beete.xyz/gif/Peek/Peek1.gif',
            'https://www.beete.xyz/gif/Peek/Peek2.gif',
            'https://www.beete.xyz/gif/Peek/Peek3.gif',
            'https://www.beete.xyz/gif/Peek/Peek4.gif',
            'https://www.beete.xyz/gif/Peek/Peek5.gif',
            'https://www.beete.xyz/gif/Peek/Peek6.gif',
            'https://www.beete.xyz/gif/Peek/Peek7.gif'
        ]

    def database(self, userid=None, data=None, authorid=None):
        
        if (data is None):
            return
        elif (userid is None):
            userid = 'None'
        elif (authorid is None):
            authorid = 'None'
        elif data == data:
            with open('Database/kiss-{}'.format(authorid)) as f:
                json.dump(data, f)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):

        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            kiss = lan.get('kiss')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            kiss = lan.get('kiss')

        print(kiss)

        kissemoji = [
            ':smiling_face_with_3_hearts:',
            ':heart_eyes:',
            ':kissing_heart:'
        ]

        randomemoji = [
            'O-o',
            'uwu',
            'O.o',
            'owo',
            'nwn'
        ]

        if (user is None):
            await ctx.reply('Necesitas mencionar a un usuario!', delete_after=5)
        elif (user == ctx.author):
            await ctx.reply('No puedes besarte a ti mismo!', delete_after=5)
        elif (user == bot):
            await ctx.reply('Necesitas mencionar a un usuario!')
        else:
            r = requests.get('https://nekos.best/api/v2/kiss').json()
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'**{ctx.author.name}** {kiss} **{user.name}** {random.choice(kissemoji)}'
            )
            embed.set_image(url=r['results'][0]['url'])
            embed.set_footer(text='Anime: {}'.format(r['results'][0]['anime_name']))
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            s = lan.get('slap')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            s = lan.get('slap')

        if (user is None):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == ctx.author):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == self.bot):
            await ctx.reply('Necesitas mencionar a un usuario!')
        else:
            r = requests.get('https://api.waifu.pics/sfw/slap').json()
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'**{ctx.author.name}** {s} **{user.name}**'
            )
            embed.set_image(url=r['url'])
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            p = lan.get('pat')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            p = lan.get('pat')

        if (user is None):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == ctx.author):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == self.bot):
            await ctx.reply('Necesitas mencionar a un usuario!')
        else:
            r = requests.get('https://api.waifu.pics/sfw/pat').json()
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'**{ctx.author.name}** {p} **{user.name}**'
            )
            embed.set_image(url=r['url'])
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            h = lan.get('hug')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            h = lan.get('hug')

        if (user is None):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == ctx.author):
            await ctx.reply('Necesitas mencionar a un usuario!')
        elif (user == self.bot):
            await ctx.reply('Necesitas mencionar a un usuario!')
        else:
            r = requests.get('https://api.waifu.pics/sfw/hug').json()
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'**{ctx.author.name}** {h} **{user.name}** ^^'
            )
            embed.set_image(url=r['url'])
            await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            cry = lan.get('cry')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            cry = lan.get('cry')

        sad = [
            'T-T',
            ':(',
            ';('
        ]

        r = requests.get('https://nekos.best/api/v2/cry').json()

        image = r['results'][0]['url']
        name = r['results'][0]['anime_name']
            
        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'**{ctx.author.name}** {cry} {random.choice(sad)}'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)

    @commands.command()
    async def smile(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            s = lan.get('smile')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            s = lan.get('smile')

        r = requests.get('https://nekos.best/api/v2/smile').json()

        image = r['results'][0]['url']
        name = r['results'][0]['anime_name']
            
        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'**{ctx.author.name}** {s} :D'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)
        
    @commands.command()
    async def blush(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            kiss = lan.get('blush')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            kiss = lan.get('blush')

        r = requests.get('https://nekos.best/api/v2/blush').json()

        image = r['results'][0]['url']
        name = r['results'][0]['anime_name']
            
        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'**{ctx.author.name}** {kiss} >.<'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)        

    @commands.command()
    async def happy(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            kiss = lan.get('happy')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            kiss = lan.get('happy')

        r = requests.get('https://api.waifu.pics/sfw/happy').json()
            
        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'**{ctx.author.name}** {kiss} :D'
        )
        embed.set_image(url=r['url'])
        await ctx.send(embed=embed)         

    @commands.command()
    async def dance(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            kiss = lan.get('dance')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            kiss = lan.get('dance')

        res = requests.get('https://nekos.best/api/v2/dance')
        data = res.json()

        image = data['results'][0]['url']
        name = data['results'][0]['anime_name']
            
        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'**{ctx.author.name}** {kiss}'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)

    @commands.command(aliases=['jojopos', 'jojospos', 'jjpos'])
    async def jpos(self, ctx):

        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open(f'Languages/Translate-Roleplay-Spanish.json') as f:
                lan = json.load(f)
            kiss = lan.get('jj')
        elif sv['server']['language'] == 'english':
            with open(f'Languages/Translate-Roleplay-English.json') as f:
                lan = json.load(f)
            kiss = lan.get('jj')

        jj = [
            'https://c.tenor.com/jsePRK8H_AkAAAAC/giorno-pose-hd-jojos-bizarre-adventure.gif',
            'https://c.tenor.com/K0qWzvdy1GgAAAAC/josuke-pose.gif',
            'https://images-ext-1.discordapp.net/external/qJFZWID_jCqNd4V0lNiIcPV3pL9MQvMNYvG1ZvZgtdc/https/nekocdn.com/images/NIZLjGgK.gif',
            'https://images-ext-2.discordapp.net/external/otfPc9CUmAtiPNx7W5yaJFUd-L22iDFuWhCa8kSd2R0/https/nekocdn.com/images/_-fM26_t.gif',
            'https://images-ext-2.discordapp.net/external/Qtf4-d9z_DuLvpj17_hy-BJOawJEd3X9cgH5gz-NY1E/https/nekocdn.com/images/LtydELxp.gif',
            'https://images-ext-1.discordapp.net/external/3wgjHVIl5RdTkyyTuBwKdpj0lFA8hxeZVrLfuLBCzIM/https/nekocdn.com/images/FXR5XoEif.gif',
            'https://images-ext-2.discordapp.net/external/N5beS02_juA69I08y3akEPZ41z0Ca5d0bgc8BTFcyA8/https/nekocdn.com/images/xKlpPOJ4.gif',
            'https://images-ext-2.discordapp.net/external/Xc2u2cj9apuMBDeADCcN4mSTCAE_g7F2IjA5zo5h4Sw/https/nekocdn.com/images/5n4wtl7m.gif'
        ]

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f"**{ctx.author.name}** {kiss}"
        )
        embed.set_image(url=random.choice(jj))
        await ctx.send(embed=embed)

    @commands.command(aliases=['anisearch', 'animesearch'])
    async def anime(self, ctx, *, name):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        embed = discord.Embed(
          color = int(sv['server']['embedcolor'], 16),
          description = f'Buscando... :mag:'
        )
        first = await ctx.send(embed=embed)
        try:
          anime = animec.Anime(name)
        except:
          await first.edit(embed=discord.Embed(description = "No pude encontrar el anime que buscabas :(", color=discord.Color.red()))
        else:
          embed = discord.Embed(title=f"{anime.title_jp}\n{anime.title_english}", url=anime.url, description=f"{anime.description[:300]}...", color=int(sv['server']['embedcolor'], 16))
          embed.add_field(name="Episodios:", value=(anime.episodes))
          embed.add_field(name="Clasificacion:", value=str(anime.rating))
          embed.add_field(name="Posicion:", value=str(anime.ranked))
          embed.add_field(name="Condicion:", value=str(anime.status))
          embed.add_field(name="Genero:", value=', '.join((anime.genres)))
          embed.add_field(name="Tipo de anime:", value=str(anime.type))
          
          embed.set_thumbnail(url=anime.poster)
          await first.edit(embed=embed)

    @commands.command()
    async def shoot(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        embed = discord.Embed(
            description = f'{ctx.author.mention} le disparo a {user.mention}',
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.set_footer(text='Powered by beete.xyz')
        embed.set_image(url=random.choice(self.shoot_endpoint))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def kill(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        embed = discord.Embed(
            description = f'{ctx.author.mention} Acaba de matar a {user.mention}',
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.set_footer(text='Powered by beete.xyz')
        embed.set_image(url=random.choice(self.kill_endpoint))
        await ctx.send(embed=embed)

    @commands.command()
    async def peek(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        embed = discord.Embed(
            description = f'{ctx.author.mention} Esta observando -_-',
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.set_footer(text='Powered by beete.xyz')
        embed.set_image(url=random.choice(self.peek_endpoint))
        await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        
        if (user is None):
            await ctx.send('Necesitas mencionar a un usuario', after_delete=5)
        else:

            res = requests.get('https://nekos.best/api/v2/punch')
            data = res.json()

            image = data['results'][0]['url']
            name = data['results'][0]['anime_name']

            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{ctx.author.mention} Le dio un golpe a {user.mention}'
            )
            embed.set_image(url=image)
            embed.set_footer(text='Anime: {}'.format(name))
            await ctx.send(embed=embed)

    @commands.command()
    async def sleep(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://nekos.best/api/v2/sleep')
        data = res.json()

        image = data['results'][0]['url']
        name = data['results'][0]['anime_name']

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Se durmio :zzz:'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)

    @commands.command()
    async def think(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://nekos.best/api/v2/think')
        data = res.json()

        image = data['results'][0]['url']
        name = data['results'][0]['anime_name']

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Esta pensando...'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)

    @commands.command()
    async def laugh(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://nekos.best/api/v2/laugh')
        data = res.json()

        image = data['results'][0]['url']
        name = data['results'][0]['anime_name']

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Se esta riendo'
        )
        embed.set_image(url=image)
        embed.set_footer(text='Anime: {}'.format(name))
        await ctx.send(embed=embed)

    @commands.command()
    async def confused(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://kawaii.red/api/gif/confused/token={}/'.format(self.token))
        data = res.json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Esta confundido/a'
        )
        embed.set_image(url=data['response'])
        await ctx.send(embed=embed)              

    @commands.command()
    async def run(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://kawaii.red/api/gif/run/token={}/'.format(self.token))
        data = res.json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Salio corriendo'
        )
        embed.set_image(url=data['response'])
        await ctx.send(embed=embed)     

    @commands.command()
    async def scared(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        res = requests.get('https://kawaii.red/api/gif/scared/token={}/'.format(self.token))
        data = res.json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'{ctx.author.mention} Esta asustado/a'
        )
        embed.set_image(url=data['response'])
        await ctx.send(embed=embed)    

    @commands.command()
    async def fight(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if user == None:
            await ctx.reply('Necesitas mencionar a un usuario para usar este comando!', delete_after=5)
        else:       
            res = requests.get('https://kawaii.red/api/gif/fight/token={}/'.format(self.token))
            data = res.json()
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{ctx.author.mention} Esta peleando con {user.mention}'
            )
            embed.set_image(url=data['response'])
            await ctx.send(embed=embed)    

def setup(bot):
    bot.add_cog(Roleplay(bot))            