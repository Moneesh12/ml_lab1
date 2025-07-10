import math,random

list1 = [random.randint(1,10) for _ in range(25)]
print(list1)
sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]
    mean = sum/25

print("mean:",mean)

maxcount = 0

for i in list1:
    count1 = list1.count(i)

    if count1>maxcount:
        maxcount = count1
        max_num = i

print("mode:",max_num)

list2 = sorted(list1)
n = len(list2)

if n%2==0:
    median = (list2[n//2-1] + list2[n//2])/2
else:
    median = list2[n//2]

print("median:",median)
