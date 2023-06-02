from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def course_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='IELTS Pro - 400.000 сум', callback_data='ielts_pro')],
        [InlineKeyboardButton(text='IELTS Basic - 350.000 сум', callback_data='ielts_basic')],
        [InlineKeyboardButton(text='Pre-IELTS - 300.000 сум', callback_data='ielts_pre')],
        [InlineKeyboardButton(text='Beginner - 250.000 сум', callback_data='ielts_beginner')]

    ])
    return ikb


def teacher_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Abdurakhmon (head instructor)', callback_data='ins_abdurakhmon')],
        [InlineKeyboardButton(text='Bobur (head instructor)', callback_data='ins_bobur')],
        [InlineKeyboardButton(text='Madina (beginner)', callback_data='ins_madina')],
        [InlineKeyboardButton(text='Nazima (beginner)', callback_data='ins_nazima')]

    ])
    return ikb


def course_content_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Orqaga', callback_data='ielts_back')],
        [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="ielts_registration")]
    ])
    return ikb