words = []

with open("./ee.txt",'r') as file:
    content = file.readlines()

for line in content:
    line = line[:-1]
    words.append(line)

splitted_words = []

for item in words:
    splitted_words.append(item.split('-'))

# print(splitted_words)


def print_item_in_list(list):
    for item in list:
        print(item)

# print_item_in_list(splitted_words)

# print(word)
ryhme = words[:5]
places = words[6:7]
foods = words[7:8]
home = words[8:9]
office = words[9:10]
library = words[10:11]
art = words[11:12]
science = words[12:13]
sport = words[13:14]



def split_my_array_over(arr,splitter):
    res = []
    for item in arr:
        con = item.split(splitter)
        for sp in con:
            res.append(sp)
    return res

def tolowercase(arr):
    res = []
    for item in arr:
        res.append(str.lower(item))
    return res

s_ryhme = split_my_array_over(ryhme,'-')
s_food = split_my_array_over(foods,'-')
s_home = split_my_array_over(home,'-')
s_office = split_my_array_over(office,'-')
s_place = split_my_array_over(places,'-')
s_library = split_my_array_over(library,'-')
s_art = split_my_array_over(art,'-')
s_science = split_my_array_over(science,'-')
s_sport = split_my_array_over(sport,'-')
# print(tolowercase(s_sport))

def merge(arr1,arr2):
    res = arr1[0:len(arr1)]
    for item in arr2:
        res.append(item)
    return res

res = merge(s_art,s_food)
print(res)

def similarities(a,b):
    c = []
    for item1 in a:
        for item2 in b:
            if tolowercase(item1) == tolowercase(item2):
                c.append(item1)

    return c

sim = similarities(s_library,s_office)
print(sim)

def diff(A,B):
    c = similarities(A,B)
    for i in range(0,len(c)):
        A.remove(c[i])
    return A

dif = diff(s_library,s_office)
print(dif)
        
