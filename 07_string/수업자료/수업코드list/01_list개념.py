#
# n개 정수입력받아 합계와 평균 출력

# num1 = int(input('1번째 숫자: '))
# num2 = int(input('2번째 숫자: '))
# num3 = int(input('3번째 숫자: '))
# num4 = int(input('4번째 숫자: '))
'''
total = num1 + num2 + num3 + num4
n = 4
total = 0
num_list = [] # num_list = list()
print(num_list)
for i in range(n):
    num = int(input(f'{i+1}숫자입력: '))
    num_list.append(num)
    total += num
avg = total /4
print(f'합계:{total}, 평균:{avg}')
print('num_list=',num_list)

for num in num_list:
    print(num)
'''

lists = [1,2,3,[1,3],[5,6,7]]
print(lists)
print(lists[0], lists[-1])

# 리스트 생성 : [] , list()
# 리스트 요소 추가 : append()
# 리스트 길이 : len(리스트)

aList = list()
for i in range(10):
    print(aList)
    aList.append(i)
print(aList)

# for와 list
total = 0
num_list = []
# 리스트에 입력한 데이터 저장
for i in range(4):
    num = int(input(f'{i+1}숫자입력: '))
    num_list.append(num)

# 리스트 데이터를 이용해 계산
for x in num_list:
    total += x

# for i in range(len(num_list)):
#     total += num_list[i]
# total = num_list[0] + num_list[1] + num_list[2] + num_list[3]

avg = total /4
print(f'합계:{total}, 평균:{avg}')
print('num_list=',num_list)

# 리스트의 요소 출력
for i in range(len(num_list)):
    print(num_list[i])

for x in num_list:
    print(x)