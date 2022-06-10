from datetime import datetime
import json
import requests
from pathlib import WindowsPath
from Utils.DefaultConfig import default_config
from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures
import os

dagpi = Client('MTY0NDE1MTQ5NQ.GqXwoPixc5N5Ht4zsnhC3q2MofiTPFQW.1ba02efc6c2c2731')

class img(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def pixel(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.pixel(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def bonk(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.bonk(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def flip(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.flip(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def blur(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.blur(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def ascii(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.ascii(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def paint(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
      
        url_pxl = str(user.avatar_url_as(static_format="png", size=1024))
        img_pxl = await dagpi.image_process(ImageFeatures.paint(), url_pxl)
        file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
        
        embed = discord.Embed(color=int(sv['server']['embedcolor'], 16))
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.set_footer(text='Peticion de: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"attachment://pixel.{img_pxl.format}")
        await ctx.reply(file=file_pxl, embed=embed, mention_author=False)

    @commands.command()
    async def shiped(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        except:

            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        try:
            r = requests.get('https://nekobot.xyz/api/imagegen?type=ship&user1={}&user2={}?size=1024'.format(user.avatar_url, ctx.author.avatar_url)).json()
        except:    
            embed = discord.Embed(
                color = discord.Color.red(),
                description = 'Peticion invalida!'
            )
            await ctx.send(embed=embed)     

        if user is None:
            await ctx.send('Necesitas mencionar a un usuario para usar este comando!')
        else:
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16)
            )
            embed.set_image(url=r['message'])
            embed.set_footer(text='{} + {}'.format(ctx.author.name, user.name))
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(img(bot))