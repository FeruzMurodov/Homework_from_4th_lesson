# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

def MakeList(n):
    list = []
    for i in range(n) :
        list.append(int(input("Введите число: ")))
    return list

def UnitLists(list1, list2):
    result = []
    for i in list1 :
        for j in list2 :
            if i == j :
                result.append(i)
    return result

def SetToList(set):
    list = []
    for item in set:
        list.append(item)
    return list

def SortList(list):
    result = []
    while len(list) > 0 :
        min = list[0]
        minIndex = 0        
        for i in range(len(list)) :
            if list[i] < min :
                min = list[i]
                minIndex = i
        result.append(list.pop(minIndex))
    return result


n = int(input("Введите количество элементов первого множества: "))
list1 = MakeList(n)
m = int(input("Введите количество элементов второго множества: "))
list2 = MakeList(m)
print(list1)
print(list2)
finalList = SortList(SetToList(set(UnitLists(list1, list2))))
print(finalList)