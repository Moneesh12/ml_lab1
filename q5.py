import math,random

list1 = [random.randint(1,10) for _ in range(25)]
sum = 0
for i in range(len(list1)):
    sum = sum + i
    mean = sum/25

print(mean)
