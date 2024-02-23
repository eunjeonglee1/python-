# 1. 딕셔너리 생성
# 집합적 자료, 순서의미가 없음
# item=> 키(key):값(value)으로 구성되어있음 : {key1:value1, key2:value2, ...}
# {} 또는 dict()를 이용하여 생성
# key로 데이터 접근

d={}
d=dict()
print(d,type(d))

d2 = {1:'a',2:'b',3:'c'}
print(d2)

# key의 순서는 생성된 순서대로 구성
# key와 value는 사용자가 지정하는 것, 규정이 없음
# key는 숫자, 문자열 다 가능하나 유일하게 구별 되어야 함
# value는 중복 가능

# 2. 딕셔너리 요소 접근 : key를 사용
# 딕셔너리[키이름]

# key로 접근하여 값을 가져옴

print(d2[1]) #1은 인덱스가 아니라 key
#print(d2[0]) #0이라는 key가 없기때문에 KeyError가 발생

# 3. key를 이용하여 값을 변경

d2[1]=10
print(d2)

# 4. 딕셔너리 요소 추가 : 딕셔너리[키] = 값

d2[4] = 100
print(d2)

# 5. key는 유일한 값
# 동일한 key값을 추가하는 경우, 맨 마지막에 입력한 key의 값이 적용

d3 = {'a':1,'b':100,'c':'hello','b':1000}
print(d3)

# 6. 값(value)은 하나 또는 여러개의 집합적 자료를 가질 수 있음

d4 = {'name':['kim','hong','lee'],
      'score':[100,90,80],
      'gender':['F','M','M'],
      'phone':('123-234','123-9092','0110-123-1111')}
print(d4)
print(d4['name'])

# 7. 요소 삭제 : del(딕셔너리[키])

del(d4['gender'])
print(d4)