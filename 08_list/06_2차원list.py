# 2차원 리스트 : [행][열]

table = [[1,2,3,4],[7,8,9,10],[10,11,12,14]]
table2 = [[1,2,3,4],[7,8,10],[10,11,12,14]]
print(table2)
print(len(table))
print(table[0])

for item in table :
    print(item, type(item),len(item))

for row in table2: #가변길이 리스트도 사용가능
    for col in row:
        print(col, end=' ')
    print()

row_n=len(table) #각 리스트 길이가 동일한경우만 사용가능
col_n=len(table[0])
print(col_n)

for r in range(row_n):
    for c in range(col_n):
        print(table[r][c], end=' ')
    print()


#연습문제 1 : 학생별 과목별 점수와 총점, 평균계산하고 출력 (2차원 리스트 이용)
x=[[90,85,70],[88,79,92],[100,100,100],[90,60,70]]
print(x)
print('---성적표 (점수)---')
for y in x :
    print(y)

print('---성적표 (점수,총점,평균)---')
for y in x :
    total =sum(y)
    avg = total/len(y)
    print(f'{y},{total},{avg:.1f}')
