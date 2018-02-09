# Поиски делителей числа

#ввод числа
from math import sqrt
n = int(input("Введите число? "))

# поиски делителей
Ans = []
a = 1
b = sqrt(n)

while a < b:
    if n % a == 0:
        Ans.append(a)
        if (a * a != n):
             Ans.append(int(n / a))
    a += 1

#выводе делителей числа
print("Делители числа:", n)
print(sorted(Ans))
