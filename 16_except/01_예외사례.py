# ZeroDivisionError: division by zero
# 10/0 # 0으로 나눌려고 할때

# TypeError
# print('나이는'+23+'살')

# NameError
# print(b)

# ValueError: incomplete format 값이 잘못 배정될때
# c=100
# print('%d%'%c)

# SyntaxError 문법적인 오류
# if x>10
#     print('hello')

# IndexError 문자를 찾을 수 없을때
# a=[1,2,3,4]
# print(a[5])

# UnboundLocalError 참조 할 수 있는 변수가 없을때에 나타나는 지역변수 에러
# def add():
#     a=a+1
#
# add()

# ModuleNotFoundError 참조 할 수 있는 모듈이 없을때
# import  mymodul

# FileNotFoundError 파일을 찾을 수 없을때
# with open('except.txt','r') as f:
#     f.read()

# OSError 경로명을 잘못썼을때
# with open('c:\file\except.txt','r') as f:
#     f.read()