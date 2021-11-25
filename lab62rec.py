# 6.2.py
# Хімчинський Орест
# Лабораторна робота No 6.2
# Пошук елементів одновимірного масиву
# Варіант 15
import random


# створення масиву
def create(size, p=[]):
    if size <= 0:
        return p
    else:

        p.append(int(random.random() * 10))
        size -= 1
        return create(size)


# визначення найменшого та найбільшого значення із масиву
def high_and_low_number(p, list_low_and_high=[]):
    if len(list_low_and_high) == 4:
        return list_low_and_high

    else:
        p = sorted(p)
        low = p[0]
        high = p[len(p) - 1]
        list_low_and_high.append(low)
        list_low_and_high.append(high)
        list_low_and_high.append(0)
        list_low_and_high.append(0)
        return high_and_low_number(p, list_low_and_high)


# розрахунки
def calculation(list_low_and_high, res=0):
    if len(list_low_and_high) == 2:
        return res
    else:
        number = list_low_and_high[0]
        res += number
        list_low_and_high = list_low_and_high[1:]
        return calculation(list_low_and_high, res)


# головна функція
def main():
    p = create(10)
    print('Масив', p)
    list_low_and_high = high_and_low_number(p)
    summ = calculation(list_low_and_high)
    print('Сума найбільшого та найменшого значення масиву: ', summ)


main()
