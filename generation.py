i = int(input("당신은 몇년도에 태어났나요?"))
if 0 <= i <= 1924:
    print("the Greatest Generation")
elif 1925 <= i <= 1945:
    print("the Silent Generation")
elif 1946 <= i <= 1964:
    print("Baby Boomer")
elif 1965 <= i <= 1980:
    print("Generation X")
elif 1981 <= i <= 1996:
    print("Millennial")
elif 1997 <= i <= 2010:
    print("Generation Z")
elif 2011 <= i <= 10000:
    print("Alpha")
else:
    for j in range(1,10001):
        print("당신은 사람이 아니야!")
