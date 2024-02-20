# 연습문제1
# 정수를 입력받아서 홀수인지 짝수인지 판별
'''
num = int(input('정수 입력:'))

if num%2==0 :
    print('짝수')
else :
    print('홀수')
'''
# 연습문제2
# 정수 3개를 입력받아서 제일 큰 수 출력
'''    
#내가 작성한것
x=int (input('정수1 입력:'))
y=int (input('정수2 입력:'))
n=int (input('정수3 입력:'))

if x>y and x>n:
       print('제일 큰 수 :',x)
elif y>n:
    print('제일 큰 수 :',y)
else:
    print('제일 큰 수 :',n)

# 강사님 답변
x=int (input('정수1 입력:'))
y=int (input('정수2 입력:'))
n=int (input('정수3 입력:'))

if x>y and x>n:
    maxNum=x
elif y>n:
    maxNum=y
else:
    maxNum=n
print(f'제일 큰 수 :{maxNum}')
'''

# 연습문제3
# 도형을 선택해서 면적 구하기
'''
x=input('도형입력(1: 사각형, 2: 삼각형, 3: 원):')

if x=='1':
    y=float(input('가로 입력 : '))
    n=float(input('세로 입력 : '))
    a=y*n
    print('사각형의 면적=',a)
elif x=='2':
    y=float(input('밑변 입력 : '))
    n=float(input('높이 입력 : '))
    a=(y*n)/2
    print('삼각형의 면적=',a)
else :
    y=float(input('반지름 입력 : '))
    n=3.14
    a=(y**2)*n
    print('원의 면적=',a)
    
#강사님 답변
choice=input('도형입력(1: 사각형, 2: 삼각형, 3: 원):')

if choice=='1':
    w=int(input('가로입력:'))
    h=int(input('세로입력:'))
    print(f'사각형의 면적={w*h}')
elif choice=='2':
    w=int(input('밑변입력:'))
    h=int(input('밑변입력:'))
    print(f'삼각형의 면적={w*h/2}')
elif choice=='3':
    r=int(input('반지름입력:'))
    print(f'삼각형의 면적={r*r*3.14}')
else:
    print('잘못 선택하였습니다')
'''

#컴퓨터와 주사위 놀이하기
'''
주사위 눈의 숫자를 입력하면 컴퓨터도 난수로 주사위 눈의 수를 발생시켜서 게임
이긴사람 출력하기

주사위 눈의 수의 입력 : 5

컴퓨터가 이겼어요!
축하합니다. 이기셨습니다!
'''
from random import randint
x=int(input('주사위 숫자 입력:'))
y=randint(1,6)

if x>y:
    print(f'com={y} : 축하합니다. 이기셨습니다')
elif x==y:
    print(f'com={y} :비겼습니다')
else:
    print(f'com={y} :컴퓨터가 이겼어요')
