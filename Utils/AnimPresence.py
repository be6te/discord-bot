import discord
import asyncio
from time import sleep, strftime, time, gmtime

start_time = 0

def now_time():
	while True:
		return strftime("%H:%M:%S", gmtime(time() - start_time))

async def status(bot):

	await bot.wait_until_ready()

	while not bot.is_closed():

		await bot.change_presence(activity=discord.Game(name=f"n!help"))

		await asyncio.sleep(10)

		await bot.change_presence(activity=discord.Game(name=f"n!help - beete.xyz/btw"))

		await asyncio.sleep(10)

		await bot.change_presence(activity=discord.Game(name=f"n!help - beete.xyz/btw/vote"))