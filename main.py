from aiogram import Bot, Dispatcher, executor
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
from function_menu_recept import cmd_start, open_recept, open_help
from categores_recept import *


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


dp.register_message_handler(cmd_start, commands='start')
dp.register_message_handler(open_recept, Text(equals='Книга рецептов 📕'))
dp.register_message_handler(open_help, Text(equals='Помощь'))
dp.register_message_handler(back_to_menu, Text(equals='Назад'))

# Menu recept
dp.register_message_handler(soups_menu, Text(equals='🍛 Супы'))
dp.register_message_handler(main_dishes_menu, Text(equals='🧆 Основные блюда'))
dp.register_message_handler(salads_and_snacks_menu, Text(equals='🥗 Салаты и Закуски 🍢'))
dp.register_message_handler(side_dishes_and_sauces_menu, Text(equals='🥩 Гарниры и Соусы'))
dp.register_message_handler(dessert_menu, Text(equals='🥧 Сладенькое'))
dp.register_message_handler(admin_message_menu, Text(equals='Предложить свой рецепт'))


if __name__ == '__main__':
    executor.start_polling(skip_updates=True,
                           dispatcher=dp)
