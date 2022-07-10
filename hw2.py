#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('Введите число n:')
n=int(input())
import math
f = math.factorial(n)
def fact(n):
    f = 1
    for i in range(n):
        f *= i+1
        print(f)
    return f 
f = fact(n) 