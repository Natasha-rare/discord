import requests

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
        hour = int(message.content.lower().split()[4])

        await message.channel.send(data[0]['url'])
        date = datetime.datetime.now()
    dogs = [
        "пес", "пёс", "собак", "собач", "бобик", "тузик", "полкан"
    ]
    if any([dog in message.content.lower() for dog in dogs]):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        await message.channel.send(data['message'])


client.run(TOKEN)

