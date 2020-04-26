import requests
import discord
from discord.ext import commands
from auth_data import DC_TOKEN, WEATHER_API_KEY

TOKEN = DC_TOKEN
URL = 'https://api.weather.yandex.ru/v1/forecast'
API_KEY = WEATHER_API_KEY


class WeatherBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.place = 'Moscow'
        self.days = 1

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        message = 'Commands:\n"#!current" напишет прогноз Москвы в данный момент\n' \
                  '"#!forecast" прогноз погоды в городе на несколько дней (n -  число)\n' \
                  '"#!place" меняет место на задданое'
        await ctx.send(message)



    @commands.command(name='current')
    async def current(self, ctx):
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/" \
                           f"?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Москва&format=json"
        response = requests.get(geocoder_request)
        json_response = response.json()
        # Выполняем запрос.
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        response_weather = requests.get(URL, params={
            "key": API_KEY,
            'lat': int(toponym_coodrinates[0]),
            'lon': int(toponym_coodrinates[1]),
            "limit": self.days
        })
        i = response_weather.json()['forecasts']
        a = f'Weather in Москва for {i["date"]}:\n'
        a += f'Temperature: {i["parts"]["day"]["temp_avg"]}\n'
        a += f'Pressure: {i["parts"]["day"]["pressure_mm"]} mm\n'
        a += f'Humidity: {i["parts"]["day"]["humidity"]}\n'
        a += f'Wind {i["parts"]["day"]["wind_dir"]}, {i["parts"]["day"]["wind_speed"]}'
        await ctx.send(a)

    @commands.command(name='forecast')
    async def show_forecast(self, ctx, days):
        self.days = days
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/" \
                           f"?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={self.place}&format=json"
        response = requests.get(geocoder_request)
        json_response = response.json()
        # Выполняем запрос.
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        response_weather = requests.get(URL, params={
            "key": API_KEY,
            'lat': int(toponym_coodrinates[0]),
            'lon': int(toponym_coodrinates[1]),
            "limit": self.days
        })
        data = response_weather.json()['forecasts']
        text = []
        for i in data:
            a = f'Weather in {self.place} for {i["date"]}:\n'
            a += f'Temperature: {i["parts"]["day"]["temp_avg"]}\n'
            a += f'Pressure: {i["parts"]["day"]["pressure_mm"]} mm\n'
            a += f'Humidity: {i["parts"]["day"]["humidity"]}\n'
            a += f'Wind {i["parts"]["day"]["wind_dir"]}, {i["parts"]["day"]["wind_speed"]}'
            text.append(a)
        await ctx.send(text)

    @commands.command(name='place')
    async def text(self, ctx, place):
        self.place = place
        await ctx.send(f"Place changed to {place}")


bot = commands.Bot(command_prefix='#!')
bot.add_cog(WeatherBot(bot))
bot.run(TOKEN)
