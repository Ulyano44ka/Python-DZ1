# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,10
# - A (7,-5); B (1,-1) -> 7,21

import math

xa=int(input('Введите xa : '))
ya=int(input('Введите ya : '))
xb=int(input('Введите xb : '))
yb=int(input('Введите yb : '))
AB=round(math.sqrt((xb-xa)**2+(yb-ya)**2),2)
print(AB)




