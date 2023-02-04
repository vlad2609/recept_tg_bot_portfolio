from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_start_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('Книга рецептов 📕')], [KeyboardButton('Помощь')]
    ], resize_keyboard=True)

    return kb


menu_recept_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🍛 Супы')
b2 = KeyboardButton('🧆 Основные блюда')
b3 = KeyboardButton('🥗 Салаты и Закуски 🍢')
b4 = KeyboardButton('🥩 Гарниры и Соусы')
b5 = KeyboardButton('🥧 Сладенькое')
b6 = KeyboardButton('Предложить свой рецепт')
b7 = KeyboardButton('Назад')
menu_recept_kb.add(b1, b2).add(b3, b4).add(b5).add(b6, b7)
