import discord

from auth_data import DC_TOKEN
TOKEN = DC_TOKEN

import datetime

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user.id} покажет котиков и пёсиков!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "set_timer" in message.content.lower():
        hour = int(message.content.lower().split()[2])
        minute = int(message.content.lower().split()[4])

        await message.channel.send(f'The timer should start in {hour} hours and {minute} minutes')
        date = datetime.datetime.now()
        delta = datetime.timedelta(hours=hour, minutes=minute)
        flag = True
    if flag:
        while True:
            if datetime.datetime.now() >= date + delta:
                await message.channel.send('Time X has come!')
                flag = False
                break
