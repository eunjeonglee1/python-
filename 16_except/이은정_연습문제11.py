# 1. 정답 : 3번
# 2. 정답 : 3번

# 3. 정답 :
# import game.graphic.render
# game.graphic.render.render_test()

# from game.graphic.render import render_test

# 4. 정답 :
# import fah_converter as fah

# 5. 정답 : 2번

# 6. 정답 :
'''
7
3
2
1
1
1
종료되었습니다.
'''

try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")

# 7. 정답 : 5번
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break

# 8. 정답 :

from calculator import *

# def first_val():
#     global vel1
#     if fourcal == "/":
#
#
# def second_val():
#     global val2

#
# user_input = input("사칙연산 프로그램: ").split(" ")
# val1, val2=int(user_input [0]), int(user_input [2])
# fourcal = user_input[1]
# if fourcal == "+": result = sum_func(val1, val2)
# elif fourcal == "-": result = minus_func(val1, val2)
# elif fourcal == "/": result =divide_func(first_val, second_val)
# else: result =multiply_func(first_val, second_val)
# print("실행 결과는", result)

# 9. 정답 : 3번X -> 4번
# 10. 정답 : 4번

# 11. 정답 : 4번

alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(a,b,b[0])

# 12. 정답 : '숫자가 아닙니다'

# import random
# answer = random.randint(1,10)
# def guess_number(answer):
#     try:
#         guess = int(input("숫자를 넣어 주세요: "))
#         if answer == guess:
#             print("정답!")
#         else:
#             print("틀렸습니다.")
#     except ValueError:
#         print("숫자가 아닙니다.")
#
# guess_number(answer)

# 13. 정답 : 2번 0SError




# 14. 정답 :
'''
Not divided by 0
1,3
2,1
'''
# for i in range(3):
#     try:
#         print(i, 3// i)
#     except ZeroDivisionError:
#         print("Not divided by 0")