from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def list_of_course_teach_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Курсы')
    b2 = KeyboardButton('Учителя')
    kb.add(b1, b2)

    return kb


def teacher_list_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Abdurakhmon')
    b2 = KeyboardButton('Bobur')
    b3 = KeyboardButton('Madina')
    b4 = KeyboardButton('Nazima')
    kb.add(b1, b2).add(b3, b4)
    return kb


def ok_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Ok')
    kb.add(b1)
    return kb