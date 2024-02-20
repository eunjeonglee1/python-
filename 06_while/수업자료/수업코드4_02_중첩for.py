# 다중 for를 이용

# for x in range(3):
#     print(x)
#     for y in range(1, 5):
#         print(y+4*x, end=' ')
#     print()
#
# a = 0
# for x in range(3):
#     for y in range(4):
#         a += 1
#         print(a, end=' ')
#     print()

# 2~9단 구구단 출력
for dan in range(2, 10):
    for n in range(1, 10):
        print(f'{dan}*{n:3d}={dan*n:>3}')
    print()