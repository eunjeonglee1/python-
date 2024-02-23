# 함수
# 재사용/ 자주 사용하는 기능들을 위한 코드 집합
# 경제적, 관리용이
# 내장함수(built-in function)/ 사용자 정의 함수 구분

# 함수 정의 및 호출

# 예. 이름, 나이 연락처 출력하는 함수 : show_info()로 사용자 정의

def show_info():
    print('이름:홍길동')
    print('나이:20')
    print('연락처:010-1111-1111')
show_info()

def show_info1():
    #나이, 이름, 연락처 입력을 받아 출력
    name=input('이름입력:')
    age=input('나이입력:')
    phone=input('연락처 입력:')
    print(f'이름:{name}')
    print(f'나이:{age}')
    print(f'연락처:{phone}')

show_info1()

# 문제. 두 정수를 입력받아 더하고 그 결과를 출력하는 함수 add() 정의하기
def add():
    x=int(input('숫자1입력:'))
    y=int(input('숫자2입력:'))
    print(f'숫자1+숫자2의 합 :{x+y}')

# result=add() #반환값이 없음으로 None으로 나옴
# print(result)

# 반환값이 있는 함수 정의하기
def add2():
    x=int(input('숫자1입력:'))
    y=int(input('숫자2입력:'))
    result=x+y
    print(f'숫자1+숫자2의 합 :{x+y}')
    return result

print(f'return value={add2()}')