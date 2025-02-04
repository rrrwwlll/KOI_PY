num = int(int(input()))
result = str(num)


if num >= 1000:
    result = str(num//1000) + 'K'
elif num >= 0:
    pass

if num >= 100000:
    result = str(num//100000) + 'M'
elif num >= 0:
    pass


print(result)