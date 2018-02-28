# NOTE : Eval, Reboot are broken due to being heavily faulty.

import discord
import random
import asyncio
import json
import os
import aiohttp
#-------Clients-------DBL

client = discord.Client()
dbltoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQxNjE2MzQ4NDQxNDI0NjkxMiIsImJvdCI6dHJ1ZSwiaWF0IjoxNTE5NDU4NTgyfQ.UyOUgdPgOiZ3nHWQ1YZW-8DjcaTBoHX3_B0IozG1Shg"
players = {}
token = "NDE2MTYzNDg0NDE0MjQ2OTEy.DXL0xQ.YydSk1LFx6X0WBOKP6aQ2LIdkfk"
url = "https://discordbots.org/api/bots/416163484414246912" + "/stats"
headers = {"Authorization" : dbltoken}
reee = "Kermit holds a gun again!"

@client.event
async def on_ready():
    payload = {"server_count" : len(client.servers)}
    async with aiohttp.ClientSession as aioclient:
        await aioclient.post(url, data=payload, headers=headers)

@client.event
async def on_server_join(server):
    payload = {"server_count" : len(client.servers)}
    async with aiohttp.ClientSession as aioclient:
        await aioclient.post(url, data=payload, headers=headers)
        
@client.event
async def on_server_remove(server):
    payload = {"server_count"  : len(client.servers)}
    async with aiohttp.ClientSession as aioclient:
        await aioclient.post(url, data=payload, headers=headers)
        
@client.event
async def on_ready():
     print("static")
     await client.change_presence(game=discord.Game(name="Type }>help"))
     
