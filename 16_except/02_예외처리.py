# 예외처리 형식

# 에러 메세지를 내가 설정한것으로 나타날 수 있게 만드는것

# 예외처리 만드는법
# try:
#     예외 발생 가능한 문장들
# except:
#     예외 처리
# else:
#     예외 발생하지 않는경우, 처리 문장들
# finally:
#     예외발생과 상관없이 항상 처리


# 예외 처리 광대한 경우

# try:
#     # print(10/0)
#     print('나이'+23+'살')
# except:
#     print('오류발생')


# 최상위 예외 클래스

# try:
#     # print(10/0)
#     print('나이'+23+'살')
# except Exception:
#     print('오류발생')


# 에러 종류에 따른 구체적인 오류 담당하는 에러클래스를 이용하여 처리
# 에러 종류 명시
# 에러 메세지 변수를 활용하여 출력 : '에러담당클래스 as 에러메세지 변수명'

# try:
#     예외 발생 가능한 문장들
# except 에러 담당 클래스명 as 에러메세지 변수명:
#     예외 처리 문장들

try:
    print(10/0)
    print('나이'+23+'살')
except ZeroDivisionError as e:  
    print('0으로 나눌 수 없습니다.',e)
except TypeError as e:
    print('잘못입력된 형식입니다',e) #두가지를 같이 써도 try의 첫번째예외에 대해서만 나타남

try:
    num=int(input('숫자입력: '))
    print(num)
except ValueError as e:
    # print('숫자가 아닙니다', e)
    pass #아무것도 입력안하고 'pass'로 넘어가게 만들 수도 있음
else:
    num=num+10
    print(num)
    print('오류가 없습니다')
finally:
    print('종료------')