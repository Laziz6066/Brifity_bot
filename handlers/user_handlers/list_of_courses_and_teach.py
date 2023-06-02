from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards.inline_kb import course_ikb, teacher_ikb, course_content_ikb
from loader import bot
from config_data.config import content_ielts_pre, content_ielts_basic, content_ielts_pro, content_ielts_beginner
from config_data.config import teacher_abdu, teacher_bob, teacher_mad, teacher_naz
from states.user_state import StudentRegister


async def list_of_courses(message: types.Message):
    if message.text == 'Kurslar':
        await message.answer(text='<b>Mavjud kurslar</b>', reply_markup=course_ikb(), parse_mode='html')
    # elif message.text == 'Instruktorlar':
    #     await message.answer(text='<b>Instruktorlar</b>', reply_markup=teacher_ikb(), parse_mode='html')
    await message.delete()


async def button_click_handler(query: types.CallbackQuery):
    if query.data == 'ins_abdurakhmon':
        await bot.answer_callback_query(query.id, text=teacher_abdu, show_alert=True)
    elif query.data == 'ins_bobur':
        await bot.answer_callback_query(query.id, text=teacher_bob, show_alert=True)
    elif query.data == 'ins_madina':
        await bot.answer_callback_query(query.id, text=teacher_mad, show_alert=True)
    elif query.data == 'ins_nazima':
        await bot.answer_callback_query(query.id, text=teacher_naz, show_alert=True)


async def handle_button_click(query: types.CallbackQuery, state: FSMContext):
    data = query.data
    if data == 'ielts_pro':
        async with state.proxy() as data:
            data['course'] = 'IELTS Pro'
        await query.message.edit_text(text=content_ielts_pro, reply_markup=course_content_ikb())
    elif data == 'ielts_basic':
        async with state.proxy() as data:
            data['course'] = 'IELTS Basic'
        await query.message.edit_text(text=content_ielts_basic, reply_markup=course_content_ikb())
    elif data == 'ielts_pre':
        async with state.proxy() as data:
            data['course'] = 'Pre-IELTS'
        await query.message.edit_text(text=content_ielts_pre, reply_markup=course_content_ikb())
    elif data == 'ielts_beginner':
        async with state.proxy() as data:
            data['course'] = 'Beginner'
        await query.message.edit_text(text=content_ielts_beginner, reply_markup=course_content_ikb())
    elif data == 'ielts_back':
        await query.message.edit_text(text='Kurslar', reply_markup=course_ikb())
    elif data == 'ielts_registration':
        await query.message.edit_text(text='Sizning Ism Familyangiz')
        await StudentRegister.next()


def register_handler_list_cour(dp: Dispatcher):
    dp.register_message_handler(list_of_courses, Text(equals='Kurslar'))
    dp.register_message_handler(list_of_courses, Text(equals='Instruktorlar'))
    dp.register_callback_query_handler(button_click_handler, lambda query: query.data.startswith('ins'))
    dp.register_callback_query_handler(handle_button_click, lambda query: query.data.startswith('ielts'))

