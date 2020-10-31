#Abel Goshu
#1675552

l = input()
l = l.split(" ")
d = {}
for each in l:
    if each in d:
        d[each] = d[each] + 1
    else:
        d[each] = 1
for each in l:
    print(each, d[each])