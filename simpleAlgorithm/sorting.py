# there are some bulit-in sorting algorithm to use

a = [5,4,-1,0,6,9,25,-2]
a.sort()
print(a)

# you can always implement your own algorithm of choice
a = [1,8,3]
def mySort(a):
    res = []
    time = len(a)
    for i in range(0,time):
        m = min(a)
        res.append(m) 
        a.remove(m)
    return res

print(mySort(a))

