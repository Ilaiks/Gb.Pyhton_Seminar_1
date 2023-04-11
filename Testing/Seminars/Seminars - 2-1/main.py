# По данному целому неотрицательному n вычислите значение n!.
#
#
#
#

number = int(input('Введите число: '))

value = factorial = 1

while value <= number:
    factorial *= value
    value += 1

print(f'Факториал {number} = {factorial}')