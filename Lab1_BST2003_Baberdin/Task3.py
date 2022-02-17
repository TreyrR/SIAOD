#Реализовать методы сортировки строк числовой матрицы в соответствии с
#заданием. Оценить время работы каждого алгоритма сортировки и сравнить его со
#временем стандартной функции сортировки. Испытания проводить на сгенерированных
#матрицах.
#Используемые сортировки: выбором, вставкой, обменом, шелла, турнирная, быстрая, пирамидальная

import time
import Task2
from random import randint
import copy
import math

#ФУНКЦИЯ СОРТИРОВКИ ВЫБОРОМ
def selectSort(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1):
            for k in range(j + 1, len(matrix[0])):
                if matrix[i][k] < matrix[i][j]:
                    matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
    return matrix

#ФУНКЦИЯ СОРТИРОВКИ ВСТАВКОЙ
def pasteSort(matrix):
    for row in range(len(matrix)):
        for col in range(1, len(matrix[0])):
            key = matrix[row][col]
            j = col - 1
            while j >= 0 and key < matrix[row][j]:
                matrix[row][j + 1] = matrix[row][j]
                j -= 1
            matrix[row][j + 1] = key
    return matrix

#ФУНКЦИЯ СОРТИРОВКИ ОБМЕНОМ
def tradeSort(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0]) - 1):
            for j in range(len(matrix[0]) - col - 1):
                if matrix[row][j] > matrix[row][j + 1]:
                    matrix[row][j], matrix[row][j + 1] = matrix[row][j + 1], matrix[row][j]
    return matrix

#ФУНКЦИЯ СОРТИРОВКИ ШЕЛЛА
def shellSort(matrix):
    n = len(matrix[0])
    k = int(math.log2(n))
    interval = int(2 ** k - 1)
    while interval > 0:
        for row in range(len(matrix)):
            for col in range(interval, n):
                temp = matrix[row][col]
                j = col
                while j >= interval and matrix[row][j - interval] > temp:
                    matrix[row][j] = matrix[row][j - interval]
                    j -= interval
                matrix[row][j] = temp
        k -= 1
        interval = int(2 ** k - 1)
    return matrix

#ФУНКЦИЯ ТУРНИРНОЙ СОРТИРОВКИ
def tournamentSort(matrix):
    tree = [None] * 2 * (len(matrix) + len(matrix) % 2)
    index = len(tree) - len(matrix) - len(matrix) % 2

    for i, v in enumerate(matrix):
        tree[index + i] = (i, v)

    for j in range(len(matrix)):
        n = len(matrix)
        index = len(tree) - len(matrix) - len(matrix) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n

        index, x = tree[0]
        matrix[j] = x
        tree[len(tree) - len(matrix) - len(matrix) % 2 + index] = None

def TournamentSort(matrix):
    for i in range(len(matrix)):
        tournamentSort(matrix[i])
    return matrix

