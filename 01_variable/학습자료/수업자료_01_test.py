# Day1 :

#1. 변수(Variable)
# 변수란 데이터를 저장하는 메모리 주소
# 파이썬의 변수 : 동적타이핑, 레퍼런스 / 변수선언 필요없음
# id(), type()
# print()

# 실습1 : 두 변수의 값 교환(Swap)

# 방법1 : 고전적 방식
'''
a = 10
b = 5
print(a, b)

c = a
a = b
b = c
print(a, b)


# 방법2 : 파이썬 방식

a, b = 10, 5
print('a=', a, 'b=', b)
a, b = b, a
print('a=', a, 'b=', b)


# 실습2 : 변수 삭제
# del a
# print(a)
# NameError


# 실습3 : 변수의 값 출력 print()
age = 30
name = 'HongGilDong'
print(name, age)

addr = '서울시 서초구'
result = name + "은 " + addr + '에 살아요'
print(result)

print(name + ": 나이는 " + str(age) + ' 입니다')
# TypeError : 문자열과 숫자는 연결할 수 없다
# 문자열을 숫자로 변환하는 함수 활용 : str(숫자)


# 실습4 : 변수를 이용한 계산 결과값 출력
# 삼각형의 넓이 계산하여 출력

w = 7
h = 5

s = ( w * h ) / 2
print('넓이=' , s)

# print() 함수의 다양한 출력
# print('문자열', 변수)

#2. 포맷 서식
# 방법1 : '서식'% 값
# format string : %f, %d, %s, %c, %x, %o, %%
print('넓이=%d' % s)

result = '%s은 %s에 살고 나이는 %d에요' %(name, addr, age) 
result2 = '넓이=%.2f' % s
pcnt = 10.5
result3 = '전체면적의 %.3f%%입니다'% pcnt
print(result)
print(result2)
print(result3)


# 방법2 : format() 함수
# format(숫자, '숫자서식')

result4 = format(s, '.2f')
print(result4)
print(format(100, '5d'))
'''
# 연습문제
# 다음의 변수 값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기

kor = 90
eng = 80
math = 75

#총점: 245, 평균: 81.67

total = format(kor + eng + math, 'd')
avg = format((kor + eng + math) / 3, '.2f')
print('총점:', total)
print('평균:', avg)


total=kor+eng+math
avg=format(total/3,'.2f')
print('총점:', total, '평균:', avg)

total=kor+eng+math
avg=total/3
print('총점: %d, 평균: %5.2f' %(total,avg))
print('총점: ',total,', 평균: ',format(avg,'5.2f'),sep='')


print('총점 : %d, 평균 : %.2f' %(kor+eng+math, (kor+eng+math)/3))


# 방법3 : '{1:서식} {0:서식} {2:서식}'.format( , , ) 함수
# str.format() 함수

print(format(3.141592, '10.3f'))
print('{0:.3f}'.format(3.1415927))
print('{1:5d} {2:05d} {0:.3f}'.format(kor, math, eng))

# 방법4 : f'string  => 3.6버전 부터 제공
result5 = f'수학점수는 {math:05d}점이고, 영어 점수는 {kor:7.3f} {eng}'
print(result5)

balance = 10300.0
print(balance)
print(int(balance))
print(format(int(balance), ','))


#3. 상수 : 고정된 변수
# 파이썬에서 상수는 변수와 구분하지 않지만, 상수로 사용 가능
# 상수로 사용할 때 이름은 대문자로 표기할 것을 권장

#4. 리터럴 : 값 그 자체 , 실수, 정수, 문자, 문자열, None, True, False


#5. print()함수의 매개변수 활용

print('국어',kor, '수학',math, '영어',eng, end='=====')
print('국어',kor, '수학',math, '영어',eng, sep='*')

# 파이썬 Doc 사이트 : https://docs.python.org/3/index.html

# 내장함수(built-in functions) :
#      https://docs.python.org/3/library/functions.html

# 튜토리얼 : https://docs.python.org/3/tutorial/index.html

