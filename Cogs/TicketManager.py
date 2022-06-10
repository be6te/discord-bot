import discord
import os
import json
import datetime
import asyncio
from Utils.DefaultConfig import default_config
from discord_components import DiscordComponents, ComponentsBot, Button, ButtonStyle, InteractionEventType

from discord.ext import commands

class Tickets():
    def __init__(self, ticket):

        for t in ticket:
            t = []
        else:
            t = None
        
        if ticket is None:
            ticket = {t}
            t = [ticket]
            
    
class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendticket(self, ctx):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)

        try:
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json') as f:
                ticket = json.load(f) 
        except:
            ticket_settings_default = {
                "ticket_guild_id": ctx.guild.id,
                "ticket_channel": "None",
                "ticket_open_message": "Hola, el numero de tu ticket es **ticket-#{}**, solo espera que un staff te ayude!"
            }
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json', 'w') as f:
                json.dump(ticket_settings_default, f, indent=4)
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json') as f:
                ticket = json.load(f)

        if ticket.get('ticket_channel') == "None":
            channel_get = ctx
        else:
            channel_get = self.bot.get_channel(int(ticket.get('ticket_channel')))

        embed = discord.Embed(
            color = int(sv['server']['embedcolor'], 16),
            description = f'Presiona el boton 📩 para abrir un ticket!'
        )
        await channel_get.send(
            embed=embed,
            
            components = [
                Button(label = "Ticket 📩", custom_id = "ticketopen")
            ]
        )

        while True:
            interaction = await self.bot.wait_for("button_click", check = lambda i: i.custom_id == "ticketopen")

            t_open = int(sv['moderation']['tickets'])
            t_open += 1
            sv['moderation']['tickets'] = t_open
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)

            db = str(sv['moderation']['tickets'])
            
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(sv, f, indent=4)

            open_message = discord.Embed(
                color = int(sv['server']['embedcolor'], 16),
                description = 'Hola, el numero de tu ticket es **ticket-#{}**, solo espera que un staff te ayude!'.format(db),
                timestamp = datetime.datetime.utcnow()
            )

            guild = ctx.guild
            
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, view_channel=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
                self.bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True)
            }
            try:
                ticket = await ctx.guild.create_text_channel("Ticket #{}".format(db), overwrites=overwrites)
                await interaction.send(content = "<#{}>".format(ticket.id))
            except:
                pass

            await ticket.send(interaction.user.mention)
            await ticket.send(
                embed=open_message,
                components = [
                    Button(label = "Cerrar ❌", custom_id = "Close")
            ])
            try:
                closeticket = await self.bot.wait_for("button_click", check = lambda i: i.custom_id == "Close")
                await ticket.delete()
            except:
                pass

    @commands.command()
    async def ticketsetup(self, ctx, channel: discord.TextChannel, *, message=None):
        try:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f) 
        except:
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            with open(f'Database/ServerConfigs/{ctx.guild.id}.json') as f:
                sv = json.load(f)
        # ------------------------------------------------------------------ #
        try:
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json') as f:
                ticket = json.load(f) 
        except:
            ticket_settings_default = {
                "ticket_guild_id": ctx.guild.id,
                "ticket_channel": "None",
                "ticket_open_message": "Hola, el numero de tu ticket es **ticket-#{}**, solo espera que un staff te ayude!"
            }
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json', 'w') as f:
                json.dump(ticket_settings_default, f, indent=4)
            with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json') as f:
                ticket = json.load(f)

        if message is None:
            message = 'Hola, el numero de tu ticket es **ticket-#{}**, solo espera que un staff te ayude!'.format(sv.get('ticket-open'))

        ticket_settings = {
            "ticket_guild_id": ctx.guild.id,
            "ticket_channel": channel.id,
            "ticket_open_message": message
        }
        with open(f'Database/ServerConfigs/Ticket-{ctx.guild.id}.json', 'w') as f:
            json.dump(ticket_settings, f, indent=4)


def setup(bot):
    bot.add_cog(Ticket(bot))