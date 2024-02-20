# 연산자

# 1. 산술연산자 : +,-,*,/,%,//,**

#divmod(x,y) : x를 y로 나눈 몫과 나머지 반환

# 문제1. 10000초는 몇시간 몇분 몇초인가?

time = 10000
minutes=time // 60
hours=minutes//60
minutes=minutes % 60
sec=time % 60
print(f'{time}은 {hours}시간 {minutes}분 {sec}초 입니다.')


hours=time//3600
time=time%3600
minutes=time // 60
sec=time % 60
print(f'{time}은 {hours}시간 {minutes}분 {sec}초 입니다.')

# 2. 관계 연산자 : >,<,>=,<=,==,!=

a = 100
b = 5
#result = a == b
print (f'{a}=={b}의 결과는 {a==b}')
print (f'{a}!={b}의 결과는 {a!=b}')
print (f'{a}>{b}의 결과는 {a>b}')

# 3. 논리 연산자 : and, or, not

print(a>200 and a<300)
print(not(a>200))

# 4. 비트 연산자 : &,|ㅡ,^,~,<<,>>

print(f'~{a}:{~a}')
print(f'{b}<<1:{b<<1}')
print(f'{b}<<3:{b<<3}')
print(f'{b}>>1:{b>>1}')
print(f'{a}>>3:{a>>3}')

# 대입(할당)연산자 : =

# 대입 연산자 : +=, -=,*=,/=,//=,%=
print('a=',a)
a+=10
print('a+=10:',a)


# 실습문제1. 지폐교환기

#50000, 10000, 5000, 1000, 나머지
#내가 쓴 답
'''
a=int(input('지폐로 교환할 돈:'))
print(f'50,000원짜리 ==> {a//50000}')
b=a%10000
print(f'10,000원짜리 ==> {(b)}')
'''

money = int(input('금액입력 :'))
# 5만원 지폐 교환
#m50 = money//50000
#rem = money % 50000
m50, rem = divmod (money,50000)
#만원 지폐 교환
#m10 = rem // 10000
#rem = rem % 10000
m10, rem = divmod (rem,10000)
#오천원 지폐 교환
m5 = rem//5000
rem = rem %5000
#천원 지폐 교환
m1 = rem//1000
rem%=1000

print('50,000원짜리 ==> %d장'%m50)
print('10,000원짜리 ==> %d장'%m10)
print('5,000원짜리 ==> %d장'%m5)
print('1,000원짜리 ==> %d장'%m1)
print('지폐로 교환하지 않은 돈 ==> %d원'%rem)
