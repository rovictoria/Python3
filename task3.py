# Задача 1. Создайте файл. Запишите в него N первых элементов
# последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
print('1. Запись N элементов последовательности Фибоначчи: ') 
def Fibonacci_numbers():
    last_element = 0
    next_element = 1
    N = int(input('Введите количество элементов: '))
    data = open('fibonacci.txt', 'w')
    for i in range(N):
        print(last_element, end = ' ')
        data.writelines(str(last_element) + '\n')
        (last_element, next_element) = (next_element, last_element + next_element)

Fibonacci_numbers()
print(' ')

# Задача 2. В файле находятся названия фруктов. Выведите все
# фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
print('2. Вывод фруктов на заданную букву: ') 

def Find_fruits():
    data = open('fruits.txt', encoding = 'utf-8')
    letter = input('Введите 1 букву для поиска: ')
    for fruct in data:
        if fruct[0].lower() == letter.lower():
            print(fruct)

Find_fruits()

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий
print('3. Первый лёгкий бот (напишите "выход" для завершения работы): ')

dictionary = \
    {
        'привет': 'Доброго времени суток',
        'Привет': 'Здравствуйте!',
        'как тебя зовут': 'Бот-Борис',
        'Как тебя зовут': 'Меня зовут Бот-Борис',
        'как дела': 'Неплохо, общаюсь с вами',
        'Как дела': 'Хорошо, спасибо за интерес',
        'Выход': 'Хорошего дня! :)',
        'выход': 'Хорошего дня! :)'
    } 

def First_bot():
    active = True
    while active:
        answer = input('Пользователь: ')
        if answer in dictionary.keys():
            print('Бот: ', dictionary[answer])
        else:
            print('Бот: Неизвестная команда')
        if answer.lower() == 'выход':
            active = not active

First_bot()
