import  random
'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
# manettes = int(input("Введите сколько лежит на столе монеток  "))
# eagle = random.randint(1,manettes)
# up_tails = manettes - eagle
# print(f"manettes - {manettes}, eagle - {eagle}, tails - {up_tails}")
#
# if eagle<up_tails:
#     print(f"переварачиваем eagle - {eagle}")
# else :
#     print(f"переварачиваем tails - {up_tails}")

'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
 Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
 а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и 
 их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
# number1 = random.randint(1, 100)
# number2 = random.randint(1, 100)
# flag = False
# S = number1 + number2
# P = number1 * number2
# print(f"num1 = {number1}, num2 = {number2}, S = {S}, P = {P}")
# for i in range(S):
#     for j in range(S):
#         if i + j == S:
#             if i * j == P:
#                 print(f"i = {i}, j= {j}")
#                 flag = True
#         if flag:
#             break

'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
# N = random.randint(0, 100)
# s = 1
# if N == 0:
#     print(f"2 в {N} степени равняется {s}")
# else:
#     print (f"{N} \n {s}", end = ', ')
#     for i in range(N):
#         for j in range(i):
#             s *= 2
#             if s <= N:
#                 print(s, end =', ' )


