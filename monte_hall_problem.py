# Monty Hall problem
from random import randint
print('Представьте, что вы стали участником игры, в которой вам нужно выбрать одну из трёх дверей. За одной из дверей находится автомобиль, за двумя другими дверями — козы. Вы выбираете одну из дверей, например, номер 1, после этого ведущий, который знает, где находится автомобиль, а где — козы, открывает одну из оставшихся дверей, например, номер 3, за которой находится коза. После этого он спрашивает вас — не желаете ли вы изменить свой выбор и выбрать дверь номер 2? Увеличатся ли ваши шансы выиграть автомобиль, если вы примете предложение ведущего и измените свой выбор?')
change_amount = 0
same_amount = 0
same_right = 0
change_right = 0
zoom = 0
print('Итак, начинаем нашу игру')
for i in range (10):
    auto_door = randint(1,3)
    print('Выберите дверь')
    door = input('1,2 or 3?')
    door_number = int(door)
    if door_number == 1:
        if auto_door == door_number:
            opened_door = randint(2,3)
        else:
            if auto_door == 2:
                opened_door = 3
            else:
                opened_door = 2
        print('Ведущий открывает дверь номер ',opened_door,' и за ней стоит коза')
        answer = input('Хотите изменить свой выбор?')
        if answer == 'да':
            change_amount = change_amount + 1
            if opened_door == 2:
                new_answer = 3
            else:
                new_answer = 2
            change_answer = new_answer
            if change_answer == auto_door:
                change_right = change_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                print('И за дверью........коза')
        else:
            same_amount = same_amount + 1
            if door_number == auto_door:
                same_right = same_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                 print('И за дверью........коза')          
    if door_number == 3:
        if auto_door == door_number:
            opened_door = randint(1,2)
        else:
            if auto_door == 2:
                opened_door = 1
            else:
                opened_door = 2
        print('Ведущий открывает дверь номер ',opened_door,' и за ней стоит коза')
        answer = input('Хотите изменить свой выбор?')
        if answer == 'да':
            change_amount = change_amount + 1
            if opened_door == 2:
                new_answer = 1
            else:
                new_answer = 2
            change_answer = new_answer
            if change_answer == auto_door:
                change_right = change_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                print('И за дверью........коза')
        else:
            same_amount = same_amount + 1
            if door_number == auto_door:
                same_right = same_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                 print('И за дверью........коза')
    if door_number == 2:
        if  auto_door == door_number:
            c = randint(1,2)
            if c == 1:
                print('Ведущий открывает дверь номер 1 и за ней стоит коза')
                zoom = 1
            else:
                print('Ведущий открывает дверь номер 3 и за ней стоит коза')
                zoom = 3
        else:
            if auto_door == 1:
                print('Ведущий открывает дверь номер 3 и за ней стоит коза')
                zoom = 3
            else:
                print('Ведущий открывает дверь номер 1 и за ней стоит коза')
                zoom = 1
        answer = input('Хотите изменить свой выбор?')
        if answer == 'да':
            change_amount = change_amount + 1
            if zoom == 1:
                change_answer = 3
            else:
                change_answer = 1
            if change_answer == auto_door:
                change_right = change_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                print('И за дверью........коза')
        else:
            same_amount = same_amount + 1
            if door_number == auto_door:
                same_right = same_right + 1
                print('Вы выиграли автомобиль!!!')
            else:
                 print('И за дверью........коза')
print('Игра закончилась, подводим итог')
if change_amount != 0:
    print('Процент выигрыша в случае изменения ответа составил: ',100*change_right/change_amount,'%')
else:
    print('измененных ответов не было')
if same_amount != 0:
    print('Процент выигрыша в случае не изменения ответа составил: ',100*same_right/same_amount,'%')
else:
    print('все ответы были изменены')
