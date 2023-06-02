import sqlite3 as sq
from aiogram import types


async def db_start():
    try:
        db = sq.connect('register_student.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, '
                    'name TEXT, age TEXT, level TEXT, teacher TEXT, period TEXT, number_phone TEXT, '
                    'ok TEXT, course TEXT)')

        db.commit()

        return db, cur
    except Exception as e:
        print("Error during database initialization:", str(e))
        return None, None


async def create_profile(user_id, course, cur):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id = ?", (user_id,)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (user_id, '', '', '', '', '', '', '', course))
        cur.connection.commit()


async def edit_profile(state, user_id, course, cur):
    async with state.proxy() as data:
        name = data.get('name', '')
        age = data.get('age', '')
        level = data.get('level', '')
        teacher = data.get('teacher', '')
        period = data.get('period', '')
        number_phone = data.get('number_phone', '')
        ok = data.get('ok', '')

        cur.execute("UPDATE profile SET name = ?, age = ?, level = ?, "
                    "teacher = ?, period = ?, number_phone = ?, ok = ?, course = ? WHERE user_id = ?",
                    (name, age, level, teacher, period, number_phone, ok, course, user_id))

        cur.connection.commit()


async def get_profiles(cur):
    cur.execute("SELECT * FROM profile")
    profiles = cur.fetchall()
    return profiles
