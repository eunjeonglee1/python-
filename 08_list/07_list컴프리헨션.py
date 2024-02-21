# 리스트 컴프리헨션
#새로운 리스트 = [반복문장(변수) for 변수 in 반복범위(range()) (if 조건식)]

num_list = []
for num in range(1,6):
    num_list.append(num)
print(num_list)

num_list=[num for num in range(1,6)]
print(num_list)

num_list2=[num*2 for num in range(1,6)]
print(num_list2)

num_list2=[num*num for num in range(1,6)]
print(num_list2)

#문제. 1~20의 정수 중 짝수만으로 구성된 리스트 생성

num_list=[num for num in range(2,21,2)]
print(num_list)

num_list=[num for num in range(1,21) if num %2 ==0]
print(num_list)

list1=[]
for num in range(1,21):
    if num %2 ==0:
        list1.append(num)
print(list1)

#문제. 1~20 정수 중 3의 배수로 구성된 리스트
num_list=[num for num in range(1,21) if num %3 ==0]
print(num_list)

list1=[1,2,3,4,10,11,12]
num_list=[num for num in list1 if num %3 ==0]
print(num_list)

#참고. zip() 함수
foods = ['떡볶이','짜장면','라면','피자']
sides = ['단무지','김치','피클']

for food, side in zip(foods, sides):
    print(food,'--',side)
for item in zip(foods, sides): #같은 열에 있는것을 묶여서 보냄
    print(item)
print(type(zip(foods,sides)),zip(foods,sides))
print(list(zip(foods,sides)))

name = ['홍길동','강감찬','성춘향','방자']
sex = ['남','남','여','남']
addr= ['서울','한양','독도','부산']

print(list(zip(name,sex,addr)))
