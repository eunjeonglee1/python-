# 튜플 생성
t=1, #값 하나만 적을때에는 ','를 꼭 붙여야됨, 안붙이면 정수로 인식
print(t,type(t))

t=(1,)
print(t,type(t))

t1=(1,2,3)
print(t1,type(t1))

t2 = 4,5,6
print(t2,type(t2))

t3 = t1,(7,8,9)
print(t3)

t4=[1,2],[3,4,5]
print(t4)

t5=tuple([1,2,3]) #인수로는 생성 불가
print(t5)

t6 = tuple('hello') #문자 하나하나를 튜플로 만듬
print(t6)

#리스트를 튜블로 변환
list1 = [1,2,3]
t7 = tuple(list1)
print(list1,t7)

#튜플을 리스트로 변환
list2=list(t4)
print(list2)