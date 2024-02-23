# 1. 함수의 매개변수(paramater)와 인수(인자:argument)

# 매개변수 : 함수를 정의할 때 함수로 전될되는 값을 갖는 변수
# 인수 : 함수를 호출할때 전달되는 값 (변수)

def get_area(width,height):
    result=width*height
    print(f'사각형 가로={width}, 세로={height}, 면적은 {result}')
    return result

print(get_area(10,20))

# 문제. 사칙연산을 수행하는 함수의 정의 만들기
# add() : 두 수를 더하기
# sub() : 두 수를 빼기
# mul() : 곱셈
# div() : 나눗셈

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b ==0:
        print('0으로 나눌 수 없다')
    else:
        return a/b

x=10
y=20
# print(f'{x}+{y}={add(x,y)}')
# print(f'{x}-{y}={sub(x,y)}')
# print(f'{x}*{y}={mul(x,y)}')
# print(f'{x}/{y}={div(x,y):.2f}')

# 2. 디폴트 매개변수
# 매개변수의 기본값이 지정되어 있는 경우
# 디폴트 매개변수는 반드시 마지막에 위치해야함

# def greet(msg='Hello',name) #SyntaxError발생
def greet(name,msg='Hello'):
    print(name+','+msg)

greet('홍길동','hi')
# greet('홍길동') # 디폴트값을 지정 안했을때 값을 입력 안하면 TypeError 발생
greet('홍길동')

# 3. 위치 매개변수(positional parameter)
# 매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장이 됨
# 매개변수 순서대로 인수를 전달


# 4. 함수에 여러개 자료로도(리스트, 딕셔너리) 전달가능

# 리스트형
def show_names(names):
    for name in names:
        print(name, end=' ')

show_names(['홍길동','심청이','강감찬'])
print()

# 딕셔너리형
def show_info(info):
    print(info)
    for key,value in info.items():
        print(key,info[key])

info={'이름':'홍길동','나이':20}
show_info(info)

# 5. 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러개의 값을 전달 받을때 사용

# 1) '*'args(변수이름) : 길이가 어떻든 반환해주는 형식 , 튜플 형식으로 나옴
# *args는 **kwargs 를 같이쓸때에는 반드시 앞에 와야함

print('hi','ho',end=' ')
print()
def my_sum(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(my_sum(1,2))
print(my_sum(1))
print(my_sum(1,2,3))
print(my_sum(1,2,3,4,5,6))

# 2) '**'kwargs(변수이름)=> key=value를 사용할때
# 매개변수 키워드를 알 수 없을때에 사용


def show_info (**kwargs):
    for key in kwargs.keys():
        print(key,end=' ')
    print()
    for value in kwargs.values():
        print(value,end=' ')
    print()
    for item in kwargs.items():
        print(item)

show_info(id='abc')
show_info(id='abcd', name='hong')
show_info(id='abcd', name='hong',age=30)

# 6. 키워드 인수(keyword arguments)
# 인수들 앞에 키워드를 두어서 인수를 구별
# 인수의 위치가 매개변수의 위치와 달라도 됨
# 매개변수 키워드를 알고 있어야 사용 가능

def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40)

my_print(a=5,c=10,b=30) #순서가 상관없이 '매개변수=값'으로 써도 매개변수 순으로 인수가 호출됨
# my_print(c=10,30,5) #디폴트가 앞으로 나와있기때문에 SyntaxError 발생

def show_info2(id,name,age):
    print(id)
    print(name)
    print(age)

show_info2('123','hong',30)
show_info2(id='123',age=30,name='hong')


def my_func(a=1,*args,**kwargs):
    pass
my_func(1,2,3,a=1,b=1)
my_func(1,2,3,a=1,b=1)

# 함수 호출:
# 위치인수와 키워드인수를 함께사용하는 경우, 위치인수는 앞으로 키워드인수는 뒤로 사용해야함
# 인수 입력할때에는 위치인수 -> *args -> **kwargs(키워드인수) 순
# 함수정의 : 위치 매개변수 뒤에 디폴트매개변수는 뒤에 <<<*다시듣기*