day=['13','14','15']
day=[i+'일' for i in day]
print(day)



month=['1','2','3','4','5','6','7','8','9','10','11','12']
#month 리스트 값에 '월'을 추가해서 month 리스트 만들기
month=[a+'월' for a in month]
a=0
while a < len(month):
    print(month)
    a += 1
    if a == 3:
        break

for i in range (3,100) :
    for j in range(2,100) :
        for q in range(1,100) :
         print(i*j*q)