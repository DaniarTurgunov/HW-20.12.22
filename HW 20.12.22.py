# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3, 8]
my_list1 = []
sum = 0
for i in range (len(my_list)):
    if i % 2: 
        z = my_list[i]
        my_list1.append(z)
        sum += z
x = ', '.join(map(str, my_list1))
print(f'{my_list} -> на нечётных позициях элементы {x} , ответ: {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = []
my_list1 = []
a = int(input('Введите кол-во чисел: '))
for i in range(a):
    my_list.append(int(input('Введите число: ')))
for i in range(a):
    if a % 2 == 0:
        x = a // 2
    else:
        x = a // 2 + 1
for i in range(x):
    z = my_list[i] * my_list[a-i-1]
    my_list1.append(z)
print(f'{my_list} => {my_list1}')

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = []
my_list1 = []
a = int(input('Введите кол-во чисел: '))
for i in range(a):
    my_list.append(float(input('Введите числа: ')))
for i in my_list:
    if i != int(i):
        z = i % 1
        z = round(z,2)
        my_list1.append(z)
ma = max(my_list1)
mi = min(my_list1)
print(f'{my_list} => {ma - mi}')
        
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите число: '))
n1 = n
my_list = []
while n1 > 0:
    z = n1 % 2
    n1 = n1 // 2
    my_list.append(z)
x = ''.join(map(str,reversed(my_list)))
print(f'{n} -> {x}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Введите число: '))
f1 = f2 = f4 = 1
f3 = 0
my_list = [f1, f2]
my_list1 = [f3, f4]
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    my_list.append(f2)
for i in range(2, n+1):
    f3, f4 = f4, f3 - f4
    my_list1.append(f4)
x = ', '.join(map(str,reversed(my_list1)))
z = ', '.join(map(str,my_list))
print(f' Для n = {n} список будет выглядеть так: {x}, {z}')
