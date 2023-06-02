from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def list_of_course_teach_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Kurslar')
    # b2 = KeyboardButton('Instruktorlar')
    kb.add(b1)

    return kb


def teacher_list_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton('Abdurakhmon')
    b2 = KeyboardButton('Bobur')
    b3 = KeyboardButton('Madina')
    b4 = KeyboardButton('Nazima')
    kb.add(b1, b2).add(b3, b4)
    return kb


def lang_lev_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("Boshlang'ich (Beginner)")
    b2 = KeyboardButton('Elementar (Elementary)')
    b3 = KeyboardButton("O'rtachadan past (Pre-Intermediate)")
    b4 = KeyboardButton("O'rtacha (Intermediate)")
    b5 = KeyboardButton("O'rtachadan yuqori (Upper-Intermediate)")
    b6 = KeyboardButton("Mukammal (Advanced)")
    b7 = KeyboardButton("Professional (Proficiency)")
    kb.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7)
    return kb


def ok_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("Ma'lumotlar to'gri kiritildi")
    kb.add(b1)
    return kb