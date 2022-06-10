import discord
import requests
import json
from Utils.DefaultConfig import default_config
from discord.ext import commands

class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gtprofile', 'gprofile'])
    async def githubprofile(self, ctx, user):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        r = requests.get('https://api.github.com/users/{}'.format(user)).json()

        name = r['login']
        id = r['id']
        avatar = r['avatar_url']
        link_profile = r['html_url']
        type = r['type']
        admin = r['site_admin']
        acc_name = r['name']
        site = r['blog']
        location = r['location']
        twitter = r['twitter_username']
        public_re = r['public_repos']
        followers = r['followers']
        following = r['following']
        bio = r['bio']

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16)
        )
        embed.add_field(name='Username', value=name, inline=True)
        embed.add_field(name='Nombre', value=acc_name, inline=True)
        embed.add_field(name='ID', value=id, inline=True)
        embed.add_field(name='Perfil', value=link_profile, inline=True)
        embed.add_field(name='Tipo de cuenta', value=type, inline=True)
        embed.add_field(name='Admin', value=admin, inline=True)
        embed.add_field(name='Sitio web', value=site, inline=True)
        embed.add_field(name='Localidad', value=location, inline=True)
        embed.add_field(name='Twitter', value=twitter, inline=True)
        embed.add_field(name='Repositorios publicos', value=public_re, inline=True)
        embed.add_field(name='Followers', value=followers, inline=True)
        embed.add_field(name='Following', value=following, inline=True)

        embed.set_thumbnail(url=avatar)
        embed.set_author(name='Github.com', icon_url='https://cdn-icons-png.flaticon.com/512/25/25231.png')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Github(bot))