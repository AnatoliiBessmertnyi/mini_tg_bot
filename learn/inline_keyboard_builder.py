# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from modular_echo_bot.lexicon import LEXICON


# # Функция для формирования инлайн-клавиатуры на лету
# def create_inline_kb(width: int,
#                      *args: str,
#                      **kwargs: str) -> InlineKeyboardMarkup:
#     # Инициализируем билдер
#     kb_builder = InlineKeyboardBuilder()
#     # Инициализируем список для кнопок
#     buttons: list[InlineKeyboardButton] = []

#     # Заполняем список кнопками из аргументов args и kwargs
#     if args:
#         for button in args:
#             buttons.append(InlineKeyboardButton(
#                 text=LEXICON[button] if button in LEXICON else button,
#                 callback_data=button))
#     if kwargs:
#         for button, text in kwargs.items():
#             buttons.append(InlineKeyboardButton(
#                 text=text,
#                 callback_data=button))

#     # Распаковываем список с кнопками в билдер методом row c параметром width
#     kb_builder.row(*buttons, width=width)

#     # Возвращаем объект инлайн-клавиатуры
#     return kb_builder.as_markup()


from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env


env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()

LEXICON = {'but_1': '1',
           'but_2': '2',
           'but_3': '3',
           'but_4': '4',
           'but_5': '5'}

BUTTONS = {'btn_1': '1',
           'btn_2': '2',
           'btn_3': '3',
           'btn_4': '4',
           'btn_5': '5'}


# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(2, last_btn='Последняя кнопка', b_1='1', b_2='2', b_3='3', b_4='4', b_5='5')
    await message.answer(
        text='Это инлайн-клавиатура, сформированная функцией '
             '<code>create_inline_kb</code>',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
