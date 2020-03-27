import requests

import discord

from auth_data import DC_TOKEN
TOKEN = DC_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user.id} покажет котиков и пёсиков!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "кот" in message.content.lower():
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        await message.channel.send(data[0]['url'])
    dogs = [
        "пес", "пёс", "собак", "собач", "бобик", "тузик", "полкан"
    ]
    if any([dog in message.content.lower() for dog in dogs]):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        await message.channel.send(data['message'])


client.run(TOKEN)

