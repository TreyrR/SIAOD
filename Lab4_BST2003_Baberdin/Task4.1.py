#  -*- coding: utf-8 -*-
#Реализовать следующие структуры данных:

# Стек (stack):
#Операции для стека: инициализация, проверка на пустоту, добавление нового элемента в начало, извлечение элемента из начала;

# Дек (двусторонняя очередь, deque):
#Операции для дека: инициализация, проверка на пустоту, добавление нового элемента в начало, добавление нового элемента в конец,
# извлечение элемента из начала, извлечение элемента из конца.

#Разработать программу обработки данных, содержащихся в заранее подготовленном txt-файле, в соответствии с заданиями,
# применив указанную в задании структуру данных. Результат работы программы вывести на экран и сохранить в отдельном txt-файле.

class Stack:
#Ссылочная реализация стека
    def __init__(self):
        self.stack = []
#Пустой стек
    def is_empty(self):
        return len(self.stack) == 0
#Добавить в стек новое значение
    def push(self, value):
        self.stack.append(value)
#Выбрать значение
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]
#Изъять с головы стека значение.
        #Бросить ошибку, если стек пуст
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
#Вернуть текущую длину стека
    def size(self):
        return len(self.stack)

    def print(self):
        print(self.stack)


class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def add_first(self, value):
        self.deque.insert(0, value)

    def add_last(self, value):
        self.deque.append(value)

    def pop_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque.pop(0)

    def pop_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque.pop()

    def peek_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque[0]

    def peek_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque[-1]

    def size(self):
        return len(self.deque)

    def print(self):
        print(self.deque)



#ЗАДАНИЕ 1
#Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №1---------------------")
print("-------------------------------------------------")

with open('books.txt', 'r', encoding='utf-8') as f:
    d1 = Deque()
    d2 = Deque()

    for book in f:
        d1.add_last(book)

    while not d1.is_empty():
        x = d1.pop_last()
        while not d2.is_empty() and d2.peek_last() < x:
            d1.add_first(d2.pop_last())
        d2.add_last(x)

    while not d2.is_empty():
        print(d2.pop_last())




#ЗАДАНИЕ 2
#Дек содержит последовательность символов для шифровки сообщений. Дан текстовый файл, содержащий зашифрованное сообщение.
#Пользуясь деком, расшифровать текст. Известно, что при шифровке каждый символ сообщения заменялся следующим за ним в деке по часовой стрелке через один.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №2---------------------")
print("-------------------------------------------------")

alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

keyRing = Deque()
for letter in alphabet:
    keyRing.add_last(letter)

def decode_char(c):
    for i in range(keyRing.size()):
        x = keyRing.pop_last()
        if x == c:
            keyRing.add_first(x)
            val = keyRing.pop_last()
            keyRing.add_first(val)
            return val
        keyRing.add_first(x)

text = 'рсйгёу нйс'



decoded = ''
for letter in text:
    if decoded_letter := decode_char(letter):
        decoded += decoded_letter
    else:
        decoded += letter
print(decoded)



#ЗАДАНИЕ 3
#Даны три стержня и n дисков различного размера. Диски можно надевать на стержни, образуя из них башни.
#Перенести n дисков со стержня А на стержень С, сохранив их первоначальный порядок. При переносе дисков необходимо соблюдать следующие правила:

# -на каждом шаге со стержня на стержень переносить только один диск;
# -диск нельзя помещать на диск меньшего размера;
# -для промежуточного хранения можно использовать стержень В. Реализовать алгоритм, используя три стека вместо стержней А, В, С. Информация о дисках хранится в исходном файле.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №3---------------------")
print("-------------------------------------------------")

A = Stack()
B = Stack()
C = Stack()

disks = 10

for i in range(disks, 0, -1):
    A.push(i)


def move(a, b):
    if a.is_empty() and not b.is_empty():
        a.push(b.pop())
    elif not a.is_empty() and b.is_empty():
        b.push(a.pop())
    elif a.peek() > b.peek():
        a.push(b.pop())
    else:
        b.push(a.pop())


if disks % 2 == 0:
    while C.size() != disks:
        move(A, B)
        move(A, C)
        move(B, C)
else:
    while C.size() != disks:
        move(A, C)
        move(A, B)
        move(B, C)

while not C.is_empty():
    print(C.pop())



#ЗАДАНИЕ 4
#Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс круглых скобок в тексте, используя стек.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №4---------------------")
print("-------------------------------------------------")

def check_brackets(string):
    bracket_stack = Stack()
    for i in string:
        if i == '(':
            bracket_stack.push(i)
        elif i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()

print(check_brackets('()())'))
print(check_brackets('(()())()()()()(()(()(())()))'))



#ЗАДАНИЕ 5
#Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс квадратных скобок в тексте, используя дек.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №5---------------------")
print("-------------------------------------------------")

def check_square_brackets(string):
    bracket_stack = Deque()
    for i in string:
        if i == '[':
            bracket_stack.add_last(i)
        elif i == ']':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop_last()
    return bracket_stack.is_empty()

print(check_square_brackets('[]'))
print(check_square_brackets('[[]]]'))


#ЗАДАНИЕ 6
#Дан файл из символов. Используя стек, за один просмотр файла напечатать сначала все цифры, затем все буквы, и,
#наконец, все остальные символы, сохраняя исходный порядок в каждой группе символов.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №6---------------------")
print("-------------------------------------------------")

text = '.си1,м/2/во3лы'

letters = Stack()
digits = Stack()
others = Stack()

for c in text:
    if c.isalpha():
        letters.push(c)
    elif c.isdigit():
        digits.push(c)
    else:
        others.push(c)

new_text = ''


while not others.is_empty():
    new_text += others.pop()

while not letters.is_empty():
    new_text += letters.pop()

while not digits.is_empty():
    new_text += digits.pop()
print(new_text[::-1])



#ЗАДАНИЕ 7
#Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа,
#затем все положительные числа, сохраняя исходный порядок в каждой группе.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №7---------------------")
print("-------------------------------------------------")

import random

numbers = [random.randint(-10, 10) for i in range(10)]
print(numbers)

deque = Deque()
for n in numbers:
    if n < 0:
        deque.add_first(n)
    else:
        deque.add_last(n)

while not deque.is_empty():
    x = deque.pop_first()
    if x < 0:
        deque.add_last(x)
    else:
        deque.add_first(x)
        break

while not deque.is_empty():
    x = deque.pop_last()
    if x < 0:
        print(x)
    else:
        deque.add_last(x)
        break

while not deque.is_empty():
    print(deque.pop_first())




#ЗАДАНИЕ 8
#Дан текстовый файл. Используя стек, сформировать новый текстовый файл, содержащий строки исходного файла,
#записанные в обратном порядке: первая строка становится последней, вторая – предпоследней и т.д.

print("-------------------------------------------------")
print("------------------ЗАДАНИЕ №8---------------------")
print("-------------------------------------------------")

with open('books.txt', 'r', encoding='utf-8') as books:
    stack = Stack()
    for book in books:
        book = book.strip()
        print(book)
        stack.push(book)
    print('-----------------------------')
    while not stack.is_empty():
        print(stack.pop())