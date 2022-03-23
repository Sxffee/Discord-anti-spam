import discord
import os
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=os.getenv('prefix'), intents=intents)
status = cycle(['No commands'])
client.remove_command('help')

@client.event
async def on_ready():
    change_status.start()
    print(f"Sucessfully logged in as {client.user}")
    while True:
            await asyncio.sleep(10)
            with open("spam-bank.txt", "r+") as file:
                file.truncate(0)

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity(type=discord.ActivityType.listening,name=str(len(client.guilds)) + " Server(s)."))

@client.event
async def on_message(message):
    guild = client.get_guild(952591652604772383)
    counter = 0
    
    with open("spam-bank.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1
        file.writelines(f"{str(message.author)+(' ')+str(message.author.id)}\n")
        if message.channel.id == 953323598809022554:
          return
        if counter > 5:
            await message.guild.ban(message.author, reason="Caught by Anti-Spam for Spamming")
            await asyncio.sleep(1)
            channel = guild.get_channel(952655140123476069)
            await channel.send(f"{message.author} was Banned by Anti-Spam for spamming..")


keep_alive()
client.run(os.getenv('token'))