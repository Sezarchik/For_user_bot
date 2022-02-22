from .. import loader, utils
import random
import pip
from bs4 import BeautifulSoup as BS
import subprocess
import logging
import requests

class PogodaMod(loader.Module):
    strings = {"name": "Weather"}

    async def wzcmd(self, message):
        msg = ' '.join(message.text.lower().split()[1:])
        r = requests.get(f'https://sinoptik.ua/погода-{msg}')
        html = BS(r.content, 'html.parser')
        for el in html.select('#content'):
          try:
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            noh = el.select('.temperature .p1')[0].text
            noch = el.select('.temperatureSens .p1')[0].text
            den = el.select('.temperature .p3')[0].text
            cden = el.select('.temperatureSens .p3')[0].text
            ytro = el.select('.temperature .p5')[0].text
            cytro = el.select('.temperatureSens .p5')[0].text
            text = el.select('.wDescription .description')[0].text
            vech = el.select('.temperature .p7')[0].text
            cvech = el.select('.temperatureSens .p7')[0].text
            tims = el.select('.lSide .today-time')[0].text
            grad = el.select('.lSide .today-temp')[0].text
            rasvet = el.select('.lSide .infoDaylight')[0].text
            await message.edit(f'<b>🌡 Погода на сегодня в {msg}:\n☀️ {rasvet}\n\nНа этот день: {t_min}, {t_max}\n{tims}: {grad}\n\n🌃 Ночью: {noh}, чувствуется как: {noch}\n🌅 Утром: {den}, чувствуется как: {cden}\n🏙 Днем: {ytro}, чувствуется как: {cytro}\n🌆 Вечером: {vech}, чувствуется как: {cvech}\n\n💬 {text[2:]}</b>')
          except:
            await message.edit(f'Город не найден!')