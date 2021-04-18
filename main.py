# С клавиатуры вводится натуральное число.
# Найти его наибольшую цифру.

# Входные данные:
# 1. Натуральное число (вводится с клавиатуры)

# Основная цель:
# 1. Найти наибольшую цифру числа

# Побочные цели:
# 1. Ввод числа
# 2. Проверка числа на соответствия
# 3. Алгоритм нахожения большего числа:
#   а) раздел числа на цифры
#   б) запись цифр в список
#   в) сортировка списка
# 4. Вывод числа

while True:
    try:
        number=int(input('Введите число: '))
        if number>=0:
            break
        else:
            print('Число не является натуральным')
    except ValueError:
        print('Число не является числом')
numberlist=[]
for i in str(number):
    numberlist.append(i)
for i in range(len(numberlist)):
    for j in range(len(numberlist)-1):
        if int(numberlist[i])>int(numberlist[j]):
            buf = numberlist[i]
            numberlist[i]=numberlist[j]
            numberlist[j]=buf

print('Самой большой цифрой в числе',number,'является',numberlist[0])