from .. import loader, utils
import random

class InsultsMod(loader.Module):
	strings = {"name": "InsultsSpam"}
	
	async def insultscmd(self,message):
		insults = "ведроносальщик мразоскрытный., мочеед гееблядский., машонколиз хуепроклятый., мыловозальщик ветропиздабольный., карманоёб кожевозный., аналоканальный течкопад., хуекентовый блядоклоун., кровоносый въеблоуказник., калоклал педосрущий., гноеирод червебливый., ебленьтяй губорвущий., пиздозлыбень неподпёздковый., порядкошныревой рабоёбанат., швалегадкое гандономышище., педовод еблеухий., бредомразный калоглот., жопопроклятый спиногрыз., тваремразный очкоглот., гноепохабная еблеводка., грозносос отцерезный., страпоноёбок мелкопиздливый., блядогавнарь шныреглазый., ёблесучище хреномразное., мразалупоед чмырегнойный., ширинколаз зубодроченный., очкопорванный тухлоёбщик., стволоёб шестивольтовый., целкоразводной петуховод., мразовыдолбок мышехуйчатый., целкосрывер пикохуйчатый., вафлеёбище гноесосное., блядконаротанский прыщегадкий., пиздощепилявный вагиновод., блядопедовка шлюшепухшая., хуеман долбомразный., яйцедонный высрогнойщик., хуежгучий кончелов., кривосручий педроёба., пиздовыкидышный залупоноид., духоёбский пиздорез., хлеборезка разгондонная., геевоющий шмарорван., клиторван губогнойный., сердцеёб шавкомышиный., гнидобездарный аналоблядильщик., спермогарьная шлюхогойка., вагинолизный педоглитс., целкогнидный гнётопёздок., тварепиздошная выбурлында., выблядятел блядодёрнутый., кончелиз рукаёбищный., пиздецелка мразокривоногая., шныреглот хуемразный., мразопетушынный глистожоп., мерзоблядый тварехуй., глазозалупцовый выхуйник., дыропроебатель дыродуйчатый., губосос спермотаксикозный., ядокаловый червеотравитель., пиздамелкий дерьмопроёбщик., апиздахуйчатый блядошавкаглист., хуесучее бесоёбище., уёбкомразый кривоеблонодонище., гнида., мразь., пидорас., сука., кобель., уебище., гомункул., баран., даун., козёл., импотент., дрочун., долбоящер., долбаеб., гандон., гей., пидор., педик., чепушила., шлюха., быдло., осел., олень., сукин сын., петух., курица., залупа."
		insults = insults.split(", ")
		await message.edit("ты:")
		args = utils.get_args_raw(message)
		for i in range (0, int(args)):
			rand = random.choice(insults)
			await message.respond(rand)
