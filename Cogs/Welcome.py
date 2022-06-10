from PIL import ImageDraw, Image, ImageFont, ImageChops
import discord
import json
from Utils.DefaultConfig import default_config
from discord.ext import commands
from main import *
from io import BytesIO
import numpy as np

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def circle(pfp,size = (215,215)): 
        pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
        bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(pfp.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, pfp.split()[-1])
        pfp.putalpha(mask)
        return pfp

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            with open(f'Database/ServerConfigs/{member.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{member.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{member.guild.id}.json') as f:
                sv = json.load(f)
        
        if sv['welcomer']['welcome'] == 'false':
            return
        elif sv['welcomer']['welcome'] == 'true':
            try:
                welcome_channel = await self.bot.fetch_channel(sv['welcomer']['channel_id'])
                welcome_message = str(sv['welcomer']['welcome_message'])
                welcome_title_message = str(sv['welcomer_embed']['embed_title'])
                embed_th = str(sv['welcomer_embed']['embed_thumbnail'])
            except:
                return
            
            if sv['welcomer']['welcome'] == 'false':
                return
            if sv['welcomer']['welcome'] == 'true':

                # Description syntax detect

                if '{user.mention}' in welcome_message:
                    welcome_message = welcome_message.replace('{user.mention}', member.mention)
                else:
                    welcome_message = welcome_message
                if '{user.name}' in welcome_message:
                    welcome_message = welcome_message.replace('{user.name}', member.name)
                else:
                    welcome_message = welcome_message

                if '{user}' in welcome_message:
                    welcome_message = welcome_message.replace('{user}', member)
                else:
                    welcome_message = welcome_message

                if '{server.name}' in welcome_message:
                    welcome_message = welcome_message.replace('{server.name}', member.guild.name)
                else:
                    welcome_message = welcome_message

                if '{member.mention}' in welcome_message:
                    welcome_message = welcome_message.replace('{member.mention}', member.mention)
                else:
                    welcome_message = welcome_message
                
                if '{member.name}' in welcome_message:
                    welcome_message = welcome_message.replace('{member.name}', member.name)
                else:
                    welcome_message = welcome_message
                
                if '{member}' in welcome_message:
                    welcome_message = welcome_message.replace('{member}', member)
                else:
                    welcome_message = welcome_message
                
                # Title syntax detect

                if '{none}' in welcome_title_message:
                    welcome_title_message = welcome_title_message.replace('{none}', '')
                else:
                    welcome_title_message = welcome_title_message
                if '{server.name}' in welcome_title_message:
                    welcome_title_message = welcome_title_message.replace('{server.name}', member.guild.name)
                else:
                    welcome_title_message = welcome_title_message
                if '{user.name}' in welcome_title_message:
                    welcome_title_message = welcome_title_message.replace('{user.name}', member.name)
                else:
                    welcome_title_message = welcome_title_message
                if '{user}' in welcome_title_message:
                    welcome_title_message = welcome_title_message.replace('{user}', str(member))
                else:
                    welcome_title_message = welcome_title_message
                
                # Thumbnail syntax detect

                if '{user.avatar}' in embed_th:
                    embed_th = embed_th.replace('{user.avatar}', str(member.avatar_url))
                else:
                    embed_th = embed_th
                if '{none}' in embed_th:
                    embed_th = '' 
                else:
                    embed_th = embed_th

                embed = discord.Embed(
                    title = welcome_title_message,
                    color = int(sv['server']['embedcolor'],16),
                    description = f'{welcome_message}'
                )
                embed.set_thumbnail(url=embed_th)
                await welcome_channel.send(embed=embed)

    @commands.command()
    async def welcomesetup(self, ctx):        
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        def check(m):
            return ctx.author == m.author

        if sv['welcomer']['welcome'] == "false":
            sv['welcomer']['welcome'] = "true"

        try:
            setup = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'Hola!, es hora de configurar los mensajes de bienvenida!\n\nMenciona un canal donde dare las bienvenidas de la siguente forma: {ctx.channel.mention}'
            )
            await ctx.send(embed=setup)

            c_id = await self.bot.wait_for('message', timeout=60.0, check=check)
            get_c_id = int(c_id.content[2:-1])
            
            start = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'Los mensajes de bienvenidas que tipo va a ser? [embed/text]' 
            )
            await ctx.send(embed=start)

            msg = await self.bot.wait_for('message', timeout=60.0, check=check)

            if msg.content == 'embed':
                if sv['welcomer_embed']['embed'] == 'false':
                    sv['welcomer_embed']['embed'] = 'true'

                try:
                    embedd = discord.Embed(
                        color = int(sv['server']['embedcolor'], 16),
                        description = 'Necesitas un mensaje para los nuevos usuarios, envia un mensaje cual usare para los mensajes de bienvenida!\n\n`{member.mention}` > Menciona al usuario en el mensaje embed\n`{member.name}` > Muestra el nombre del usuario en el mensaje embed\n`{server.name}` > Utiliza el nombre del servidor'
                    )
                    await ctx.send(embed=embedd)
                    cf_message = await self.bot.wait_for('message', timeout=60.0, check=check)
                    if cf_message.content == None:
                        cf_message.content = 'Hola! {user.mention} bienvenido a {server.name}'
                except:
                    return await ctx.send('Timeout -- Ya no puedes hacer esta **configuracion** si deseas configurar usa **{}welcome**'.format(sv['server']['prefix']))

                title_embed = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = 'El mensaje embed necesita un titulo.\n\n`{none}` > Sin titulo\n`{user.name}` > Utiliza el nombre del usuario que entro a tu server como titulo\n`{server.name}` > Usa el nombre del servidor como titulo.\n`{envia un mensaje para un titulo custom}` > Usa el titulo que tu quieras.'
                )
                title_embed.set_image(url='https://www.beete.xyz/examples/titleexample.png')
                await ctx.send(embed=title_embed)

                try:
                    cf_embed_title = await self.bot.wait_for('message', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return await ctx.send('Timeout -- Ya no puedes hacer esta **configuracion** si deseas configurar usa **{}welcome**'.format(sv['server']['prefix']))
                try:
                    th_embed = discord.Embed(
                        title = 'Thumbnail',
                        color = int(sv['server']['embedcolor'], 16),
                        description = 'Un thumbnail de bienvenida!\n\n`{user.avatar}` > Usa el avatar de la persona que se unio al servidor\n`<url>` > Envie una **url** para utilizarla\n\nAsi se veria tu mensaje de bienvenida, ejemplo:' 
                    )
                    th_embed.set_image(url='https://www.beete.xyz/examples/thexample.png')
                    await ctx.send(embed=th_embed)

                    cf_embed_th = await self.bot.wait_for('message', timeout=10.0, check=check)
                    if cf_embed_th.content == '{user.avatar}':
                        cf_embed_th.content = '{user.avatar}'

                    print('Embed title ' + cf_embed_title.content)
                    print('Thumbnail ' + cf_embed_th.content)

                    em_title = cf_embed_title.content
                    em_thum = cf_embed_th.content
                    em_message = cf_message.content

                    servername = ctx.guild.name
                    serverid = ctx.guild.id

                    sv['welcomer']['channel_id'] = int(get_c_id)
                    sv['welcomer']['server_id'] = int(ctx.guild.id)
                    sv['welcomer']['server_name'] = str(ctx.guild.name)
                    sv['welcomer']['welcome_message'] = str(em_message)
                    sv['welcomer_embed']['embed'] = 'true'
                    sv['welcomer_embed']['embed_title'] = str(em_title)
                    sv['welcomer_embed']['embed_thumbnail'] = str(em_thum)

                    fin = discord.Embed(
                        color = int(sv['server']['embedcolor'], 16),
                        description = f'Finalizando la configuracion.'
                    )
                    fined = await ctx.send(embed=fin)

                    done = discord.Embed(
                        color = int(sv['server']['embedcolor'], 16),
                        description = f'Configuracion terminada, y guardada exitosamente!'
                    )
                    await fined.edit(embed=done)

                    saved_json = {
                        "welcomer": {
                            "welcome": "true",
                            "channel_id": get_c_id,
                            "server_id": serverid,
                            "server_name": servername,
                            "welcome_message": em_message
                        },
                        "welcomer_embed": {
                            "embed": "true",
                            "embed_title": em_title,
                            "embed_thumbnaild": em_thum
                        }
                    }
                
                    await ctx.send('Configuracion en formato **JSON**')
                    await ctx.send('```{}```'.format(saved_json))

                    with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                        json.dump(sv, f, indent=4)

                except asyncio.TimeoutError:
                    return await ctx.send('Timeout -- Ya no puedes hacer esta **configuracion** si deseas configurar usa **{}welcome**'.format(sv['server']['prefix']))
            elif msg.content == 'text':
                try:
                    textmsg = await self.bot.wait_for('message', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return await ctx.send('Timeout, Ya no puedes hacer esta **configuracion** si deseas configurar usa **{}welcome**'.format(sv['server']['prefix']))
            else:
                return await ctx.send('Opcion invalida, intentelo denuevo usando el mismo comando **{}welcome**'.format(sv['server']['prefix']))
        except asyncio.TimeoutError:
            return await ctx.send('Timeout -- Ya no puedes hacer esta **configuracion** si deseas configurar usa **{}welcome**'.format(sv['server']['prefix']))

    @commands.command()
    async def wl(self, ctx):

        member = ctx.author

        filename = 'ola.png'
        
        background = Image.open('Welcome.png')
        
        asset = ctx.author.avatar_url_as(size=1024) # This loads the Member Avatar
        data = BytesIO(await asset.read())
        
        pfp = Image.open(data).convert("RGBA")
        pfp = self.circle(pfp)
        pfp = pfp.resize((265,265)) # Resizes the Profilepicture so it fits perfectly in the circle
        
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("candy.otf",42) # <- Text Font of the Member Count. Change the text size for your preference
        member_text = ("#" + str(ctx.guild.member_count) + " USER") # <- Text under the Profilepicture with the Membercount
        draw.text((383,410),member_text,font=font)
        
        background.paste(pfp, (379,123), pfp) # Pastes the Profilepicture on the Background Image
        background.save(filename) # Saves the finished Image in the folder with the filename
        
        msg = await ctx.send(file = discord.File(filename),content ="WELCOME " + ctx.author.mention + "! Please read the rules! :heart:")

    @commands.command()
    async def examples(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        e = discord.Embed(
            title = 'Example!',
            color = int(sv['server']['embedcolor'], 16),
            description = f'Hola! **beete#1337**, bienvenido a **Server Test!**\nRecuerda leer las reglas para no tener problemas en el servidor!\n\n-> Rules: <#972913574383063071>\n-> Chat: <#972913596348633098>\n-> Commands: <#972913619039846431>'
        )
        e.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command()
    async def welcomer(self, ctx, arg):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if arg == 'true':
            if sv['welcomer']['channel_id'] == 0:
                return await ctx.send('Necesitas configurar esta opcion antes de habilitarla.')
            if sv['welcomer']['welcome'] == 'true':
                return await ctx.send('No puedes habilitar esta opcion porque ya esta habilitada.')
            else:
                sv['welcomer']['welcome'] = 'true'
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                    json.dump(sv, f, indent=4)
                await ctx.send('Los mensajes de bienvenida fueron habilitados!')
        elif arg == 'false':
            if sv['welcomer']['welcome'] == 'false':
                return await ctx.send('No puedes desabilitar una opcion que ya esta desabilitada.')
            else:
                sv['welcomer']['welcome'] = 'false'
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                    json.dump(sv, f, indent=4)
                await ctx.send(f'Opcion desabilitada, puedes habilitarla denuevo con **{sv["server"]["prefix"]}welcomer true**')
        else:
            return await ctx.send('Opcion invalida opciones validas: **true/false**')   

    @commands.command()
    async def genimg(self, ctx, *, text = 'XDD'):

        image = Image.open('white.png')

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('comicsans.ttf', 24)

        draw.text((0,150), text, (0,0,0), font=font)
        image.save('gay.png')
        
        await ctx.send(file=discord.File("gay.png"))
        os.remove('gay.png')

def setup(bot):
    bot.add_cog(Welcome(bot))