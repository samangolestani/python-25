def myRecursiveFunc(a):
    if(a<1):
        return 0
    return myRecursiveFunc(a/2 -1) + myRecursiveFunc(a/2) +1
print(myRecursiveFunc(1000))