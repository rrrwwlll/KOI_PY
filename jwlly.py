jelly=100
student=90

while student:
    print("맛있는 젤리 당첨")
    jelly -= 1
    print("젤리가 %d 개 남았네요ㅠㅠ"%jelly)

    if jelly == 0:
        print("젤리가 없어요.")
        break
