def applyNumbers(op, a,b):
    if(op == '+'):
        return a+b
    elif (op== '-'):
        return a-b
    elif (op == '*'):
        return a*b
    else:
        return a/b;
#Numeric Operatios
print(applyNumbers('/', 91 ,32))
print(applyNumbers('+', 91 ,32))


#String operation
a = 'hello'
b = 'World'
print(a+ " " +b)
print(a.capitalize())
print(a.index('l'))
print(a.split('l'))
print(a.isupper())

#Boolean operation
a = True
b = False
print(a and b)
print(a or b)
print(a and not b)

#List operations
a = ['blue' , 'red' , 'green']
for item in a:
    if(item ==  'blue'):
        print(item +' :brown')
    elif(item == 'red'):
        print(item + ' :yellow')
    else:
        print(item +' :cyan')

a.append('white')
a.remove('green')
print(a)
b = ['a','b','z']

c = []
def conCat(a, b):
    for item in a:
        c.append(item)

    for item in b:
        c.append(item)
conCat(a,b)
print(c)

#Set operation
a = {'green', 'blue', 'yellow' , 'orange' , 22, 323, 142,700}
a.add('brown')

b = a.copy()
b.remove(22)
c = a.difference(b)

print(c)

#Dictionary Operations
# date1 = {
#     "year" : 1999,
#     "month" : "April",
#     "day" : 'Wednesday',
#     "hour" : 2,
#     "isDaylight" : True
# }
# date2 = {
#     "year" : 2006,
#     "month" : "March",
#     "day" : 'Sunday',
#     "hour" : 8,
#     "isDaylight" : False
# }

myDates = { "date1" : {
    "year" : 1999,
    "month" : "April",
    "day" : 'Wednesday',
    "hour" : 2,
    "isDaylight" : True
} ,
    "date2" : {
    "year" : 2006,
    "month" : "March",
    "day" : 'Sunday',
    "hour" : 8,
    "isDaylight" : False     
    }
}
a = myDates.keys()
print(a)
print(myDates['date1']["isDaylight"])
