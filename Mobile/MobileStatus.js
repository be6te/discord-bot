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


client.login('OTUwODAzMzA0Mzk1NDcyOTU2.G8ji8w.Cv_rfnHFUt0mahEPQX_J9JisLqt_b9ZTIfUr5g')