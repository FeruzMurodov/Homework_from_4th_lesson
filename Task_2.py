# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло a[i] ягод. В этом фермерском хозяйстве внедрена система 
# автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
# с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.

from random import randint

def FindMaxTrio(list) :
    maxSet = 0
    maxSetIndex = 1
    for i in range(1, len(list)-1) :
        if list[i] + list[i-1] + list[i+1] > maxSet :
            maxSet = list[i] + list[i-1] + list[i+1]
            maxSetIndex = i
    return maxSetIndex
        

a = int(input("Введите число кустов: "))
list = [randint(25, 125) for _ in range(a)]
print(list)
maxIndex = FindMaxTrio(list)
previousIndex = maxIndex - 1
nextIndex = maxIndex + 1
print(f"Максимальное число ягод за один заход: {list[previousIndex]} + {list[maxIndex]} + {list[nextIndex]} = {list[previousIndex] + list[maxIndex] + list[nextIndex]}")