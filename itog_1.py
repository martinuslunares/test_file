from random import choice

f = open('cities.txt', encoding='utf-8')
cities_list = [line.strip() for line in f]

answer = open('answers.txt', 'a+', encoding='utf-8')
answers_list = [line.strip() for line in answer]

iskl = ['ё', 'й', 'ц', 'ъ', 'ы', 'ь']



def proverka_goroda(): # проверка города от пользователя
    user = input('Ваш ход: ')
    if user in answers_list:  # проверяем был ли город ранее назван
        print('Город уже был')

        return

    if user not in cities_list:  # проверяем существует ли город в списке
        print('Такого города нет в списке!')

        return

    word = answers_list[-1]
    first_letter = word[0].lower() if word[-1].lower() in iskl else word[-1].lower()

    if user[0].lower() != first_letter:  # проверка на первую букву
        print(f'Город должен начинаться на букву "{first_letter}".')

        return

    answers_list.append(user)
    return user


def generator_g_computer(computer,cities_list, answers_list): # генерация города от компьютера
    word = answers_list[-1]
    computer = None

    first_letter = word[0].lower() if word[-1].lower() in iskl else word[-1].lower() # определение первой буквы если искл и не искл

    for city in cities_list:
        if city.lower().startswith(first_letter) and city not in answers_list:
            computer = city
            break

    if computer: #если тру
        answers_list.append(computer)
        print('Ход компьютера:', computer)

        if computer[-1].lower() in iskl:
            print(f'Компьютер назвал город на "{computer[-1]}". Вам нужно ввести город на первую букву "{computer[0]}".')
    else:
        print('Компьютер не может найти город. Вы выиграли!')
        return computer

computer = choice(cities_list) # начало игры
if computer[-1].lower() in iskl:
    print('Первый ходит компьютер:', computer)
    print(f'Компьютер назвал город на "{computer[-1]}". Вам нужно ввести город на первую букву "{computer[0]}".')
else:
    print('Ход компьютера:', computer)
answers_list.append(computer)
user_try = 0
while user_try < 5 :
    if proverka_goroda() is None:
        user_try += 1
        if user_try >= 5:
            print('Вы проиграли')
        else:
            print('попробуйте еще раз')
            continue
    generator_g_computer(computer, cities_list, answers_list)

