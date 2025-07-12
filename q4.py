#for finding the most repeated letter in a word
word = "hippopatamus"

l = list(word)#converts the word into a list of letters

max_ch = ''
maxcount = 0

for i in range(len(l)):
    a = l[i]
    count1 = l.count(a)#counts how many times the letter repeated


#used for checking if the current count is more than the current maximum    
    if count1>maxcount:
        maxcount = count1
        max_ch = a

print("most repeated letter:",max_ch)
print("count = ",maxcount)
