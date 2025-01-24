jelly=100000000
student=1000000000

while student:
    print("이거 왜 봄?")
    jelly -= 1
    print("남은수:%d"%jelly)

    if jelly == 0:
        print("젤리가 없어요.")
        break
