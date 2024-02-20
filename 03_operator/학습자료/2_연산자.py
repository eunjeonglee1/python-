# 연산자

# 1. 산술연산자 : +, -, *, /, %, //, **

# divmod(x, y) : x를 y로 나눈 몫과 나머지 반환

# 문제1. 10000초는 몇시간 몇분 몇초인가?

time = 10000
hours = time // 3600
temp = time % 3600
minutes = temp // 60
seconds = temp % 60
print(f'{time}는 {hours}시간 {minutes}분 {seconds}초입니다.')


# 2. 관계 연산자 : > < >= <= == !=

a = 100
b = 5
# result = a == b
print(f'{a}=={b}의 결과는 {a == b}')
print(f'{a}!={b}의 결과는 {a != b}')
print(f'{a}>{b}의 결과는 {a > b}')

# 3.논리 연산자 : and  or  not

print( (a > 10) and a < 300 )
print( not(a > 200))

# 4. 비트 연산자 : &  | ^  ~ <<  >>

print(f'~{a} : {~a}')
print(f'{b}<<1 : {b<<1}')
print(f'{b}<<3 : {b<<3}')
print(f'{b}>>1 : {b>>1}')
print(f'{b}>>2 : {b>>2}')
print(f'{a}>>3 : {a>>3}')

# 대입(할당) 연산자 : =

# 대입연산자 : +=  -= *= /= //= %=

print('a=',a)
a+=10
print('a+=10 : ', a)



# 실습문제1. 지폐교환기

# 50000, 10000, 5000, 1000

money = int(input('금액입력: '))

# 5만원 지폐 교환
# m50 = money // 50000
# rem = money % 50000
m50, rem = divmod(money, 50000)

# 만원 지폐 교환
# m10 = rem // 10000
# rem %= 10000
m10, rem = divmod(rem, 10000)

# 오천원 지폐 교환
m5 = rem // 5000
rem %= 5000

# 천원 지폐 교환
m1 = rem // 1000
rem %= 1000

print('50000원지폐 ==> %d장' % m50)
print('10000원지폐 ==> %d장' % m10)
print('5000원지폐 ==> %d장' % m5)
print('1000원지폐 ==> %d장' % m1)
print('지폐로 교환하지 않은 돈 ==> %d원'  % rem)









