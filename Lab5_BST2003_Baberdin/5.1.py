import time
from turtle import *

cnt = 0


def gilbert(level, angle, step):
    global cnt
    speed(0)

    if level == 0:
        cnt += 1
        return

    right(angle)

    gilbert(level - 1, -angle, step)

    forward(step)
    left(angle)

    gilbert(level - 1, angle, step)

    forward(step)

    gilbert(level - 1, angle, step)

    left(angle)
    forward(step)

    gilbert(level - 1, -angle, step)
    right(angle)


def main():
    level = int(input("Введите глубину: "))
    size = 100
    penup()
    goto(-size / 2.0, size / 2.0)
    pendown()

    # For positioning turtle
    prev_t = time.time()
    gilbert(level, 90, size / (2 ** level - 1))
    cur_t = time.time() - prev_t
    print(f"Глубина рекурсии: {cnt}\nВремя выполнения: {cur_t}")
    done()


main()