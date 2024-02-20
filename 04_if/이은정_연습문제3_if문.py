#연습문제3 if문

#1.입력받은 십진수를 2진수로 변환하여 출력

x=int(input('십진수 입력 : '))

if x>0:
    a,rem=divmod(x,2)
    if a>0:
        b,rem2=divmod(a,2)
        if b>0:
            c,rem3=divmod(b,2)
            if c>0:
                d,rem4=divmod(c,2)
                y=int(f'{rem2}{rem3}{rem4}'f'{rem}')
                print(f'이진수는 0b{y}')

            

#2. 16진수 글자하나를 입력하면 16진수인지 아닌지 구분하며 16진수인 경우 10진수로 변환하 출력

x=input('16진수 한 글자 입력 : ')
y=(f'1,2,3,4,5,6,7,8,a,b,c,d,e,f')

if x in y:
    val=int(f'{x}',16)
    print(f'10진수 ==> {val}')
else :
    print('16진수가 아닙니다')



#'a'<x<'z' 활용
#print(int(x,16))
x=input('16진수 한 글자 입력 : ')

if 'a'<=x<='f':
    print('10진수 ==>',int(x,16))
elif '1'<=x<='8':
    print('10진수 ==>',int(x,16))
elif 'A'<=x<='F':
    print('10진수 ==>',int(x,16))
else:
    print('16진수가 아닙니다')

#강사님 답변
num= input('16진수 한글자 입력 : ')

if ('0'<=num<='9')or('a'<=num<='f')or('A'<=num<='F'):
    print('10진수 ==>', int(num,16))
else:
    print('16진수가 아닙니다')
