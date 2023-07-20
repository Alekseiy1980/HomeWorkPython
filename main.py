import  random
'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
# print('Случайное целое число:', end=' ')
# print(random.randint(0, 10))

manettes = int(input("Введите сколько лежит на столе монеток  "))
eagle = random.randint(1,manettes)
up_tails = manettes - eagle
print(f"manettes - {manettes}, eagle - {eagle}, tails - {up_tails}")

if eagle<up_tails:
    print(f"переварачиваем eagle - {eagle}")
else :
    print(f"переварачиваем tails - {up_tails}")
