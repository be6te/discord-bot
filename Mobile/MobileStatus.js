const { Client , Intents } = require('discord.js')

const client = new Client(
	{
		intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
		ws: { properties: { $browser: "Discord iOS" }}
	}
	);

client.once('ready', () => {
	console.log('Ready!');
});


client.login('your bot token')
