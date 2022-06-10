import discord
from discord.ext import commands
import datetime
import json
from Utils.DefaultConfig import default_config
import re

invitere = r"(?:https?:\/\/)?discord(?:\.gg|app\.com\/invite)?\/(?:#\/)([a-zA-Z0-9-]*)"
invitere2 = r"(http[s]?:\/\/)*discord((app\.com\/invite)|(\.gg))\/(invite\/)?(#\/)?([A-Za-z0-9\-]+)(\/)?"


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipes = {}

        @bot.listen('on_message_delete')
        async def on_message_delete(msg):
            if msg.author.bot:
                return
            self.snipes[msg.channel.id] = msg

    def sanitise(self, string):
        if len(string) > 1024:
            string = string[0:1021] + "..."
        string = re.sub(invitere2, '[INVITE REDACTED]', string)
        return string

    @commands.command()
    async def snipe(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        try:
            snipe = self.snipes[ctx.channel.id]
        except KeyError:
            return
        if snipe is None:
            return
        emb = discord.Embed()
        emb.set_author(name=str(snipe.author), icon_url=snipe.author.avatar_url)
        emb.description = self.sanitise(snipe.content)
        emb.colour = int(sv['server']['embedcolor'], 16)
        emb.set_footer(text=f'Mensaje captado por: {ctx.author.name}', icon_url=ctx.author.avatar_url)
        emb.timestamp = snipe.created_at
        await ctx.send(embed=emb)
        self.snipes[ctx.channel.id] = None


def setup(bot):
    bot.add_cog(Snipe(bot))