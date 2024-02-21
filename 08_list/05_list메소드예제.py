# 1. 리스트 요소 추가 : append(), insert() 사용
'''
name_list = []

for i in range(10):
    name=input('회원 입력 : ')
    name_list.append(name)
print(f'회원 명당 : {name_list}')

i=0
while i>10:
    name=input('회원 입력 : ')
    name_list.append(name)
    i+=1
print(f'회원 명당 : {name_list}')

while True:
    name=input('회원 입력 : ')
    if name == 'x':
        break
    else:
        name_list.append(name)


print(f'회원 명당 : {name_list}')

# 회원 명단출력
print(f'회원 명당 : {name_list}')
for name in name_list:
    print(name,end=' ')
print()
'''

#2. 5명의 성적입력, 총점, 평균 계산
total = 0
scores = []
for i in range(5):
    score=int(input(f'학생{i+1} 점수 입력 : '))
    scores.append(score)

cnt=0
for score in scores:
    total+=score
    if score >= 80:
         cnt+=1


# cnt=0
# for score in scores:
#     if score>= 80:
#         cnt+=1

avg = total / len(scores)

print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')
print(f'80점 이상 학생 : {cnt}명')
