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



# from aiogram import Bot, Dispatcher
# from aiogram.filters import BaseFilter
# from aiogram.types import Message

# BOT_TOKEN = '6777882636:AAEwT4UsxcuKIEIUG8B3E2-nji4-OH3ncAI'
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
# admin_ids: list[int] = [552434688]


# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         self.admin_ids = admin_ids
    
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids


# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='Вы админ')


# @dp.message()
# async def answer_if_not_admins_update(message: Message):
#     await message.answer(text='Вы не админ')

# if __name__ == '__main__':
#     dp.run_polling(bot)


from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message, PhotoSize


BOT_TOKEN = '6777882636:AAEwT4UsxcuKIEIUG8B3E2-nji4-OH3ncAI'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.strip(',.!-')
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем словарь со списком чисел по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')


@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    print(photo_min)


if __name__ == '__main__':
    dp.run_polling(bot)






