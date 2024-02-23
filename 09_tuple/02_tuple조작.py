# 튜플 조작

#1. 인덱싱
t=1,2,3,4,5,6,7,8
print(t[0])

#2. 슬라이싱
print(t[:])
print(t[3:])
print(t[::-1])

#3. +연산
t1=(4,5,6)
t2=10,11,12
t3=t1+t2
print(t3)

#4. *연산
print(t1*3)

#5. 멤버연산 : in/ not in
t5='hello','hi','hoho'
print('hi' in t5 )

#6. 길이:len()
t4=t1*3
print(len(t4))

#데이터값 변경 불가
#t5[0]='hahaha'
#TypeError: 'tuple' object does not support item assignment 발생

#데이터값 삭제 불가
#del(t5[0])
#TypeError: 'tuple' object doesn't support item deletion
#튜플안에 있는 요소를 바꾸고 싶을때에는 list로 변경한다음 다시 tuplu로 변경

#튜플 자체를 제거하는 것은 가능
del(t5)

#7. 튜플 요소 검색 : index(), count()
t6=tuple('hello hi how are you!')
print(t6)
print(t6.index('o'))
print(t6.count('h'))