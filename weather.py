锘縡rom .. import loader, utils
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
        r = requests.get(f'https://sinoptik.ua/锌芯谐芯写邪-{msg}')
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
            await message.edit(f'<b>馃尅 袩芯谐芯写邪 薪邪 褋械谐芯写薪褟 胁 {msg}:\n鈽�锔� {rasvet}\n\n袧邪 褝褌芯褌 写械薪褜: {t_min}, {t_max}\n{tims}: {grad}\n\n馃寖 袧芯褔褜褞: {noh}, 褔褍胁褋褌胁褍械褌褋褟 泻邪泻: {noch}\n馃寘 校褌褉芯屑: {den}, 褔褍胁褋褌胁褍械褌褋褟 泻邪泻: {cden}\n馃彊 袛薪械屑: {ytro}, 褔褍胁褋褌胁褍械褌褋褟 泻邪泻: {cytro}\n馃寙 袙械褔械褉芯屑: {vech}, 褔褍胁褋褌胁褍械褌褋褟 泻邪泻: {cvech}\n\n馃挰 {text[2:]}</b>')
          except:
            await message.edit(f'袚芯褉芯写 薪械 薪邪泄写械薪!')