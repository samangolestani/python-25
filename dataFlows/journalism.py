# in order to demontrate the flow of codes to be excuted we use if statements

a = input("please enter your nationality:")

b = str.lower(a)

temp = "Your country of birth is:"
res = ''
if(b =="iranian"):
    res = temp + 'Iran'
elif (b== "ukranian"):
    res = temp + 'Ukrain'
elif( b == 'german'):
    res = temp + 'Germany'
else:
    res = 'Your nationality is unknown'
print(res)



#nested if statement

a = 26
b = 28

if(a>25):
    if(b<32):
        print("Hi")
    else:
        print("Hey")
else:
    if(b<5):
        print("bye")
    else:
        print("goodbye")


