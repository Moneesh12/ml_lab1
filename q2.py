#for finding the range of a list
def find_range(num):
    if len(num)<3:
        return "Range determination is not possible"#if number of elements less than 3 then print this
    else:
        r = max(num) - min(num)#we are finding the maximum element of the list and subtracting with minimum to get the range
    return r

l = find_range([0,4,6,7,8,12])
print(l)
