# 2차원 튜플 생성

t=((1,2,3),(4,5,6),(7,8,9))
print(t)

# 2차원 튜플의 요소를 행렬의 테이블 형식으로 출력

#내가 답한것
x=len(t)
y=len(t[0])
for n in range(x):
    for c in range(y):
        print(t[n][c], end=' ')
    print()

#강사님 답변
for r in t:
    for c in r:
        print(c,end=' ')
    print()

for r in range(len(t)):
    for c in range(len(t[r])):
        print(t[r][c], end=' ')
    print()

for i in range(len(t)):
    lt1,lt2,lt3=t[i]
    print(lt1,lt2,lt3)