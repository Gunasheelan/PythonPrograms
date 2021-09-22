from array import *
arr = array('i', [5,3,8,8,7,2,1,3,0,7])

first, second = 0, 0
for i in arr:
    if i > first:
        first = i
    if i > second and i is not first:
        second = i
        if second > first:
            first = second

print(first, second)
