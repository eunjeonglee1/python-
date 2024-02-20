# 10개의 정수 입력 후 양수, 음수, 0의 개수 출력하기

pos, neg, zero = 0, 0, 0
for i in range(10):
    # prompt = '숫자' + str(i+1) +'입력 : '
    prompt = f'숫자{i+1}입력 : '
    num = int(input(prompt))
    if num > 0 :
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print('----------------------')
print('양의 개수 :', pos)
print('음의 개수 :', neg)
print('0의 개수 :', zero)
