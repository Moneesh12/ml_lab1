#for finding mean,median and mode

#mean
import random

list1 = [random.randint(1,10) for _ in range(25)]#this generates a list from 1 to 10 with 25 elements
print(list1)
sum = 0#used for finding sum of a list
for i in range(len(list1)):
    #we are finding the sum of the array and dividing by the number of elements to get mean
    sum = sum + list1[i]
    mean = sum/25

print("mean:",mean)

#Mode

maxcount = 0#we are initialising this to find the element that has repeated the most in the list

for i in list1:
    count1 = list1.count(i)#we are checking for each number the number of times it has repeated

    if count1>maxcount:
        maxcount = count1
        max_num = i

print("mode:",max_num)

#Median

list2 = sorted(list1)
n = len(list2)

if n%2==0:
    median = (list2[n//2-1] + list2[n//2])/2#we are using the median formula when number of elements are even
else:
    median = list2[n//2]#we are using the median formula when number of elements are odd

print("median:",median)

