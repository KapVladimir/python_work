"""4) Пользователь вводит целое положительное число. Найдите самую большую
цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

my_var = int(input("Введите число: "))
my_max = my_var % 10
my_var = my_var // 10
while my_var > 0:
    if my_var % 10 > my_max:
        my_max = my_var % 10
    my_var = my_var // 10
print(f"Максимальное число: {my_max}")
