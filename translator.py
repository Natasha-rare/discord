import requests
from discord.ext import commands
from auth_data import DC_TOKEN, TRANSLATOR_API_KEY

TOKEN = DC_TOKEN
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = TRANSLATOR_API_KEY


class TransliteBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lang = 'en-ru'

    @commands.command(name='help_bot')
    async def help_bot(self, ctx):
        await ctx.send("инструкция")

    @commands.command(name='set_lang')
    async def set_lang(self, ctx, lang):
        self.lang = lang
        await ctx.send(lang)

    @commands.command(name='text')
    async def text(self, ctx, text):
        response = requests.get(URL, params={
            "key": API_KEY,
            "lang": self.lang,
            "text": text
        })
        data = response.json()
        print(data)
        await ctx.send(data['text'][0])


bot = commands.Bot(command_prefix='!!')
bot.add_cog(TransliteBot(bot))
bot.run(TOKEN)