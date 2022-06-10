import discord
import requests
import json

from Utils.DefaultConfig import default_config
from discord.ext import commands

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mcp(self, ctx, *, name):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
    
        get_uuid = requests.get('https://api.ashcon.app/mojang/v2/user/{}'.format(name)).json()
        uuid = get_uuid['uuid']
        req = requests.get('https://api.slothpixel.me/api/players/{}'.format(uuid)).json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.set_thumbnail(url='https://mc-heads.net/head/{}'.format(name))
        embed.set_author(name='{}'.format(get_uuid['username']), icon_url='https://mc-heads.net/head/{}'.format(name))

        embed.add_field(name='Username:', value=req['username'], inline=False)
        embed.add_field(name='Usernames:', value=' > '.join(req['name_history']), inline=False)
        embed.add_field(name='UUID:', value=req['uuid'], inline=False)
        embed.add_field(name='Skin slim:', value=get_uuid['textures']['slim'], inline=False)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def hypixel(self, ctx, *, name):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
    
        get_uuid = requests.get('https://api.ashcon.app/mojang/v2/user/{}'.format(name)).json()
        uuid = get_uuid['uuid']
        req = requests.get('https://api.slothpixel.me/api/players/{}'.format(uuid)).json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16)
        )

        rank = str(req['rank'])

        if '_PLUS' in rank:
            rank = rank.replace('_PLUS', '+')

        embed.set_thumbnail(url='https://mc-heads.net/head/{}'.format(name))
        embed.set_author(name='{}'.format(get_uuid['username']), icon_url='https://mc-heads.net/head/{}'.format(name))

        embed.add_field(name='Username:', value=req['username'], inline=True)
        embed.add_field(name='Online:', value=req['online'], inline=True)
        embed.add_field(name='Rank:', value=rank, inline=True)
        embed.add_field(name='Karma:', value=int(req['karma']), inline=True)
        embed.add_field(name='EXP:', value=int(req['exp']), inline=True)
        embed.add_field(name='Total Coins:', value=int(req['total_coins']), inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def bedwards(self, ctx, *, name):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
    
        get_uuid = requests.get('https://api.ashcon.app/mojang/v2/user/{}'.format(name)).json()
        uuid = get_uuid['uuid']
        req = requests.get('https://api.slothpixel.me/api/players/{}'.format(uuid)).json()

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16)
        )

        embed.set_thumbnail(url='https://mc-heads.net/head/{}'.format(name))
        embed.set_author(name='{}'.format(get_uuid['username']), icon_url='https://mc-heads.net/head/{}'.format(name))

        rank = str(req['rank'])

        if '_PLUS' in rank:
            rank = rank.replace('_PLUS', '+')

        embed.add_field(name='Username:', value=req['username'], inline=True)
        embed.add_field(name='Online:', value=req['online'], inline=True)
        embed.add_field(name='Rank:', value=rank, inline=True)
        embed.add_field(name='Level:', value=int(req['stats']['BedWars']['level']))
        embed.add_field(name='Coins:', value=int(req['stats']['BedWars']['coins']))
        embed.add_field(name='EXP:', value=int(req['stats']['BedWars']['exp']))
        embed.add_field(name='Wins:', value=int(req['stats']['BedWars']['wins']))
        embed.add_field(name='Losses:', value=int(req['stats']['BedWars']['losses']))
        embed.add_field(name='Games played:', value=int(req['stats']['BedWars']['games_played']))
        embed.add_field(name='Kills:', value=int(req['stats']['BedWars']['kills']))
        embed.add_field(name='Deaths:', value=int(req['stats']['BedWars']['deaths']))

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Minecraft(bot))