#5. НЕОБЯЗАТЕЛЬНАЯ Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input())
list = []
for i in range(n + 1):
    if i == 0:
        list.append(0)
    elif i == 1 or i == 2:
        list.append(1)
    else:
        list.append(list[-1] + list[-2])
list2 = []
for i in range (1, n + 1):
    if i % 2 == 0:
        list2.insert(0, list[i] * (-1))
    else:
        list2.insert(0, list[i])
i = 0
for el in list2:
    list.insert(i, el)   
    i += 1  
print(list) 
