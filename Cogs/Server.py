import discord
import json
import asyncio
from discord.ext import commands
from Utils.DefaultConfig import default_config

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resetconfig(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        
        await ctx.send('Estas seguro que quieres cambiar mi configuracion por predeterminado en este server?')

        def check(m):
            return ctx.author == m.author
            
        try:
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
            
            
            if (msg.content == 'si'):

                embed_edit = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = 'Configuracion predeterminada se aplico correctamente!'
                )

                embed = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = 'Aplicando la configuracion predeterminada, porfavor espere.'
                )
                message = await ctx.send(embed=embed)

                new = default_config
                
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                    json.dump(new, f, indent=4)

                await message.edit(embed=embed_edit)

            elif (msg.content == 'no'):
                
                await ctx.reply('Se cancelo el cambio de configuracion!')

            elif (msg.content == 'yes'):

                embed_edit = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = 'Configuracion predeterminada se aplico correctamente!'
                )

                embed = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = 'Aplicando la configuracion predeterminada, porfavor espere.'
                )
                message = await ctx.send(embed=embed)

                new = default_config
                
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                    json.dump(new, f, indent=4)

                await message.edit(embed=embed_edit)                

            else:
                await ctx.send('Opcion invalida!') 

        except TimeoutError:
            return
    
    @commands.command()
    async def changelanguage(self, ctx, *, lan=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
            
        lanlist = [
            'español',
            'ingles'
        ]     
        
        if lan == 'spanish':
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
            sv['server']['language'] = 'spanish'
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            await ctx.send('Lenguaje cambiado a: **Español**')
        if lan == 'english':
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
            sv['server']['language'] = 'english'
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            await ctx.send('Language changed to: **English**')

        if lan == 'español':
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
            sv['server']['language'] = 'spanish'
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            await ctx.send('Lenguaje cambiado a: **Español**')
        
        elif lan == 'ingles':
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
            sv['server']['language'] = 'english'
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)
            await ctx.send('Language changed to: **English**')



def setup(bot):
    bot.add_cog(Server(bot))