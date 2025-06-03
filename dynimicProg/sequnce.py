arr_f = [2]
def F(n,a,q):
    if n==1:
        return a
    return q*F(n-1,a,q)
for i in range(1,1000):
    arr_f.append(1.01*arr_f[i-1])
S = [0]

for i in  range(1,1000):
    S.append(arr_f[i]+S[i-1])

print(S[999])