import easygui as gui
import random

rock_image = "rock.png"
scissors_image = "scissors.png"
paper_image = "paper.png"

def rock_paper_scissors():

    choices = [
        {"label": "Камень", "image": rock_image},
        {"label": "Ножницы", "image": scissors_image},
        {"label": "Бумага", "image": paper_image},
    ]

    while True:
        user_choice = gui.buttonbox(
            "Выбери один из вариантов:",
            "Камень, Ножницы, Бумага",
            choices=[c["label"] for c in choices],
            images=[c["image"] for c in choices]
        )
        
        if not user_choice: 
            gui.msgbox("Игра завершена. До встречи!", "Выход")
            break

        computer_choice = random.choice(choices)["label"]
        
        result = f"Твой выбор: {user_choice}\nВыбор компьютера: {computer_choice}\n\n"
        
        if user_choice == computer_choice:
            result += "Ничья!"
        elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
             (user_choice == "Ножницы" and computer_choice == "Бумага") or \
             (user_choice == "Бумага" and computer_choice == "Камень"):
            result += "Ты победил!"
        else:
            result += "Ты проиграл!"
        
        gui.msgbox(result, "Результат")

        play_again = gui.ynbox("Хочешь сыграть ещё раз?", "Продолжить?", ["Да", "Нет"])
        if not play_again:
            gui.msgbox("Спасибо за игру!", "Выход")
            break

    rock_paper_scissors()

def guess_the_number():
    gui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = gui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()
