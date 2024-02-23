#1.
#1) 정답 : [0,1,2],[0,1] , [4,3,2,1,0]
a=[0,1,2,3,4]
print(a[:3],a[:-3])
print(a[::-1])

#2) 정답 : [["egg", "salad", "bread"],["lamb","chicken"],["apple"]]
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
print(f'john : {john}')
del john[2]
print(f'john[2] : {john}')
john.extend([order[2][0:1]])
print(john)

#3) 정답 : [1,2,3,4], None
list_a = [3, 2, 1, 4]
print(list_a)
list_b = list_a.sort()  #메서드는 반환값을 하지 않기때문에 'None'으로 나옴

print(list_b)
print(list_a, list_b)


#4) 정답 : None
a = [5, 7, 3]
b = [3, 9, 1]
c = a + b
print(c)
c = c.sort()
print(c)

#5) 정답 : [1, 2, 3, 4, 1, 2, 3, 4]
num = [1, 2, 3, 4]
print(num * 2)


#6) 정답 : False,6
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))


#7) 정답 : ["Korea", "Japan", "China",["Seoul", [2, 3], "Beijing"]]
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)


#8) 정답 : ['orange', 'strawberry', 'melon'],['banana','orange']
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])


#9) 정답 : ['Hankook','is','academic','located','South Korea']
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', \
'in', 'South Korea']
print(len(list_a))
list_b=[ ]
for i in range(len(list_a)):
    if i % 2 != 1:
        print(i)
        list_b.append(list_a[i])
print(list_b)

#2. 정답 :  3번
admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year))


#3. 정답 : week1+week2
week1 = ["Mon", "Tue", "Wed"]
week2 = ["Thu", "Fri", "Sat", "Sun"]
week3 = week1+week2
print(week3[:len(week2) + 2])
'''
'''
#4.
#1) 정답 :
name_list = []

for i in range(3):
    name=input('회원 입력 : ')
    name_list.append(name)
    # name_list.append(input('회원입력:')) 로도 작성 가능
print(f'회원 명단 : {name_list}')


#2) 정답 :
total = 0
scores = []
num=int(input("학생 수 입력 : "))
for i in range(num):
    score=int(input(f'학생{i+1} 점수 입력 : '))
    scores.append(score)

cnt=0
for score in scores:
    total+=score
    if score >= 80:
         cnt+=1

avg = total / len(scores)

print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')
print(f'80점 이상 학생 : {cnt}명')


#3) 정답
name_list=[]
while True:
    name=input('상품 등록 (엔터키 누르면 종료) : ')
    if name == '':
        break
    else:
        name_list.append(name)
print(f'등록된 상품 : {name_list}')

#4) 정답 :
total = 0
scores = []

num=int(input("학생 수 입력 : "))
for i in range(num):
    score=int(input(f'학생{i+1} 점수 입력 : '))
    scores.append(score)
    scores.sort(reverse=True)

cnt=0
for score in scores:
    total+=score
    if score >= 80:
         cnt+=1

avg = total / len(scores)

print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')
print(f'80점 이상 학생 : {cnt}명')
print(f'점수 내림차순 정렬 : {scores}')


#5) 정답 :
n=['개과천선','구사일생','군계일학','무용지물','동고동락','유비무한','입신양명','괄목상대','막역지우','고장난명']
n2=['잘못을 고치고 옳은 길에 들어섬','죽일 고비를 여러번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람','아무짝에나 쓸모없는것', '\
고통과 즐거움을 함께한다','미리 준비해두면 근심 걱정이 없다','사회적으로 인정받고 출세하여 이름을 세상에 드날림','\
다른 사람의 학식이나 업적이 크게 진보한 것을 말함','생사를 같이 할 수 있는 친밀한 벗', '상대 없이 혼자서는 어떤 일을 이룰 수 없다']

for name, meaning in zip(n, n2):
    print(name,':',meaning)

print('\n')
print('사자성어 맞추기 게임을 시작합니다')
print('-----------------------------')
y=list(zip(n,n2))
from random import randint
while True:
    y=randint(0,len(n2)-1)
    q=n2[y]
    a=n[y]
    print(q)
    x=input('이 말의 사자성어는? : ')
    if x==a:
        print(f'\n맞습니다.. 게임을 종료합니다.\n')
        break
    else:
        print(f'\n틀렸습니다...다시 도전 ! \n')

# n3=len(n2)
# while True:
#     rnd=randint(0,n3-1)
#     print(n2[rnd])
#     in_idiom=input('이 말의 사자성어는? :')

