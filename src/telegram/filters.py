from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import BoundFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE