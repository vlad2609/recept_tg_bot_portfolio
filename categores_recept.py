from aiogram import types
from keyboards import get_start_kb
from list_of_recipe_references import *
import random



async def back_to_menu(message: types.Message):
    await message.delete()
    await message.answer('Выберите опцию...', reply_markup=get_start_kb())


async def admin_message_menu(message: types.Message):
    await message.delete()
    await message.answer('Привет! Если ты хочешь добавить\nсвой рецепт в наш бот или предложить видео\nиз ютуба, то напиши нашему менеджеру\n\n@Vladik2609')


async def soups_menu(message: types.Message):
    await message.delete()
    await message.answer(random.choice(soups))


async def main_dishes_menu(message: types.Message):
    await message.delete()
    await message.answer(random.choice(main_dishes))


async def salads_and_snacks_menu(message: types.Message):
    await message.delete()
    await message.answer(random.choice(salads_and_snacks))


async def side_dishes_and_sauces_menu(message: types.Message):
    await message.delete()
    await message.answer(random.choice(side_dishes_and_sauces))


async def dessert_menu(message: types.Message):
    await message.delete()
    await message.answer(random.choice(dessert))