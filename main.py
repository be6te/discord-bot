import discord
from discord import Embed
import os
import json
from Utils.AnimPresence import *
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from Utils.DefaultConfig import default_config
from discord.ext import commands

i = 'https://discord.com/api/oauth2/authorize?client_id=950803304395472956&permissions=1539208314102&scope=bot'

with open('Settings.json') as f:
    config = json.load(f)

def get_prefix(bot, message):
    try:
        with open(f'Database/ServerConfigs/{message.guild.id}.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes['server']['prefix']
    except:
        with open(f'Database/ServerConfigs/{message.guild.id}.json', 'w') as f:
            json.dump(default_config, f, indent=4)
        with open(f'Database/ServerConfigs/{message.guild.id}.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes['server']['prefix']

invite = 'https://discord.com/api/oauth2/authorize?client_id=950803304395472956&permissions=1532732303607&scope=bot'

bot = commands.Bot(
    command_prefix = (get_prefix),
    intents = discord.Intents(
        messages=True,
        guilds=True,
        members=True
    )
)
DiscordComponents(bot)

@bot.event
async def on_connect():
    print('Done!')

@bot.command()
async def helpy(ctx):
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
        description = 'Hola! **{}** 👋, gracias por pedir mi lista de comandos!\n\n\t`47 comandos` y `6 categorias`\n\n**- Moderacion**\n**- Roleplay**\n**- Imagenes**\n**- Utilidades**\n**- Bienvenidas**\n**- Busquedas**'.format(ctx.author.name)
    )
    global send
    send = await ctx.send(
        embed = embed,
        components = [
            Select(
                placeholder = 'Categorias',
                options = [
                    SelectOption(label="Moderacion", value="Opcion1"),
                    SelectOption(label="Roleplay", value="Opcion2"),
                    SelectOption(label="Imagenes", value="Opcion3"),
                    SelectOption(label="Utilidades", value = "Opcion4"),
                    SelectOption(label="Bievenidas", value="Opcion5"),
                    SelectOption(label="Busquedas", value="Opcion6")
                ])])


@bot.event
async def on_select_option(interaction):
    try:
        with open(f'Database/ServerConfigs/{interaction.guild.id}.json') as f:
            sv = json.load(f) 
    except:
        with open(f'Database/ServerConfigs/{interaction.guild.id}.json', 'w') as f:
            json.dump(default_config, f, indent=4)
        with open(f'Database/ServerConfigs/{interaction.guild.id}.json') as f:
            sv = json.load(f)

    prefix = sv['server']['prefix']

    mod = discord.Embed(
        color = int(sv['server']['embedcolor'], 16),
        description = f'```ini\n[Moderacion]\n\n{prefix}ban <@Member> <Razon>\n{prefix}kick <@Member> <Razon>\n{prefix}purge <Monto>\n{prefix}addrank <@Member> <@Role>\n{prefix}removerank <@Member> <@Role>\n{prefix}slowmode <Segundos>\n\n[Si necesitas ayuda con un comando usa {prefix}help <Comando>]```'
    )
    mod.set_footer(text='Categoria: Moderacion', icon_url=bot.user.avatar_url)
    mod.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)

    role = discord.Embed(
        color = int(sv['server']['embedcolor'], 16),
        description = f'```ini\n[Roleplay]\n\n{prefix}kiss <@Member>\n{prefix}hug <@Member>\n{prefix}slap <@Member>\n{prefix}shoot <@Member>\n{prefix}kill <@Member>\n{prefix}pat <@Member>\n\n[Reacciones]\n\n{prefix}dance\n{prefix}smile\n{prefix}cry\n{prefix}happy\n{prefix}peek\n{prefix}blush\n{prefix}jpos\n\n[Si necesitas ayuda con un comando usa {prefix}help <Comando>]```'
    )
    role.set_footer(text='Categoria: Roleplay', icon_url=bot.user.avatar_url)
    role.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)

    util = discord.Embed(
        color = int(sv['server']['embedcolor'], 16),
        description = f'```ini\n[Utilidades]\n\n{prefix}avatar <@Member>\n{prefix}poll <Message>\n{prefix}userinfo <@Member>\n{prefix}snipe\n{prefix}mcp <Minecraft Nick>\n{prefix}hypixel <Minecraft Nick<\n{prefix}bedwards <Minecraft Nick>\n{prefix}translate <Lenguage> <Mensaje>\n\n[Si necesitas ayuda con un comando usa {prefix}help <Comando>]```'
    )
    util.set_footer(text='Categoria: Utilidades', icon_url=bot.user.avatar_url)
    util.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)

    img = discord.Embed(
        color = int(sv['server']['embedcolor'], 16),
        description = f'```ini\n[Roleplay]\n\n{prefix}ascii <@Member>\n{prefix}blur <@Member>\n{prefix}bonk <@Member>\n{prefix}flip <@Member>\n{prefix}paint <@Member>\n{prefix}pixel <@Member>\n{prefix}shipped <@Member>\n\n[Si necesitas ayuda con un comando usa {prefix}help <Comando>]```'
    )
    img.set_footer(text='Categoria: Utilidades', icon_url=bot.user.avatar_url)
    img.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)


    await interaction.respond(type=6)
    if interaction.values[0] == "Opcion1":
        await send.edit(embed=mod)
    elif interaction.values[0] == "Opcion2":
        await send.edit(embed=role)
    elif interaction.values[0] == "Opcion3":
        await send.edit(embed=img)
    elif interaction.values[0] == "Opcion4":
        await send.edit(embed=util)
    
    # TicketMaganer.py | Events

bot.loop.create_task(status(bot=bot))

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

if __name__ == '__main__':
    token = config.get('token')
    bot.run(token) 