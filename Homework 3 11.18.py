#Abel Goshu
#1675552

numbers = input().split()
result = []
for num in numbers:
    num = int(num)
    if num >= 0:
        result.append(num)
result.sort()
for num in result:
    print(num, end=' ')