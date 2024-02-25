#1-1) 정답:
# Before: 10
# In Function: 20
# After: 10

def test(t):
    t = 20
    print ("In Function:", t)
x = 10
print ("Before:", x)
test(x)
print ("After:", x)

#1-2) 정답: None
def sotring_function(list_value):
    return list_value.sort()
print(sotring_function([5,4,3,2,1]))

#1-3) 정답: None
number = "100"
def midterm(number):
    result = ""
    if number.isdigit() is True:
        if number == 100:
            if number/10 == 1:
                result = True
    else:
        result = False
    return result

#1-4) 정답: Flase
def add_and_mul(a, b, c):
    return b + a * c + b
print(add_and_mul(3, 4, 5) == 63)

#1-5) 정답: *args의 순서가 중간으로 가있어서 Error 발생
'''
def args_test_3(one, two, *args, three):
    print(one + two + sum(args))
    print(args)
args_test_3(3, 4, 5, 6, 7)
'''

#1-6) 정답: ["green", "blue"]
def rain(colors):
    colors.append("purple")
    colors = ["green", "blue"]
    return colors

rainbow = ["red", "orange"]
print(rain(rainbow))

#1-7) 정답: 8 ,None <return이 없기때문에
def function(value):
    print(value ** 3)
print(function(2))

#1-8) 정답: "appl"
def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit

fruit = "appl"
get_apple(fruit)
print(fruit)

#1-9) 정답: I Love You543210
def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return(return_sentence(sentence, n))

sentence = "I Love You"
print(return_sentence(sentence, 5))

#1-10) 정답: ["x"]
def test(x, y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)

x = ["y"]
y = ["x"]
test(x, y)
print(y)

#1-11) 정답: 0dd,Even

def countdown(n):
    if n %2 == 0:
        print ("Even")
    else:
        print ("Odd")
        countdown(n-1)
countdown(3)


#1-12) 정답: Value: 10 , Value: 20
def exam_func():
    x = 10
    print("Value:", x)

x = 20
exam_func()
print("Value:", x)

#1-13) 정답: A,B,C,A,B

def message() :
    print("A")
    print("B")

message()
print("C")
message()

print("="*20)

#1-14) 정답: A, A, C, B
print("A")
def message() :
    print("B")

print("A")
print("C")
message()

#1-15) 정답: B, A

def message1():
    print("A")
def message2():
    print("B")
    message1()

message2()


print("="*20)


#1-16) 정답: A, C, B, E, D
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")

message1()
print("E")
message2()

print("="*20)


#1-17) 정답: B, C, B, C, B, C, A

def message1():
    print("A")
def message2():
    print("B")
def message3():
    for i in range(3) :
        message2()
        print("C")
    message1()

message3()


#1-18) 정답: 15
def calc_rect_area(width, height):
    width = 3
    height = 5
    result = width * height
    return result

width = 2
height = 4


#1-19) 정답: None
country = ["Korea", "Japan", "China"]
country.append("Remove")
print(country.remove("Remove"))


#2. 정답:
def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * 24

print(factorial_calculator(5))

#3. 정답 : 함수를 정의하기 전에 먼저 썼기때문에 함수를 찾을수 없어 에러 발생
'''
hello()
def hello():
    print("Hi")
'''
#4-1) 정답 :
def print_coin():
    return "비트코인"

#4-2) 정답 :
print(print_coin())
#4-3) 정답 :
print(print_coin()*100)

#4-4) 정답 :
def print_coins():
    for a in range(101):
        print("비트코인")

#4-5) 정답 :
def mul(x,y):
    return x*y

#4-6) 정답 :
def toUpper(n):
    n2=str(n)
    return n2.upper()

#4-7) 정답 :

def pickup_even(n):
    li = []
    for a in n:
        if a%2 == 0:
            li.append(a)
    return li

n=1,2,4,5,6,7,3,10
print(pickup_even(n))