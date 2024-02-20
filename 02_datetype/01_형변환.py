#Day2:
#1. 자료형(Data Type)

# 기본자료형 : 정수(int), 실수(float), 부울(bool), 문자열(str)
# iterative/집학적 자료 / sequence:리스트, 딕셔너리, 튜플, 세트

# 1) 진법 변환 함수
#2진수, 8진수, 16진수, 10진수
#bin(), oct(), hex()

print('bin(123)=', bin(123))
print('bin(0o123)=', bin(0o123))
print('bin(0x123)=', bin(0x123))

print('oct(123)=', oct(123))
print('oct(0b11010111)=', oct(0b11010111))
print('oct(0x123)=', oct(0x123))

print('hex(123)=', hex(123))
print('hex(0b11010111)=', hex(0b11010111))
print('hex(0o123)=', hex(0o123))


# 변수의 자료형 : 실행할 때 결정(동적타이핑)
# id(), type()

# 2) 형변환
# int(string), float(string), str(number)

#int(string, base=10)
#int(string) : 10진수 기본
#int(string, base=2), int(string, base=8), int(string, base=16)

print("int('123')=",int('123'))
print('int(\'1010\',2)=',int('1010',2))
print("int('ff',16)=",int('ff',16))
print('int(\'123\',8)=',int('123',8))

#에러 : NameError, TypeError, ValueError
#ValueError: print("int('ff')=",int('ff')) ->10진수값이 아니기때문에 진수지정필요

#float(string) : 문자열을 실수형으로 변환

print('float("13.5")=',float('13.5'))
print('float("13")=',float('13'))

#str(숫자) : 문자열 변환
#print('나이는 = %d' % '20') #Type Error 발생
print('나이는 = %d' % int('20'))
#print('나이는 ='+20) #Type Error 발생
print('나이는 ='+str(20))


#input() 함수 : 키보드로 입력받아서 문자열로 반환
#input(prompt) : prompt는 화면에 표시되는 문자열을 말함

name = input('이름은:')
year = int(input('출생연도는:'))
print(f'이름은{name} ,나이는{2024-year}')

num = input('실수입력:')
result=flout(num)*10
print(f'{num}*10={result}')

#연산자 : *,+
#문자열+문자열=두 문자열을 연결
#문자열*숫자=문자열을 숫자만큼 생성해서 연결

#SW=>Data+algorithm+model+prompt engineering >현재 SW3.0임

#문제1. 두 정수를 입력받아서 합계 출력
num1 = int(input('번호1:'))
num2 = int(input('번호2:'))
print(f'합계{num1+num2}이다')


# 문제2. 몸무게와 키 값을 입력받아서 BMI 지수 계산
# BMI=몸무게/키의 제곱

kg=float(input('몸무게:'))
m=float(input('키:'))
print(f'당신의 BMI : {kg/(m*m)}')


# eval() : 값에 따라 변환
