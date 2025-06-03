# there are two types of iteration in programming languages

def cube(a) :
    return a**3

# 1th:for loop which iterates at a certain number of times
for i in range(3,15):
    print(cube(i))

# 2nd: while loops which iterates until its condition is sattisfied

a = 1

while(cube(a)<1000):
    print(cube(a))
    a+=1 

