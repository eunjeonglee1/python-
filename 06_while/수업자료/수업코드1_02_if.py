# 2/15 
'''
# 문제1. 짝수 판단

num = int(input('정수 입력 : '))

if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 문제2. 세 수 중 가장 큰수 출력하기
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

if num1 > num2 and num1 > num3:
    maxNum = num1
elif num2 > num3:
    maxNum = num2
else:
    maxNum = num3
print(f'제일 큰 수 {maxNum}')

# 코드 예1.   
a=int(input('정수1 입력 : '))
b=int(input('정수2 입력 : '))
c=int(input('정수3 입력 : '))
max=0
if a>=b:
    max=a
else:
    max=b

if max >= c:
    pass
else:
    max=c

print(max)

# 코드 예2
x=int(input('정수1 입력:'))
y=int(input('정수2 입력:'))
n=int(input('정수3 입력:'))

if x>y and x>n:
    print('제일 큰 수 :',x)
elif y > n:
    print('제일 큰 수 :',y)
else:
    print('제일 큰 수 :',n)


#문제3. 도형 선택하여 해당하는 도형의 면적 구하기

choice = input('도형입력(1:사각형, 2:삼각형, 3:원) : ')

if choice == '1':
    w = int(input('가로입력: '))
    h = int(input('세로입력: '))
    print(f'사각형의 면적 = {w*h}')
elif choice =='2':
    w = int(input('밑변입력: '))
    h = int(input('높이입력: '))
    print(f'삼각형의 면적 = {w*h/2}')
elif choice == '3':
    r = int(input('반지름 입력: '))
    print(f'원의 면적 = {r*r*3.14}')
else:
    print('잘못 선택하였습니다!')


'''

# 문제4. 컴퓨터와 주사위 놀이하기
# 랜덤숫자 발생

from random import randint

me = int(input('주사위 눈의 수 입력(1~6): '))
com = randint(1,6)

if me > com:
    print(f'com={com}, me={me} : 내가 이겼다')
elif me == com:
    print(f'com={com}, me={me} : 비겼다')
else:
    print(f'com={com}, me={me} : 컴이 이겼네!')















