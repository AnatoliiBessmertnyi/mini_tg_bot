# from aiogram import Bot, Dispatcher
# from aiogram.types import Message


# BOT_TOKEN = '6777882636:AAEwT4UsxcuKIEIUG8B3E2-nji4-OH3ncAI'

# # Создаем объекты бота и диспетчера
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()


# # def my_start_filter(message: Message) -> bool:
# #     return message.text == '/start'


# # Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(lambda msg: msg.text == '/start')
# async def process_start_command(message: Message):
#     await message.answer(text='Это команда /start')


# if __name__ == '__main__':
#     dp.run_polling(bot)

# def custom_filter(my_list):
#     return sum(i for i in my_list if isinstance(i, int) and i % 7 == 0) <= 83

# anonymous_filter = lambda my_str: my_str.lower().count('я') >= 23
# print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))



from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

BOT_TOKEN = '6777882636:AAEwT4UsxcuKIEIUG8B3E2-nji4-OH3ncAI'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
admin_ids: list[int] = []


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids
    
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

if __name__ == '__main__':
    dp.run_polling(bot)












