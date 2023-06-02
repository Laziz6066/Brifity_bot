import os
from dotenv import load_dotenv


load_dotenv('.env')
bot_token = os.getenv('TOKEN_API')

content_ielts_pro = "IELTS Pro \n\nUshbu kurs intensive hisoblanib unda kandidatlar 2 oydan 4 oygacha " \
                    "bo’lgan muddat davomida maksimal 6 - 8 ielts ball olishlari mumkin"

content_ielts_basic = "IELTS Basic \n\nUshbu kurs odatiy kurs hisoblanib unda kandidatlar 3 oydan 5 " \
                      "oygacha bo’lgan muddat davomida maksimal 6 - 7 IELTS ball olishlari mumkin"

content_ielts_pre = "Pre-IELTS\n\nUshbu kurs odatiy kurs hisoblanib unda  bazaviy ko’nikmalarga ega kandidatlar" \
                    " 6 oydan 8 oygacha bo’lgan muddat davomida maksimal 6 - 7 IELTS ball olishlari mumkin"

content_ielts_beginner = "Beginner\n\nUshbu kurs odatiy kurs hisoblanib unda boshlang’ich bazaviy kandidatlar 8  " \
                         "oydan 10 oygacha bo’lgan muddat davomida maksimal 6 - 7 ielts ball olishlari mumkin"


teacher_abdu = "Abdurakhmon (head instructor)\n\nShu o'qituvchi xaqida ma'lumot"

teacher_bob = "Bobur (head instructor)\n\nShu o'qituvchi xaqida ma'lumot"

teacher_mad = "Madina (beginner)\n\nShu o'qituvchi xaqida ma'lumot"

teacher_naz = "Nazima (beginner)\n\nShu o'qituvchi xaqida ma'lumot"