# 반복문 for

#1~10사이의 정수를 더하기

'''
total = 1+2+3+4+5+6+7+8+9+10
print(total)

total=0
total=total+1
total=total+2
total=total+3
total=total+4
total=total+5
total=total+6
total=total+7
total=total+8
total=total+9
total=total+10
print(total)

total=0
for num in range(1,11):
    total =total + num
print(total)
'''

# 1~10사이의 홀수를 더하기
'''
total=0
for num in range(1,11,2):
    total += num
print(total)
'''

#시작값, 끝값을 입력받아 이 사이에 있는 정수 더하기

x=int(input('시작값:'))
y=int(input('끝값:'))

total=0
for result in range(x,y+1):
    total+=result
print(total)

#강사님 답변
start=int(input('시작값 입력:'))
end=int(input('끝값 입력:'))

total=0
for num in range(start,end+1):
    total += num
print(f'{start}~{end}사이의 합은 {total}')

# 5명의 점수 입력받아 합격>=60, 불합격<60 출력
for _ in range(5):
    jumsu = int(input('0~100사이 점수입력: '))
    if jumsu>=60:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu}불합격')