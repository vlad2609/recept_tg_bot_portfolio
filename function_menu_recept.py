from aiogram import types
from keyboards import get_start_kb, menu_recept_kb


async def cmd_start(message: types.Message):
    await message.delete()
    await message.answer('👨‍🍳Приветствую! Ты только что запустил лучшего своего помощника на кухне, может даже и друга). Здесь ты найдешь\nне только'
                         ' рецепты но и советы приготовлении блюда.🍳\n\nЕсли ты не знаком '
                         'с использованием бота, то\nнажми на <b>Помощь</b>', parse_mode='HTML', reply_markup=get_start_kb())
    await message.answer('Выберете опцию...')


async def open_recept(message: types.Message):
    await message.delete()
    await message.answer('Выберите категорию...',
                         reply_markup=menu_recept_kb)


async def open_help(message: types.Message):
    await message.delete()
    await message.answer('Ты попал в раздел <b>Помощь</b> 👮‍♀️\n\n'
                         'Чтобы посмотреть рецепты главных блюд\nна твой вкусненький вечер стоит нажать\nна главном меню <b>Книга рецептов 📕</b>.\n\n'
                         'А дальше тебя ждет меню с выбором раздела категории\nкакого рецепта блюда ты хочешь. '
                         'Ну а дальше ты все поймешь уже сам).\n'
                         'При нажатии на выбранную категорию появится ссылка\n'
                         'на видео рецепт, а также вы можете по повторному нажатию получить другой рецепт\n\n'
                         '<i><b>Приятного аппетита)</b> 🍝🍜🍲</i>',
                         parse_mode='HTML',
                         reply_markup=get_start_kb())