#coding: utf-8
from random import randint
import time
import copy



def Print(mas, n):
    for i in range (int(n)):
        print(mas[i], end=' ')
    print()

#бинарный поиск
def binary_search(array, value):
    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != value and low <= high:
        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("Искомого числа в массиве нет")
    else:
        print("Индекс: ", mid)


# Фибоначчиев поиск
def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1
    return -1

#Интерполяционный
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1


#Бинарное дерево

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, ' найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root

def Insert(mas):
    print("Хотите внести элемент? ")
    ans = input()
    if ans=="да" or ans =="Да":
        el = int(input("Введите число: "))
        index = int(input("Введите индекс: "))
        mas.insert(index, el)
        Print(mas, n + 1)



def Delete(mas):
    print("Хотите удалить элемент? ")
    ans = input()
    if ans == "да" or ans == "Да":
        index = int(input("Введите индекс: "))
        del mas[index]
        Print(mas, n - 1)

#Программа

#генерация массива
n = int(input("Введите количество элементов массива: "))
min_limit = input("Укажите начальный диапозон чисел для генерации: ")
max_limit = input("Укажите конечный диапозон чисел для генерации: ")
mas = [randint(int(min_limit), int(max_limit)) for i in range(int(n))]


print("Сгененированный массив: ")
Print(mas,n)

mas.sort()
print("Отсортированный массив: ")
Print(mas, n)

#бинарный поиск
print("Бинарный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_bin = copy.deepcopy(mas)
start_time_bin = time.time()
binary_search(mas_bin, element)
end_time_bin = time.time()-start_time_bin
print(end_time_bin)
Insert(mas_bin)
Delete(mas_bin)


#интерполяционный поиск
print("Интерполяционный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_inter = copy.deepcopy(mas)
start_time_inter = time.time()
b = InterpolationSearch(mas_inter, element)
end_time_inter = time.time()-start_time_inter
if b == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", b)
print("Время работы: ", end_time_inter)
Insert(mas_inter)
Delete(mas_inter)


#Фибоначчиев поиск
print("Фибоначчиев поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_fib = copy.deepcopy(mas)
start_time_fib = time.time()
a = FibonacciSearch(mas_fib,element)
end_time_fib = time.time()-start_time_fib
if a == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", a)
print("Время работы: ", end_time_fib)
Insert(mas_fib)
Delete(mas_fib)

#Бинарное деререво
print("Бинарное деререво")
mas_tree = copy.deepcopy(mas)
root = make_a_tree(mas_tree)
num = int(input("Введите элемент, который хотите найти: "))
start_time_tree = time.time()
result = root.findval(num)
end_time_tree = time.time() - start_time_tree
task = input("Хотите внести элемент? ")
if task == "да" or task =="Да":
    num = int(input("Введите элемент, который хотите внести: "))
    root.insert(num)
    root.PrintTree()
task = input("Хотите удалить элемент? ")
if task == "да" or task =="Да":
    num = int(input("Введите элемент, который хотите удалить: "))
    mas_tree.remove(num)
    root = make_a_tree(mas_tree)
    root.PrintTree()

print("Время работы: ", end_time_tree)