# 반복문  for

# 1~10사이의 정수를 더하기
'''
total = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(total)

total = 0
for num in range(1, 11):
    total = total + num

print(total)

# 1부터 10사이의 홀수 더하기

total = 0
for num in range(1, 11, 2):
    total = total + num

print(total)

# 1부터 10사이의 짝수 더하기

total = 0
for num in range(2, 11, 2):
    total = total + num

print(total)

# 시작값, 끝값을 입력받아 이 사이에 있는 정수 더하기
start = int(input('시작값입력: '))
end = int(input('끝값 입력:'))

# start, end = map(int,input().split())

total = 0
# NameError: name 'total' is not defined

for num in range(start, end+1):
    total = total + num

print(f'{start}~{end}사이의 합은 {total}')
'''

# 5명의 점수 입력받아 합격>=60, 불합격<60 출력
for _ in range(5):
    jumsu = int(input('0~100사이 점수입력: '))
    if jumsu >= 60:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu} 불합격')










