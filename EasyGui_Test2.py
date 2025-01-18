from base64 import encode
import easygui as gui

title =  "Application"

#out = gui.ccbox("Зіграемо ще?", title, choices=("Так", "Ні"))
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.ynbox("Зіграемо ще?", title)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.boolbox("Зіграемо ще?", title)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.buttonbox(
#    "Скільки буде гравців?", title,
#    choices=[str(x) for x in range(1, 6)],
#    images=["python.png"] *3
#)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.indexbox(
#    "Скільки буде гравців?", title,
#    choices=[str(x) for x in range(1, 6)]
#)
#gui.msgbox(out, "Application", "Hello", image="python.png")

import os

files = os.listdir(os.getcwd())
#out = gui.choicebox("Оберіть файл", title, choices=files)

#out = gui.multchoicebox("Оберіть файл", title, choices=files)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.enterbox("Введить ім'я файлу", title, default="file.txt")
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.integerbox(
#    "Введіть вашу ставку", title, default=100,
#    lowerbound=10, upperbound=1000
#)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#fields = ("Им'я", "e-mail", "Телефон")
#values = ["Ivan", "ivan@fake.mail", "731273"]
#out = gui.multenterbox("Реестрация", title, fields, values)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#out = gui.passwordbox("Введить пароль")
#gui.msgbox(out, "Application", "Hello", image="python.png")

#fields = ("Логин", "Пароль")
#out = gui.passwordbox("Авторизация", title, fields)
#gui.msgbox(out, "Application", "Hello", image="python.png")

#file = open("EasyGui_Test2.py", encoding="utf-8")
#gui.textbox("EasyGui_Test2.py", title, text=file.read())

file = open("EasyGui_Test2.py", encoding="utf8")
gui.codebox("EasyGui_Test2.py", title, text=file.read())
