    #Написать генератор случайных матриц(многомерных), который принимает
    #опциональные параметры m, n, min_limit, max_limit, где m и n указывают размер
    #матрицы, а min_lim и max_lim - минимальное и максимальное значение для
    #генерируемого числа . По умолчанию при отсутствии параметров принимать следующие
    #значения:
        #m = 50
        #n = 50
        #min_limit = -250
        #max_limit = 1000 + (номер своего варианта)

from random import randint          #БИБЛИОТЕКА РАНДОМА

#ФУНКЦИЯ ГЕНЕРАЦИИ МАТРИЦЫ
def createMatrix():
    print('Команда 1: Ввести параметры матрицы вручную')
    print('Команда 2: Ввести дефолтные параметры матрицы')
    print('Введите номер команды: ')
    ask = int(input())

    while (True):
        if (ask == 1):
            print('Введите индекс n: ')            #ВВОД ПОЛЬЗОВАТЕЛЕМ ЗНАЧЕНИЙ
            n = int(input())
            print('Введите индекс m: ')
            m = int(input())
            print('Введите минимальное значение интервала рандома: ')
            min_limit = int(input())
            print('Введите максимальное значение интервала рандома: ')
            max_limit = int(input())

            # ЗАПОЛНЕНИЕ РАНДОМНЫМИ ЗНАЧЕНИЯМИ В ИНТЕРВАЛЕ (min_limit, max_limit)
            matrix = [[randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
            return matrix
            break

        elif (ask == 2):
            n = 50
            m = 50
            min_limit = -250
            max_limit = 1000 + 2

            # ЗАПОЛНЕНИЕ РАНДОМНЫМИ ЗНАЧЕНИЯМИ В ИНТЕРВАЛЕ (min_limit, max_limit)
            matrix = [[randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
            return matrix
            break

        else:
            print('Такой команды не существует, введите команду из перечисленных! (1-заполнить вручную, 2-заполнить дефолтными значениями)')
            ask = int(input())

#ФУНКЦИЯ ВЫВОДА МАТРИЦЫ
def outputMatrix():
    matrix = createMatrix()
    print('МАТРИЦА: ')
    for i in range(len(matrix)):
        print(matrix[i])

#ВЫЗОВ ФУНКЦИИ ВЫВОДА
#outputMatrix()

