import discord
import requests
from Utils.DefaultConfig import default_config
import json
import os
import random
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['changeembedcolor', 'embedcolor', 'chem'])
    async def changecolor(self, ctx, color):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if '#' in color:

            f = color.replace('#', '0x')
  
            sv['server'][str('embedcolor')] = f
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'Nuevo color cambiado! **{color}**'
            )
            embed.set_footer(text='Color cambiado por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        elif color == 'random':
            colors = [
                "0xFFE4E1",
                "0x00FF7F",
                "0xD8BFD8", 
                "0xDC143C", 
                "0xFF4500", 
                "0xDEB887", 
                "0xADFF2F", 
                "0x800000", 
                "0x4682B4", 
                "0x006400", 
                "0x808080", 
                "0xA0522D", 
                "0xF08080", 
                "0xC71585", 
                "0xFFB6C1", 
                "0x00CED1"
            ]

            get_color = random.choice(colors)

            sv['server'][str('embedcolor')] = str(get_color)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'Nuevo color cambiado! **{get_color}**'
            )
            embed.set_footer(text='Color cambiado por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif '0x' in color:
            sv['server'][str('embedcolor')] = color
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'Nuevo color cambiado! **{color}**'
            )
            embed.set_footer(text='Color cambiado por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        else:
            await ctx.send('Opcion invalida!')

    @commands.command()
    async def changeprefix(self, ctx, prefix):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        sv['server'][('prefix')] = prefix

        with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
            json.dump(sv, f, indent=4)            

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'Mi nuevo prefix en este servidor es **{prefix}**\n\nRecuerda usar **{prefix}help** para usar mis comandos.'
        )
        embed.set_footer(text=f'Prefix cambiado por: {ctx.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def serversettings(self, ctx):
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)


        em = sv['server']['embedcolor']

        f = em.replace('0x', '#')

        embed = discord.Embed(
            title = f'Configuracion de {ctx.guild.name}',
            color = int(sv['server']['embedcolor'], 16),
            description = f'''

            `::` Server name: {ctx.guild.name}
            `::` Server ID: {ctx.guild.id}
            `::` Owner: {ctx.guild.owner}
            `::` Region: {ctx.guild.region}

            `::` Canales de texto: {text_channels}
            `::` Canales de boz: {voice_channels}
            `::` Categorias: {categories}
            `::` Todos los canales: {channels}

            `::` Embedcolor [Hexcolor]: {f}
            `::` Prefix: {sv.get('prefix')}
            '''
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text='Peticion de {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        try:
            await ctx.author.send(embed=embed)      
        except:
            await ctx.send(f'{ctx.author.mention} Oye, tienes los mensajes privados desactivados, necesitas activarlos para poder usar este comando!')

    @commands.command()
    async def poll(self, ctx, *, arg):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except FileNotFoundError:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        poll_numbers = int(sv['moderation']['poll'])
        poll_numbers += 1

        sv['moderation']['poll'] = poll_numbers

        with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
            json.dump(sv, f, indent=4)
        
        embed = discord.Embed(
            title = f'Votacion! - #' + str(sv['moderation']['poll']),
            color = int(sv['server']['embedcolor'], 16),
            description = arg
        )
        embed.set_footer(text='Votacion iniciada por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        poll = await ctx.send(embed=embed)
        await poll.add_reaction('✅')
        await poll.add_reaction('❌')

    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except FileNotFoundError:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
            
        if user is None:
            user = ctx.author

        avatar = str(user.avatar_url_as(static_format="png", size=1024))

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.set_image(url=avatar)
        embed.set_author(name=f'Avatar de: {user}', icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(user), icon_url=user.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utils(bot))