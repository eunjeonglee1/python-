# 조건문

# if문
'''
num=int(input('정수입력:'))
if num>10 :
    print('10보다 크네요')
    
# if~else문
if num>10 :
    print('10보다 크네요')
else :
    print('10보다 작거나 같아요') #pass로 사용하면 아무것도 안나타남

'''
#연습문제1. 등록된 아이디와 비번 확인 로그인
#내가 작성한 답변
'''
ID=input('아이디 입력 : ')
password=int(input('비밀번호 입력:'))
if ID=='flower' and password==1234 :
    print('로그인 성공!')
else :
    print('로그인 실패!')

ID='flower'
PW='1234'


input_id = input('아이디 입력 : ')
input_pw = input('비밀번호 입력 : ')
'''
'''
if ID == input_id and PW == input_pw :
    print('로그인 성공')
else :
    print('로그인 실패')
'''


# 중첩 if : if조건이 만족하는 경우 또다른 조건에 따라 실행
    #if 아래 if 존재
'''
if ID==input_id:
    if PW== input_pw:
        print('로그인 성공')
    else:
        print('로그인 실패 : 비밀번호가 다르다')
else:
    if PW==input_pw:
        print('로그인 실패 : 아이디가 다르다')
    else:
        print('로그인 실패 : 아이디와 비밀번호 모두 다르다')

'''

# if~elif~else문

'''
if ID==input_id:
    if PW== input_pw:
        print('로그인 성공')
    else:
        print('로그인 실패 : 비밀번호가 다르다')
elif PW==input_pw:
        print('로그인 실패 : 아이디가 다르다')
else:
    print('로그인 실패 : 아이디와 비밀번호 모두 다르다')
'''

# 점수 입력 (0~100) 받아서 학점 출력
# 90점 이상 A
# 80점 이상, 90미만 : B
# 70점 이상, 80미만 : C
# 60점 이상, 70미만 : D
# 60미만 : F

#내가 입력한 내용
'''
S = int(input('점수 : '))
if S>=90:
    print('A')
elif S>=80:
    print('B')
elif S>=70:
    print('C')
elif S>=60:
    print('D')
else :
    print('F')
'''

jumsu=int(input('점수입력(0~100) : '))

if jumsu >= 90:
    score='A'
elif jumsu >=80:
    score='B'
elif jumsu >=70:
    score='C'
elif jumsu >=60:
    score='D'
else:
    score='F'
print(f'{jumsu}에 대한 학점은 {score}')


if jumsu < 60:
    score='F'
elif jumsu < 70:
    score='D'
elif jumsu < 80:
    score='C'
elif jumsu < 90:
    score='B'
else:
    score='A'
print(f'{jumsu}에 대한 학점은 {score}')

#if jumsu>=90 and jumsu <=100:
#if 90<= jumsu<=100:
#    score='A'
