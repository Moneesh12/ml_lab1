def find_range(num):
    if len(num)<3:
        return "Range determination is not possible"
    else:
        r = max(num) - min(num)
    return r

l = find_range([0,4,6,7,8,12])
print(l)