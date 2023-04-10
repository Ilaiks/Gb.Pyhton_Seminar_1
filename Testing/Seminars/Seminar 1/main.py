"""
a = 5 
b = 5.89
c = 'hello'

print(a, ' - ', b, ' - ',c)
"""

"""
a = 5 
b = 5.89
c = 'hello'

print(f"{a} - {b} - {c}")
"""

"""
a = 5 
b = 5.89
c = 'hello'

print("{} - {} - {}".format(a,b,c))
"""

"""
print('Введите первую строку')
a = input()
print(a)
"""

"""
print('Введите первое число: ')
a = input()
print(a)
"""

"""
print('Введите первое число: ')
a = input()

b = input('Введите второе число: ')
"""

"""
print('Введите первое число: ')
a = input()
b = input('Введите второе число: ')

print(a, ' + ', b, ' = ', a+b)
"""

"""
c = 5.89
print(c)
print(type(c))
c = int(c)
print(c)
print(type(c))
"""

"""
c = 5.89
print(c)
print(type(c))
c = str(c)
print(c + '89')
print(type(c))
"""

"""
c = 1
print(c)
print(type(c))
c = bool(c)
print(c)
print(type(c))
"""


"""
print('Введите первое число: ')
a = int (input())
b = int (input('Введите второе число: '))

print(a, ' + ', b, ' = ', a+b)
"""


"""
a = 5.89956
b = 6.556551
print(round(a*b, 3))
"""

"""
iter = 2
iter += 3 #iter = iter + 3
iter -= 4 #iter = iter - 4
iter *= 5 #iter = iter * 5
iter /= 5 #iter = iter / 5
iter //= 5 #iter = iter // 5
iter %= 5 #iter = iter % 5
iter **= 5 #iter = iter ** 5
"""


# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a==b)
# a = 1 < 3 < 5 < 10
# print(a)


"""
username = input('введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)            
"""


"""
i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит')
print(i)
"""


"""
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не може превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1     
"""


"""
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не може превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1     
    """


"""
a = 'qwerty'

for i in a:
    print(i)
"""


"""
line = ""
for i in range (5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
"""



text = 'Сьешь ещё этих мягких французких булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё','ЕЩЁ'))