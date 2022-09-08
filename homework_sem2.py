# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# N = input("Введите число ")
# sum = sum(int(i) for i in N if i.isdigit())
# print(sum)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import math
n = int(input("Введите число: "))
data = list(math.factorial(i) for i in range(1,n+1))
print(data)



# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# n = int(input("Введите число "))
# data = list((1+1/i)**i for i in range(1,n+1))
# print(f'Сумма для числа {n} = {round(sum(data), 2)}')
    


# Реализуйте алгоритм перемешивания списка.
# import random
# data = [1, 2, 3, 4]
# random.shuffle(data)
# print(data)
  




# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# from random import randint

# N = int(input("Введите число: "))
# numbers = []

# for i in range(N):
#     numbers.append(randint(-N, N))
# print(f"Заданный список: {numbers}")

# with open("a.txt", 'r') as f:
#     pozition = list(map(int, f.readlines()))
# print(f"Список позиций из файла: {pozition}")        

# composition = 1
# for i in pozition:
#     composition *= numbers[i]
# print(f"Произведение элементов: {composition}")








