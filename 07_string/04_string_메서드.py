# 1. 문자열 대소문자 변환
#unper(),lower(),title(),capitalize(),swapcase()
text1='Python is preat!'
text2='yes, it is.'
text3= "it's not like any other"

print(f'text1:{text1}')
print(f'text2:{text2}')
print(f'text3:{text3}')
print('------------')
print('대문자로',text1.upper())
print('소문자로',text1.lower())
print('단어별로 시작문자 대문자로',text2.lower().title())
print('문장의 첫글자만 대문자로',text1.upper().capitalize())
print('서로 반대(대, 소문자)의 문자로 변경 swapcase()',text1.swapcase())

# 2. 문자열 검색
# count(단어),find(단어,rfind(),index(),rindex(), startswith(), endtwith()
text4='I like python, i like swimming, i like hotdog'
print('count():',text4.count('Python'))
print('count():',text4.count('like'))
print('find():',text1.find('Python')) #인덱스 변환 (가장 첫번째로 만난 위치)
print('rfind():',text1.rfind('Python'))
print('rfind(,3):',text1.rfind('Python',3))
print('find():',text1.find('melon')) #없다면 '0'으로 표시
print('rfind():',text1.rfind('melon'))
print('index():',text4.index('like')) #찾는 문자열이 없는경우 오류 발생
print('rindex():',text4.rindex('like'))
print('startwith():',text4.startswith('like'))
print('startwith():',text4.startswith('I like')) #논리값 반환
print('endtwith():',text4.endswith('I like'))


# 3. 문자열 치환, 편집
#strip(), rstrip(), lstrip() : 공백문자 (지정문자) 제거
#replace() : 문자치환
text5 = '       ham haha hotdog!   '
text6 = '<><><hoho>>>>!'
print('strip():',text5.strip())
print('lstrip():',text5.lstrip())
print('rstrip():',text5.rstrip())
print('strip(<>):',text6.strip('<>')) #문자지정하면 그부분만 삭제
print('replace():',text5.replace('ham','hom'))


# 4. 문자열 분리/결합
#split(),rsplit(),join()
print(text4)
print('split():',text4.split())
print('split():',text4.split(','))
print('rsplit():',text4.rsplit())

text8='apple banana kiwi'
date=text8.split()
print(date)
print('join():','-'.join(date))
print('join():','/'.join(date))
print('join():',''.join(date))
print('join():',''.join(date))

text9='''firsline
.. secondline
.. thirdline
'''
print(text9.split('\n'))
print(text9.splitlines())
print(text9.split())
print(text9.split('\n',1))
print(text9.split('\n',maxsplit=1))

# 5. 문자열 정렬 : 포멧 , ^, <, > 를 함수로 표기 한 것
#center(), ljust(),rjust()
print('center():',text8.center(30))
print('center():',text8.center(30,'*'))
print('ljust():',text8.ljust(30))
print('ljust():',text8.ljust(30,'-'))
print('rjust():',text8.rjust(30,'-'))

# 6. 문자열 판단 : 숫자, 알파벳, ... 을 참과 거짓으로 판별
#lsdigit(), isdecimal(), isalpha(),...
print('1234'.isdigit())
print('1234'.isalpha())
print('abc한글'.isalpha())
print('1234***'.isalnum())
print('hello'.isupper())
print('hello'.islower())
print('hello'.istitle())
print('Hello HoHo'.istitle())

#Unicode : '\u'+16진법으로 작성
print('\u0101','\u0663','\u0011')