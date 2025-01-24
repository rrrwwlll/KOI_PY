raindow=['','빨','주','노','초','파','남','보','검']
#내가 좋아하는 색은 리스트의 몇번째 요소이고,'무슨색이야 첫번째 줄 출력
#검정색 삭제한 리스트 new_raindow 리스트로 새롭게 선언
#새럽게 선언한 new_raindow 리스트의 마지막 값 흰색 추가
print('내가 좋아하는 색은',raindow.index('파'),'번째이고,\n'
      '내가 좋아하는 색은',raindow[5],'야')
new_raindow=raindow
raindow.remove('검')
new_raindow=raindow
new_raindow.insert(7,'흰')
print(new_raindow)