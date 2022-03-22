print('Игра "Я угадаю число".')
print('Для общения с компьютером используйте следующие символы:')
buttons = ['< - число меньше загаданного', '> - число больше загаданного', '= - число равно загаданному']
for button in buttons:
    print(button)
print(' ')
print('Я начинаю угадывать.')

import random
number = random.randint(1, 100)
result = None
big_numbers = [100]
small_numbers = [1]
count = 0
while result != '=':
    count += 1
    print(f'Попытка № {count}')
    print(f'Число равно {number}')
    result = input('Верно? ')
    start = int(small_numbers[-1])
    stop = int(big_numbers[0])
    step = 1
    if result == '>':
        big_numbers.append(number)
        list.sort(big_numbers)
        stop = int(big_numbers[0])
        number = random.randrange(start, stop, step)
    elif result == '<':
        small_numbers.append(number)
        list.sort(small_numbers)
        start = int(small_numbers[-1]) + 1
        number = random.randrange(start, stop, step)
print(f'Ура, я выиграл с {count} попытки!')