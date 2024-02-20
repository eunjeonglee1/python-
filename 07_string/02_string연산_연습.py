# 1. 문자열의 모든 글자 뒤에 $ 붙이기
'''
s = '파이썬짱!'
for text in s:
    print(text,end='$')


s = '파이썬짱!'
temp=''
for text in s:
    temp+= text+'$'
print(temp)

# 2.문자열의 짝수번째 글자는 모두 #으로 변경하여 출력

s='파이썬은재미있어요'

for text in s[::2]:
    print(text,end='#')

s='파이썬은재미있어요'
temp=''
for i in s[::2]:
    temp+=i+'#'
print(temp)
'''
#강사님 답변
s='파이썬은재미있어요'
temp=''
cnt=-1
for ch in s:
    if cnt %2 ==0:
        ch='#'
    else :
        pass
    temp+=ch
    cnt+=1
print(temp)

for i in range(len(s)):
    ch = '#' if i %2!=0 else s[i]
    temp+=ch
print(temp)

# 3. 입력받은 문자열을 거꾸로 출력하기

text=input('문자열을 입력하세요:')
rev=text[::-1]
print(rev)
