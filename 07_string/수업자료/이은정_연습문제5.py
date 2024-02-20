#1. 코드결과 작성

#1) 정답 : 21
x='Python is funny'
print(len(x))
print(x.rfind('n'))
print(x.find('n'))
print(str(x.count('n')+x.find('n')+x.rfind('n')))

#2) 정답 : python is a programming language \n
# Python effectively language
text1 = 'Python is a programming language'
text2 = 'and integrate systems more effectively'
print(text1.lower())
print(text1[:7] + text2.split()[-1] + text1[-9:])

#3) 정답 : 'LANGUAGE programming  a is Python'
text = 'Python is a programming language'
temp = ''
for i in text.split():
 print(i)
 if i == 'language':
     temp = i.upper() + ' ' + temp
 else:
     temp = i + ' ' + temp
print(temp)

#4) 정답 : 문자열을,요 <위치 인덱스 관련
text = '문자열을 입력하세요: '
print('{1},{0}'.format(text[-3], text[:4]))

#2. 정답 : 'python'이라는 글자를 포함하여 왼쪽순으로 공백채우면서 10개의 문장이 나타날 수 있게 함
print('{0:>10s}'.format('python'))

#3. 정답 :
str1 = 'this is'
str2 = 'PythON'
print(str1.lower().title()+' '+str2.upper())

#4. 정답 :
x=input('문자열을 입력하세요: ')
print(x.replace('o','$'))





#5. 정답 : input에 입력하는 문자열을 날짜로 변환하는 방법을 알지못해 작성못함
'''
from datetime import date, timedelta
x=input('날짜(연/월/일) 입력: ')
y=date.(x)
print(type(x))
'''

'''
from datetime import date, timedelta
x=input('날짜(연/월/일) 입력: ')
x.strftime('%Y-%m-%d')
print(x+timedelta(days=365*10))
'''
'''
#현재 날짜에서 10년 더하는걸로 나옴(날짜지정X)
from datetime import date, timedelta
x=input('날짜(연/월/일) 입력: ')
x=date.today()  #현재 날짜에서 10년 더하는걸로 나옴(날짜지정X)
print(type(x))
print(x+timedelta(days=365*10))
'''
'''
from datetime import datetime, date, timedelta
x=input('날짜(연/월/일) 입력: ')
print('split():',x.split('/'))
y=x.split('/')
print(y,type(y))
a,b,c = y
print(a,b,c,type(a))
print(x+timedelta(days=365*10))

'''
#6. 정답 :

x=input('숫자를 여러개 입력하세요.')
for text in x[::1]:
    if int(text)>0:
        n=int(text)
        print('\u2764'*n)
    else:
        pass

#
# x=int(input('숫자를 여러개 입력하세요.'))
# for text in x[::1]:
#     print(text)
#     n=int(text)
# print(type(text))
#
# x=input('숫자를 여러개 입력하세요.')
# for text in x[::1]:
#     print(text)