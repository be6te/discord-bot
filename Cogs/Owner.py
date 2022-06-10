import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def servers(self, ctx):
        activeservers = self.bot.guilds

        loop = [f"{u}" for u in activeservers]
        list = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])
        print('\n{}'.format(list))

def setup(bot):
    bot.add_cog(Owner(bot))