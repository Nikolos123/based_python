# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. В
# торой — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(a, y):
    print(a ** -y)


my_func(5, -7)


def my_fucn2(a, y):
    i = -y
    c = 0
    while i != 1:
        c = c * a if c != 0 else a * a
        i -= 1
    print(c)


my_fucn2(5, -7)