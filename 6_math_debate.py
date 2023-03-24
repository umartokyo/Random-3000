def solution1():
    numbers = [1, 3, 5, 7, 9]          # инициализация списка чисел
    results = []                       # инициализация списка результатов

    for i in numbers:                  # перебор элементов списка numbers
        for l in numbers:              # вложенный перебор элементов списка numbers
            if i != l:                 # проверка, что i не равно l
                results.append(f"{i}{l}")  # добавление пары чисел в список результатов

    print(len(results))                # вывод количества пар | выдаст: 20
    print(results)                     # вывод списка результатов | выдаст: ['13', '15', '17', '19', '31', '35', '37', '39', '51', '53', '57', '59', '71', '73', '75', '79', '91', '93', '95', '97']


def solution2():
    numbers = [1, 3, 5, 7, 9]          # инициализация списка чисел
    numbers2 = [1, 3, 5, 7]            # инициализация второго списка чисел
    results = []                       # инициализация списка результатов

    for num1 in numbers:               # перебор элементов списка numbers
        for num2 in numbers2:          # вложенный перебор элементов списка numbers2
            results.append(f"{num1}{num2}")  # добавление пары чисел в список результатов

    print(len(results))                # вывод количества пар | выдаст: 20
    print(results)                     # вывод списка результатов | выдаст: ['11', '13', '15', '17', '31', '33', '35', '37', '51', '53', '55', '57', '71', '73', '75', '77', '91', '93', '95', '97']


solution1()
solution2()