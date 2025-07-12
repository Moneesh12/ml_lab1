a = [2,7,4,1,3,6]
count = 0#initially the number of pair count is 0

#goes through the list to find the pair with sum = 10
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == 10:
            count = count + 1
            print("the pairs:",a[i],a[j])
            
    
print("the number of pairs are:",count)

