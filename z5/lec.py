# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).


n = int(input('Введите номер четверти от 1 до 4: '))
if n == 1:
    print(f'Диапазон координат точек в первой четверти x > 0 и y > 0')
elif n == 2:
    print(f'Диапазон координат точек во второй четверти x < 0 и y > 0')
elif n == 3:
    print(f'Диапазон координат точек в третьей четверти x < 0 и y < 0')
elif n == 4:
    print(f'Диапазон координат точек в четвертой четверти x > 0 и y < 0')
