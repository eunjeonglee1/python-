#1.정답 :
students=[{'name':'홍길동','korean':87,'math':98,'english':88,'science':95},
          {'name':'이몽룡','korean':92,'math':98,'english':96,'science':98},
          {'name':'성춘향','korean':76,'math':96,'english':94,'science':90},
          {'name':'변학도','korean':98,'math':92,'english':96,'science':92},
          {'name':'박지성','korean':95,'math':98,'english':98,'science':98},
          {'name':'류현진','korean':64,'math':88,'english':92,'science':92}]

print('{0:6s}{1:6s}{2}'.format('이름','총점','평균'))
for s in students:
    total=s['korean']+s['math']+s['english']+s['science']
    avg=total/4
    print(f'{s['name']:6s}{total:<7d}{avg}')




#2. 정답 :
n = {}
while True:
    x=input('\n''영어 단어 등록 (종료는 quit) : ')
    if x == 'quit':
        break
    elif x in n:
        print(f'{x}는 이미 등록된 단어 입니다.')
    else:
        y = input(f'{x}의 뜻입력 (종료는 quit) : ')
        n[x] = y
        print(n)
while True:
    x=input('\n''검색할 단어 입력 (종료는 quit) : ')
    if x == 'quit':
        print('\n''종료합니다.')
        break
    elif x in n:
        print(f'{x}의 뜻은 {n[x]}입니다 (종료는 quit)')
    else:
        print(f'{x}는 사전에 없는 단어 입니다.')


#강사님 답변
'''
n = {}
while True:
    x=input('\n''영어 단어 등록 (종료는 quit) : ')
    if x != 'quit':
        if x in n.keys():
            print(f'{x}는 이미 등록된 단어 입니다.')
        else:
            y = input(f'{x}의 뜻입력 (종료는 quit) : ')
            if y=='quit':
                break
            else:
                n[x] = y
    else:
        break
while True:
    x=input('\n''검색할 단어 입력 (종료는 quit) : ')
    if x != 'quit':
        meaning=n.get(x)
        if meaning in None:
            print(f'{x}는 사전에 없는 단어 입니다.')
        else:
            print(f'{x}의 뜻은 {n[x]}입니다 (종료는 quit)')
    else:
        print('\n''종료합니다.')
        break
'''

#3. 정답 : 3번 (유일한 값이 와야하는데 변경가능한 리스트가 key로 되어있기 때문에
a={}
a['name']='python'
a[('a',)]='python'
# a[[1]]='python'
a[250]='python'
print(a)

#4. 정답 : 듀플이라 값이 변경 불가능

#5. 정답 : t는 튜플이고 바인딩하는 데이터 1, 2, 3, 4 는 정수형
t=1,2,3,4
print(type(t))

#6-1) 정답 :
my_variable=()
print(my_variable,type(my_variable))

#6-2) 정답 :
x=(1,)
print(x,type(x))

#6-3) 정답 :
t=('a','b','c')  #t=tuple('abc')도 사용 가능
print(t,type(t))

#6-4) 정답 :
t1=t[1:]
t2=('A',)
t=t2+t1
print(t,type(t))

#6-5) 정답 :
interest=('삼성전자','LG전자','SK Hynix')
x=list(interest)
print(x,type(x))

#6-6) 정답 :
interest=['삼성전자','LG전자','SK Hynix']
x=tuple(interest)
print(x,type(x))

#6-7) 정답 :
x=(1,2,3)
y=(4,)
print(x+y)

#강사님 답변
'''
t=1,2,3
li = list(t)
li.append(4)
t=tuple(li)
print(t)
'''

#6-8) 정답 :
a = {'A':90, 'B':80, 'C':70}
del a['B']    #a.pop('B')로 사용 가능
print(a)

#7.
partyA ={'Park','Kim','Lee'}
partyB ={'Park','길동','몽룡'}

#7-1) 정답 :
print(partyA.union(partyB))
#7-2) 정답 :
print(partyA&partyB)
#7-3) 정답 :
print(partyA-partyB)
#7-4) 정답 :
print(partyB-partyA)
