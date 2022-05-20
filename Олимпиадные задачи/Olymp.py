#coding: utf-8
from collections import defaultdict


def task1(sides):
    result = 0
    sides_sorted = sorted(sides, reverse=True)
    for i in range(len(sides_sorted) - 2):
        a = sides_sorted[i]
        b = sides_sorted[i+1]
        c = sides_sorted[i+2]
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
    return result


def task2(nums):
    nums_str = []
    result = ''
    for num in nums:
        nums_str.append(str(num))
    nums_str_sorted = sorted(nums_str, reverse=True)
    for i in range(len(nums_str_sorted) - 1):
        if nums_str_sorted[i]+nums_str_sorted[i+1] < nums_str_sorted[i+1]+nums_str_sorted[i]:
            nums_str_sorted[i], nums_str_sorted[i+1] = nums_str_sorted[i+1], nums_str_sorted[i]
    for num in nums_str_sorted:
        result += num
    return(result)


def task3(mat):
    diagonal = defaultdict(list)
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            diagonal[row-col].append(mat[row][col])
    for i in diagonal:
        diagonal[i].sort()
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            mat[row][col] = diagonal[row-col].pop(0)
    return mat


def main():
    print("Пример 1: ",task1([2, 1, 2, 3]))
    print("Пример 2: ",task2([10,2]))
    a = task3([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
    for i in a:
        print(i)

main()