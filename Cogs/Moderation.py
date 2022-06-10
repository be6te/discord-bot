import discord
import requests
import datetime
from io import BytesIO
import json
from Utils.DefaultConfig import default_config
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def embed_perms(message):
        try:
            check = message.author.permissions_in(message.channel).embed_links
        except:
            check = True
        return check
    
    def get_user(message, user):
        try:
            member = message.mentions[0]
        except:
            member = message.guild.get_member_named(user)
        if not member:
            try:
                member = message.guild.get_member(int(user))
            except ValueError:
                pass
        if not member:
            return None
        return member
        
    def embed_perms(message):
        try:
            check = message.author.permissions_in(message.channel).embed_links
        except:
            check = True
        return check
        
    def find_channel(channel_list, text):
        if text.isdigit():
            found_channel = discord.utils.get(channel_list, id=int(text))
        elif text.startswith("<#") and text.endswith(">"):
            found_channel = discord.utils.get(
                channel_list,
                id=text.replace("<", "").replace(">", "").replace("#", ""))
        else:
            found_channel = discord.utils.get(channel_list, name=text)
        return found_channel

    @commands.command()
    async def ban(self, ctx, user: discord.Member=None, *, reason=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open('Languages/Translate-Moderation-Spanish.json') as f:
                lan = json.load(f)
            
            user_banned = lan['banned']['ban']
            banned_by = lan['banned']['bannedby']
            rason = lan['banned']['reason']
            banneds = lan['banned']['baneos']
            none_reason = lan['all']['nonereason']

            autoban = lan['user']['autoban']
            ban_bot = lan['user']['banbot']
            dbbans = lan['banned']['dbbans']

        elif sv['server']['language'] == 'english':
            with open('Languages/Translate-Moderation-English.json') as f:
                en = json.load(f)

            user_banned = en['banned']['ban']
            banned_by = en['banned']['bannedby']
            rason = en['banned']['reason']
            banneds = en['banned']['baneos']
            none_reason = en['all']['nonereason']

            autoban = en['user']['autoban']
            ban_bot = en['user']['banbot']

            dbbans = en['banned']['dbbans']

        if user == ctx.author:
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{autoban} :x:'
            )
            await ctx.reply(embed=embed)
        elif user == self.bot:
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{ban_bot} :x:'
            )
            await ctx.reply(embed=embed)
        elif user is None:
            await ctx.send('{} Necesitas mencionar a un usuario/bot para expulsar'.format(ctx.author.mention))
        else:
            await user.ban(reason=reason)
            bans = await ctx.guild.bans()

            today = datetime.datetime.now()
            date_time = today.strftime("%d/%m/%Y")

            if reason is None:
                reason = none_reason
                
            ban_reasons = int(sv['moderation']['ban'])
            ban_reasons += 1
            sv['moderation']['ban'] = ban_reasons
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)

            db = str(sv['moderation']['ban'])

            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                timestamp=ctx.message.created_at
            )
            embed.add_field(name=user_banned, value=user, inline=True)
            embed.add_field(name=banned_by, value=ctx.author, inline=True)
            embed.add_field(name=rason, value=reason, inline=True)
            embed.add_field(name=banneds, value='`{} | {}`'.format(db, dbbans).format(db), inline=True)
            embed.set_footer(text=f'Server: {ctx.guild.name} | {banneds} #{db}', icon_url=ctx.guild.icon_url)
            embed.set_author(name=user, icon_url=user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def kick(self, ctx, user: discord.Member=None, *, reason=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if sv['server']['language'] == 'spanish':
            with open('Languages/Translate-Moderation-Spanish.json') as f:
                lan = json.load(f)
            
            user_kicked = lan['kick']['kick']
            kicked_by = lan['kick']['kickedby']
            kickrason = lan['kick']['kickreason']
            kickeds = lan['kick']['kicks']
            none_reason = lan['all']['nonereason']

            autokick = lan['kickuser']['autokick']
            bot_kick = lan['kickuser']['botkick']

            dbks = lan['kick']['dbkicks']

        elif sv['server']['language'] == 'english':
            with open('Languages/Translate-Moderation-English.json') as f:
                en = json.load(f)

            user_kicked = en['kick']['kick']
            kicked_by = en['kick']['kickedby']
            kickrason = en['kick']['kickreason']
            kickeds = en['kick']['kicks']
            none_reason = en['all']['nonereason']

            autokick = en['kickuser']['autokick']
            bot_kick = en['kickuser']['botkick']

            dbks = en['kick']['dbkicks']


        if user == ctx.author:
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{autokick} :x:'
            )
            await ctx.reply(embed=embed)
        elif user == self.bot:
            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = f'{bot_kick} :x:'
            )
            await ctx.reply(embed=embed)
        elif user is None:
            await ctx.send('{} Necesitas mencionar a un usuario/bot para expulsar'.format(ctx.author.mention))
        else:
            await user.kick(reason=reason)
            today = datetime.datetime.now()
            date_time = today.strftime("%d/%m/%Y")

            if reason is None:
                reason = none_reason
                
            kick_reasons = int(sv['moderation']['kick'])
            kick_reasons += 1
            sv['moderation']['kick'] = kick_reasons
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)

            db = str(sv['moderation']['kick'])

            embed = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                timestamp=ctx.message.created_at
            )
            embed.add_field(name=user_kicked, value=user, inline=True)
            embed.add_field(name=kicked_by, value=ctx.author, inline=True)
            embed.add_field(name=kickrason, value=reason, inline=True)
            embed.add_field(name=kickeds, value='`{} | {}`'.format(db, dbks), inline=True)
            embed.set_author(name=user, icon_url=user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['nuke'])
    @commands.bot_has_permissions(manage_channels=True)
    async def purge(self, ctx, amount:int):
        today = datetime.datetime.now()
        date_time = today.strftime("%d/%m/%Y")

        if (amount > 1200):
            return await ctx.reply('No puedes borrar mas de 1200 mensajes al mismo tiempo!')
        elif (amount < 0):
            return await ctx.reply('No puedes borrar menos de 0 mensajes!')
        else:
            try:
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                    sv = json.load(f)
            except:
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                    json.dump(default_config, f, indent=4)
                with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                    sv = json.load(f)
                try:
                    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
                    print(invitelink)
                except:
                    print('None!')

            await ctx.channel.purge(limit=amount)

            embed = discord.Embed(color = int(sv['server']['embedcolor'], 16))
            embed.add_field(name='Cantidad de mensajes borrados:', value=str(amount), inline=True)
            embed.add_field(name='Mensajes borrados por:', value=ctx.author, inline=True)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def addrank(self, ctx, user: discord.Member=None, rank: discord.Role=None):

        today = datetime.datetime.now()
        date_time = today.strftime("%d/%m/%Y")

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
            invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
            print(invitelink)
        except:
            print('None!')
        
        if (rank is None):
            await ctx.reply('Necesitas mencionar al role que quieres otorgar.')
        else:    
            try:
                await user.add_roles(rank)
            except:
                embed = discord.Embed(color=int(sv['server']['embedcolor'], 16), description = f'No puedo añadir este role a este usuario!')
                embed.set_footer(text='El error puede ser causado ya que usted no tiene permisos suficientes, o el role que esta intentando dar es superior al mio [Coloque mi role arriba del que quiere otorgar]')
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(
                    color = int(sv.get('embedcolor'),16)
                    )
                embed.add_field(name='Usuario:', value=user.mention, inline=True)
                embed.add_field(name='Rol añadido:', value=rank.mention, inline=True)
                embed.add_field(name='Rol añadido por:', value=ctx.author.mention, inline=True)
                embed.add_field(name='Timestamp:', value=date_time, inline=True)
                
                embed.set_author(name=user, icon_url=user.avatar_url)
                embed.set_footer(text='Rol añadido por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(aliases=['unrank'])
    async def removerank(self, ctx, user: discord.Member=None, rank: discord.Role=None):

        today = datetime.datetime.now()
        date_time = today.strftime("%d/%m/%Y")

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
                
        if (rank is None):
            await ctx.reply('Necesitas mencionar al role que quieres quitar.')
        else:    
            try:
                await user.remove_roles(rank)
            except:
                embed = discord.Embed(color=int(sv['server']['embedcolor'], 16), description = f'No puedo quitar este role a este usuario!')
                embed.set_footer(text='El error puede ser causado ya que usted no tiene permisos suficientes, o el role que esta intentando quitar es superior al mio [Coloque mi role arriba del que quiere quitar]')
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(
                    color = int(sv.get('embedcolor'),16)
                    )
                embed.add_field(name='Usuario:', value=user.mention, inline=True)
                embed.add_field(name='Rol quitado:', value=rank.mention, inline=True)
                embed.add_field(name='Rol quitado por:', value=ctx.author.mention, inline=True)
                embed.add_field(name='Timestamp:', value=date_time, inline=True)
                
                embed.set_author(name=user, icon_url=user.avatar_url)
                embed.set_footer(text='Rol quitado por: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                # await user.add_roles(role)
            
    @commands.command()
    async def slowmode(self, ctx, time: int=None, *, status=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if (time is None):
            time = 5
        elif (time < 0):
            return await ctx.send('El tiempo no puede ser menor a 0 segundos')
        elif (time > 21600):
            return await ctx.send('El tiempo no puede ser mayor a 6 horas')
        else:
            if time == 0:
                await ctx.channel.edit(slowmode_delay=time)
                await ctx.send('Slowmode desactivado.')
            else:
                await ctx.channel.edit(slowmode_delay=time)
                
                embed = discord.Embed(
                    color = int(sv['server']['embedcolor'], 16),
                    description = f'Slowmode activado.'
                )
                embed.set_footer(text='Slowmode de {} segundos'.format(time))
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
    
    @commands.group(invoke_without_command=True, aliases=['user', 'uinfo', 'info', 'ui'])
    async def userinfo(self, ctx, *, name=""):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        if ctx.invoked_subcommand is None:
            if name:
                try:
                    user = ctx.message.mentions[0]
                except IndexError:
                    user = ctx.guild.get_member_named(name)
                if not user:
                    user = ctx.guild.get_member(int(name))
                if not user:
                    user = self.bot.get_user(int(name))
                if not user:
                    await ctx.send('No pude encontrar este usuario.')
                    return
            else:
                user = ctx.message.author

            if isinstance(user, discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"
                voice_state = None if not user.voice else user.voice.channel
            
            em = discord.Embed(
                timestamp=ctx.message.created_at,
                colour=int(sv['server']['embedcolor'], 16),
                description = f'```diff\n+ Usuario: {user}\n+ ID: {user.id}```'
            )
            if isinstance(user, discord.Member):
                em.add_field(name='En canal de voz', value=voice_state, inline=True)
                em.add_field(name='Actividad', value=user.activity, inline=True)
                em.add_field(name='Role mas alto', value=role, inline=True)
                em.add_field(name='Cuenta creada', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                if isinstance(user, discord.Member):
                    em.add_field(name='Se unio', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_thumbnail(url=user.avatar_url)
                em.set_author(name=user, icon_url=user.avatar_url)
                await ctx.send(embed=em)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Moderation(bot))