#----Clients Command----

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith("}>coinflip"):
		choice = random.randint(1,2)
		if choice == 1:
			await client.send_message(message.channel, "Heads!")
		if choice == 2:
			await client.send_message(message.channel, "Tails!")
	elif message.content.startswith("}>8ball"):
		await client.send_message(message.channel, random.choice(["Yes, I agree, (or whatever)",
	                                                                                                                    "So confused, what are you trying to say?",
	                                                                                              			          "No, my mind is telling me that I disagree."]))
	elif message.content.startswith("}>help"):
		embed=discord.Embed(title="Command List", color=0x00ff00)
		embed.add_field(name="}>8ball", value="Answers inaccurately.")
		embed.add_field(name="}>ping", value="Pong!")
		embed.add_field(name="}>help", value="Shows a help list of commands.")
		embed.add_field(name="}>bonzi", value="random")
		embed.add_field(name="}>coinflip", value="Flips a emoji, not a coin.")
		embed.add_field(name="}>botinfo", value="Shows a info of the bot.")
		embed.add_field(name="BOT DEVELOPER ONLY", value="`}>shutdown`, `}>debug`, `}>reboot`, `}>print`, `}>version`, `}>beta`")
		embed.add_field(name="}>cleverbotinfo", value="Shows the CleverBot info.")
		embed.add_field(name="}>invite", value="Invite the bot!")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("./cmdhelp 8ball"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "8ball - A fun command whenever you qgot the chance to demand the bot to answer your question! Although fun, being answered can be extremely inaccurate.")
	elif message.content.startswith("./cmdhelp ping"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./ping - A extremely inspired piece of art from other bots.")
	elif message.content.startswith("./cmdhelp coinflip"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./coinflip - Actually picks a emoji, not flip a coin, so a fun command.")
	elif message.content.startswith("./cmdhelp help"):
		await client.add_reaction(message, "✅")
		await client.send_message(message.channel, "./help - Direct messages you a help list, its actually notable for a very few mistakes observed.")
	elif message.content.startswith("./ende ende"):
		await client.send_message(message.channel, "ende ende")
	elif message.content.startswith("}>print"):
		message.author.id == "383561620661731329"
		if not message.author.id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
			variable = message.content[len("}>print"):].strip()
			await client.send_message(message.channel, variable)
			print("Log : Used }>print")
	elif message.content.startswith("}>bonzi"):
		await client.send_message(message.channel, "hi, i am bonzi buddy, to get started, plz type ./hell")
	elif message.content.startswith("}>hell"):
		await client.send_message(message.channel, "./bonzi and ./hell are actually a joke")
	elif message.content.startswith("}>debug"):
		message.author.id == "383561620661731329"
		if not message.author.id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
		    stripped_content = message.content[7:].strip()
		    result = eval(stripped_content)
		    result = str(result)
		    result2 = type(result)
		    result2 = str(result)
		    result3 = exec(stripped_content)
		    result3 = str(result)
		    await client.send_message(message.channel, "Eval:\n```Python\n" + result + "\n```" + "\nType:\n```Python\n" + result2 + "\n```" + "\nTraceback:\n```Python\n" + result3 + "\n```")
	elif message.content.startswith("<@413857586006458368> go eat shit The Pip"):
		await client.send_message(message.channel, "***throws a skittle at you***")
	elif message.content.startswith("<@413857586006458368> Hello. The Pip."):
		await client.send_message(message.channel, "Hello.")
	elif message.content.startswith("<@413857586006458368> fite me irl"):
		await client.send_message(message.channel, "Okay, fite me plez. ***throws a skittle at you***")
	elif message.content.startswith("}>botinfo"):
		embed=discord.Embed(title="Bot Info")
		embed.add_field(name="CleverBot prefix as a mention?", value="Yes.", inline=False)
		embed.add_field(name="Library used", value="discord.py", inline=False)
		embed.add_field(name="Editor used", value="Python IDLE 3.5.4+", inline=False)
		embed.add_field(name="Virtual Private Server?", value="Nope, not yet.", inline=True)
		embed.set_footer(text="Bot Version beta v1.7.98-release")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("}>ping"):
		await client.send_message(message.channel, "`Pong!`")
	elif message.content.startswith("}>shutdown"):
		message.author.id == "383561620661731329"
		if not message.author.id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
			await client.send_message(message.channel, "Now shutting down...")
			await asyncio.sleep(3)
			await client.send_message(message.channel, "Successful!")
			await client.logout()
	elif message.content.startswith("}>invite"):
		await client.send_message(message.channel, "```You can invite the bot here, but this has no music, so no musics.``` https://discordapp.com/api/oauth2/authorize?client_id=416163484414246912&permissions=0&scope=bot")
	elif message.content.startswith("<@413857586006458368> are u homeless or alone m8"):
		await client.send_message(message.channel, "yes mate")
	elif message.content.startswith("}>cleverbotinfo"):
		embed=discord.Embed(title="CleverBot Info")
		embed.add_field(name="Coded manually?", value="Yes mate.")
		embed.add_field(name="Used CleverBot API?", value="Nope.")
		embed.add_field(name="Prefix", value="A ping.")
		embed.set_footer(text="cleverbot v1.8b and credits goes to the CleverBot library.")
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("}>reboot"):
		message.author.id == "383561620661731329"
		if not message.author.id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
			await client.send_message(message.channel, "Please wait.. **Rebooting..**")
			await asyncio.sleep(3)
			await client.send_message(message.channel, "Success!")
			await client.logout()
	elif message.content.startswith("}>beta"):
		message.author.id == "383561620661731329"
		if not message.author. id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
			await client.send_message(message.channel, "Beta prototype now starting...")
			await asyncio.sleep(3)
			await client.send_message(message.channel, "**Successfully logged in!**")
			await client.login("NDE2NzUwMzQ5MTM1NzczNzA3.DXJAhw.JfnR9gJD5E1GuWbFej2qDR08Z1w")
	elif message.content.startswith("}>version"):
		message.author.id == "383561620661731329"
		if not message.author.id == "383561620661731329":
			await client.send_message(message.channel, "Bot developer only.")
		else:
			embed=discord.Embed(description="discord.py version : " + discord.__version__, color=0x3fffa3)
			embed.set_footer(text="Made by Ende Gerasimenko")
			await client.send_message(message.channel, embed=embed)
	elif message.content.startswith("}>eval"):
	    await client.send_message(message.channel, "A alias for `}>debug`, this command is a alias and not usuable.")
        
try:
    client.run(token)
except LoginFailure:
    print("invalid!")
