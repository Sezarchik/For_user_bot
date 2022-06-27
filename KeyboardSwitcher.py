# meta developer: tg://openmessage?user_id=1707984808

import logging
from .. import loader, utils
import telethon

logger = logging.getLogger(__name__)


async def register(cb):
    cb(KeyboardSwitcherMod())


@loader.tds
class KeyboardSwitcherMod(loader.Module):
    """Смена расскаладки клавиатуры у текста"""
    strings = {
        "name": "KeyboardSwitcher"}

    async def switchcmd(self, message):
        """Если ты допустил ошибку и набрал текст не сменив раскладку клавиатуры
то вернись в его начало и допиши `.switch` и твой текст станет читабельным.
Если ты всё же отправил сообщение не в той расскладке, то просто ответь на него этой командой и он измениться.
если же твой собеседник допустил ошибку, то просто ответь на его сообщение и сообщение с командой измениться."""
        RuKeys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
        EnKeys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""

        if message.is_reply:
            reply = await message.get_reply_message()
            text = reply.raw_text
            if not text:
                message = await utils.answer(message, 'Тут текста нету...')
                return
            change = str.maketrans(RuKeys + EnKeys, EnKeys + RuKeys)
            text = str.translate(text, change)

            if message.sender_id != reply.sender_id:
                message = await utils.answer(message, text)
            else:
                await message.delete()
                await reply.edit(text)

        else:
            text = utils.get_args_raw(message)
            if not text:
                message = await utils.answer(message, 'Тут текста нету...')
                return
            change = str.maketrans(RuKeys + EnKeys, EnKeys + RuKeys)
            text = str.translate(text, change)
            message = await utils.answer(message, text)
