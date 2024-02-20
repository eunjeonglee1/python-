#Day1 : 변수에 대해서 실습

#변수란 데이터를 저장하는 메모리 주소
#파이썬의 변수 : 동적타이핑, 레퍼런스 / 변수선언 필요없음
#id(), type()
#print()

#실습1 : 두 변수의 값 교환(Swap)

#방법1 : 고전적 방식
'''
a=10
b=5
print(a,b)

c=a
a=b
b=c
print(a,b)


#방법2 : 파이썬 방식

a,b=10,5
print('a=',a,'b=',b)
a,b=b,a
print('a=',a,'b=',b)


#실습2 : 변수 삭제
del a
print(a)
NameError

#실습3 : 변수의 값 출력 print()
age=30
name='HongGilDong'
print(name,age)

addr='서울시 서초구'
result=name+'은 '+addr+'에 살아요'
print(result)

print(name+": 나이는"+str(age)+'입니다')
#TypeError : 문자열과 숫자는 연결할 수 없
#숫자를 문자열로 변환하는 함수 활용 : str(숫자)

#실습4 : 변수를 이용한 계산 결과값 출력
#삼각형의 넓이 계산
w=4
h=5
s=(w*h)/2
print('넓이=',s)

#print() 함수의 다양한 출력
#print('문자열',변수)

#포맷 서식
#방법1('서식'%값)
print('넓이=%d'%s)

#format string(문자 코드):%f=실수, %d=정수, %s=여러문자열, %c=하나의 문자, %x=16진수, %O=8진수

result='%s은 %s에 살고 나이는 %d에요' %(name,addr,age)
result2='넓이=%7.2f'%s
pcnt=10.5
result3='전체면적의 %.3f%%입니다'%pcnt
print(result)
print(result2)
print(result3)

#방법2 : format()함수
#format(숫자, '숫자서식')
result4=format(s,'.2f')
print(result4)
'''

#연습문제
#다음의 변수값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기

kor=90
eng=80
math=75

x=kor+eng+math
result5=format(x,'d')
print('총점: ',result5)
result6=format(x/3,'.2f')
print('평균: ',result6)

#방법3 :'{0:서식}'.format() 함수
#str.format()함수

print('{0:.3f}'.format(3.1415927))
print('{0:5d} {1:05d} {2:.3f}'.format(kor,math,eng))

#방법4 : f'string - 3.6버전부터 사용함
result7=f'수학점수는{math:05d} {kor:7.3f} {eng}'
print(result7)

balance = 10300.0
print(balance)
print(int(balance))
print(format(int(balance),','))

#상수 : 고정된 변수
#리터럴: 값그자체, 실수, 정수, 문자,문자열, None, True,False

#print()함수의 매개변수 활용

print('국어',kor,'수학',math,'영어',eng,end='====')
print('국어',kor,'수학',math,'영어',eng,sep='*')
