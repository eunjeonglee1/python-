# 1. 정답: '적당한 수 입니다.'
'''
a=123
if a>100:
    if a>200:
        print('완전히 큰 수 입니다.')
    else:
        print('적당한 수 입니다.')
else :
    print('완전히 작은 수 입니다.')
    print('프로그램 끝입니다.')


# 2. 정답: ['12', '34', '56']
num = ['12','34','56']
for i in num:
    i=int(i)
print(num)


# 3. 정답 : 25개
for i in range(1,100,4):
    print('파이선 꿀잼').

 #갯수 확인할수 있는 방법
x=0
for i in range(1,100,4):
    print('파이선 꿀잼')
    x += 1
print(f'{x}번 출력')

# 4. 정답: 5
num = 0
i =1

while i <8:
    if i %3 == 0:
        break
    i+=1
    num += i
print(num)


# 5. 정답 : -5
result = 0
for i in range(5,-5,-2):
    if i < -3:
        result+=1
    else:
        result-=1
print(result)

# 6. 정답 : apple
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit=='fruit':
    fruit='fruit'
else:
    fruit=fruit
print(fruit)

# 7. 정답 : 0
first_value=0
second_value=0
for i in range(1,10):
    if i == 5:
        continue
        first_value = i
    if i == 10:
        break
        second_value = i
print(first_value+second_value)

# 8. 정답 : 986531
num=""
for i in range(10):
    if i <=5 and (i%2)==0:
        continue
    elif i == 7 or i == 10:
        continue
    else:
        num=str(i)+num
print(num)

# 9. 정답 : 2600
coupon = 0
money =200000
coffee=3500
while money>coffee:
    if coupon<4:
        money-=coffee
        coupon+=1
    else:
        money+=2800
        coupon=0
print(money)

# 10. 정답 : 2번 '6'
list_data_a = [1,2]
list_data_b = [3,4]

for i in list_data_a:
    for j in list_data_b:
        result=i+j
print(result)




# 11. 정답 :
#1)
x=6

while x<7:
    x -=1
    if x ==0:
        break
    print('*'*x)

#2)
for i in range (1,11):
    if i <6:
        for y in range(5-i):
            print(" ", end='')
        for y in range(2*i-1):
            print('*',end='')
    print()

#i를 이용해 공백을 '4-i', 별은 '2*i+1'로 작성
x=0

for i in range (5):
    for x in range(4 - i):
        print(" ", end='')
    for x in range(2 * i + 1):
        print('*', end='')
    print()

x=10

while x>9:
    x -=1
    if x ==0:
        break
    print('*'*x)

bin_=''
while dec > 0:
    r = dec %2
    dec = dec // 2
    bin_=str(r)+bin_
print('0b'+bin_)

'''
star='*'
space=' '

i=0
while i<5:
    a=4-i
    b=2*i+1
    j,k=0,0
    while j<a:
        print(space,end='')
        j+=1
    while k<b:
        print(star,end='')
        k+=1
    i+=1
    print()

i=0
while i<=5:
    print(space*(5-i),star*(2*i-1))
    i+=1
