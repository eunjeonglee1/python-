'''
x=0

while x<10:
    x +=1
    if x % 2==0:
        break
    print(x,end=',')

print('\n-------------')

x=0

while x<10:
    x +=1
    if x % 2==0:
        continue
    print(x,end=',')
print('\n-------------')
'''

#연습문제
#숫자 10개를 입력받아서 양, 음, 0개의 개수 출력 (for,whild 둘다 작성)
'''
#for문
x=0
y=0
n=0
for num in range(0,10) :
    num2=int(input(f'숫자{num+1}입력 :'))
    if num2>0:
        x+=1
    elif num2<0:
        y+=1
    else:
        n += 1
print('\n---------------')
print('양의 개수 : ',{x})
print('음의 개수 : ',{y})
print('0의 개수 : ',{n})

#whild문

num = 0
while num<10 :
    num2=int(input(f'숫자{num+1}입력 :'))
    num+=1
'''

#강사님 답변

pos, neg, zero = 0,0,0

for i in range(10):
    num=f'숫자{i+1}입력 : ' #'숫자'+str(i+1)+'입력:'<이라고 적어도 됨
    num2=int(input(num))
    if num2 > 0:
        pos+=1
    elif num2<0:
        neg+=1
    else :
        zero+=1
print('양의 개수:',pos)
print('음의 개수:',neg)
print('0의 개수:',zero)