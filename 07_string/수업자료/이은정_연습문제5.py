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
print(str1.title()+' '+str2.upper())

#4. 정답 :
x=input('문자열을 입력하세요: ')
print(x.replace('o','$'))

#replace코드 사용 못할시 for문으로도 입력가능
temp=''
for ch in text:
    if ch == 's':
        temp+='$'
    else:
        temp += ch
print(temp)





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

from datetime import datetime, date, timedelta
x=input('날짜(연/월/일) 입력: ')
print('split():',x.split('/'))
y=x.split('/')
year=int(y[0])
m=int(y[1])
d=int(y[2])
print(year,type(y),m,type(m),d,type(d))
print({year}+timedelta(days=365*10))


"""
from datetime import datetime, timedelta, date
date2=input('날짜 입력(연/월/일):')
date2=datetime.strptime(date2,'%Y/%m/%d')
# print(type(date2))
print(f'10년 뒤: {date2.year+10}년 {date2.month}월 {date2.day}일')

# from datetime import date,timedelta 10년후 계산이라 쓸 필요가 없었음
momentIn=input('날짜(연/월/일) 입력 : ')
temp=momentIn.split('/')
year=int(temp[0])
month=int(temp[1])
date=int(temp[2])
year10=year+10
print(f'입력한 날짜의 10년 후 => {year10}년 {month}월 {date}일')



#6. 정답 :
#내가 작성한 코드
x=input('숫자를 여러개 입력하세요.')
for text in x[::1]:
    if int(text)>0:
        n=int(text)
        print('\u2764'*n)
    else:
        pass

#강사님이 수정해주신 코드
x=input('숫자를 여러개 입력하세요.')
for text in x:
    n= int(text)
    if n>0:
        print('\u2764'*n)

nums=input("숫자를 여러 개 입력하세요.")
for h in range(len(nums)):
	print(int(nums[h])*'\u2665')

heart = '\u2665'
iter = input('숫자를 여러개 입력하세요.')
for n in iter:
    print(heart * int(n))

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
"""