#ФУНКЦИЯ БЫСТРОЙ СОРТИРОВКИ
def partition(matrix, low, high, row):
    pivot = matrix[row][(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while matrix[row][i] < pivot:
            i += 1

        j -= 1
        while matrix[row][j] > pivot:
            j -= 1

        if i >= j:
            return j

        matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]

def fastSort(matrix):
    def _quick_sort(items, low, high,row):
        if low < high:
            split_index = partition(items, low, high,row)
            _quick_sort(items, low, split_index,row)
            _quick_sort(items, split_index + 1, high,row)

    for row in range(len(matrix)):
        _quick_sort(matrix, 0, len(matrix[row])-1,row)

    return matrix

#ФУНКЦИЯ ПИРАМИДАЛЬНОЙ СОРТИРОВКА
def heapify(matrix, n, i, row):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and matrix[row][i] < matrix[row][l]:
        largest = l
    if r < n and matrix[row][largest] < matrix[row][r]:
        largest = r

    if largest != i:
        matrix[row][i], matrix[row][largest] = matrix[row][largest], matrix[row][i]
        heapify(matrix, n, largest, row)


def piramidSort(matrix):
    for row in range(len(matrix)):
        n = len(matrix[0])
        for i in range(n // 2, -1, -1):
            heapify(matrix, n, i, row)
        for i in range(n - 1, 0, -1):
            matrix[row][i], matrix[row][0] = matrix[row][0], matrix[row][i]
            heapify(matrix, i, 0, row)
    return matrix


#ГЕНЕРИРУЕМ МАТРИЦУ И ЗАПИСЫВАЕМ В ПЕРЕМЕННУЮ
matrix = Task2.createMatrix()

#ВЫЗОВ ЧТОБЫ ВЫВЕСТИ 2 МАТРИЦЫ
selectSort_matrix = copy.deepcopy(matrix)
selectSort(selectSort_matrix)

#ВЫВОД НЕОТСОРТИРОВАННОЙ МАТРИЦЫ
print('НЕОТСОРТИРОВАННАЯ МАТРИЦА')
print('--------------------------------------------------------------------------------------')
for u in range(len(matrix)):
     print(matrix[u])
print('--------------------------------------------------------------------------------------')
#ВЫВОД ОТСОРТИРОВАННОЙ МАТРИЦЫ
print('ОТСОРТИРОВАННАЯ МАТРИЦА')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for u in range(len(selectSort_matrix)):
     print(selectSort_matrix[u])
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


#СОРТИРОВКА ВЫБОРОМ
#КОПИРУЕМ ОТСОРТИРОВАННУЮ МАТРИЦУ В НОВУЮ ПЕРЕМЕННУЮ
selectSort_matrix = copy.deepcopy(matrix)
#ФИКСИРУЕМ ВРЕМЯ
startTime = time.time()
#ВЫЗОВ ФУНКЦИИ ВЫБОРОЧНОЙ СОРТИРОВКИ
selectSort(selectSort_matrix)
#ПОДСЧЁТ ВРЕМЕНИ ВЫПОЛНЕНИЯ СОРТИРОВКИ
endTime = time.time() - startTime
print("Время выполнения сортировкой выбора: ",'%.3f' %endTime,"сек")
print('_________________________')

#CОРТИРОВКА ВСТАВКОЙ
pasteSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
pasteSort(pasteSort_matrix)
endTime = time.time() - startTime
print("Время выполнения сортировкой вставки: ",'%.3f' %endTime,"сек")
print('_________________________')

#СОРТИРОВКА ОБМЕНОМ
tradeSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
tradeSort(tradeSort_matrix)
endTime = time.time() - startTime
print("Время выполнения сортировкой обмена: ",'%.3f' %endTime,"сек")
print('_________________________')

#СОРТИРОВКА ШЕЛЛА
shellSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
shellSort(shellSort_matrix)
endTime = time.time() - startTime
print("Время выполнения сортировкой Шелла: ",'%.3f' %endTime,"сек")
print('_________________________')

#ТУРНИРНАЯ СОРТИРОВКА
tournamentSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
TournamentSort(tournamentSort_matrix)
endTime = time.time() - startTime
print("Время выполнения турнирной сортировкой: ",'%.3f' %endTime,"сек")
print('_________________________')

#БЫСТРАЯ СОРТИРОВКА
fastSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
fastSort(fastSort_matrix)
endTime = time.time() - startTime
print("Время выполнения быстрой сортировкой: ",'%.3f' %endTime,"сек")
print('_________________________')

#ПИРАМИДАЛЬНАЯ СОРТИРОВКА
piramidSort_matrix = copy.deepcopy(matrix)
startTime = time.time()
piramidSort(piramidSort_matrix)
endTime = time.time() - startTime
print("Время выполнения пирамидальной сортировкой: ",'%.3f' %endTime,"сек")
print('_________________________')

# for u in range(len(matrix)):
#     print(matrix[u])
#print("Время выполнения: ",'%.3f' %endTime,"сек")
# for u in range(len(selectSort_matrix)):
#     print(selectSort_matrix[u])
