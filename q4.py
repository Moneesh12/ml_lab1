word = "hippopatamus"

l = list(word)

max_ch = ''
maxcount = 0

for i in range(len(l)):
    a = l[i]
    count1 = l.count(a)
    
    if count1>maxcount:
        maxcount = count1
        max_ch = a

print("most repeated letter:",max_ch)
print("count = ",maxcount)