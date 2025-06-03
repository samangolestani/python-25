import math

myLam = lambda x : x*2

polynomial = lambda X : X**2 +1


# for i in range(-1000,1000):
#     print(polynomial(i))


def n_th_member_subsets(a):
    return lambda n: math.floor(math.factorial(n)/(math.factorial(a)*math.factorial(n-a)))

n = 20

two_member_subset = n_th_member_subsets(2)
three_member_subset = n_th_member_subsets(3)
four_member_subset = n_th_member_subsets(4)
print(two_member_subset(20))
print(three_member_subset(20))
print(four_member_subset(20))


I  = lambda x: math.floor(x)
F = lambda x: x- I(x)

res = 0

map = lambda x , y: x/y
for i in range(1,1000):
    if F(map(i,1000)) + F(1/map(i,1000)) == 1:
        res = i

print(i)