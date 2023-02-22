import random

list = [random.randint(0, 100) for _ in range(15)]

print(list)
number = int(input('Введите искомое число: '))

if list.count(number) == 0:
    nearest = list[0]
    for num in list:
        if abs(number - num) < abs(number - nearest):
            nearest = num
    print(f'Ближайщее число к {number} это {nearest}')
else:
    print(f'Число {number} встречается {list.count(number)} раз')
