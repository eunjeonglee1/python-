# 지역변수(local variable)와 전역변수(global variable)

# 지역변수 : 함수 내부에서 정의된 변수, 함수 안에서만 사용 가능
#         -함수 호출 시 생성되고, 함수 종료되면 소멸되어 더이상 사용 불가
# 지역변수명와 전역변수이름이 같을 경우, 지역변수가 우선

a=10  #저장되어있는것을 끌어쓸 수 있는것은 전역변수

def show_info(name):
    age=10   #지역변수
    print(name,age)

show_info('age')

def show1():
    a=1  #지역변수
    a=a+1
    print(f'지역변수 a:{a}',id(a))

def show2():
    # a=a+1  #지역변수를 찾을수 없기때문에 UnboundLocalError로 발생
    print(f'지역변수 a:{a}',id(a))

def show3():
    b=a+1  #이름이 다른 변수를 사용할 시, 전역변수'a'로 사용함
    print(f'a:{a}',id(a))
    print(f'지역변수 b:{b}', id(b))

def show4():
    global a #전역변수를 사용하고 싶을때
    a=a+1
    print(f'a:{a}',id(a))

show1()
show2()
show3()
show4()
print(f'전역변수 a : {a}',id(a))

def sub(x,y):
    a=7
    x,y=y,x
    b=3
    print(a,b,x,y)

a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)

# sub(x,y)=7,3,4,3
# print(a,b,x,y) = 1,2,3,4

def sub(x,y):
    global b,a  #리스트 형태로도 사용가능
    a=7
    x,y=y,x
    b=3  #위에 global로 바꾸었기때문에 지역변수가 전역변수로 바뀜
    print(a,b,x,y)

a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)

# sub(x,y)=7,3,4,3
# print(a,b,x,y) = 1,2,3,4


#매개변수와 전역변수랑 이름이 같을 경우 얕은복사가 되어 똑같이 변형된다
#변경불가능한 튜플을 사용한 전역변수은 괜찮음

def show_list(my_list):
    print(my_list,id(my_list))

my_list=[1,2,3,4]
show_list(my_list)
print(my_list,id(my_list))

# 원본이 수정될 수 없게 만들때에는 깊은복사를 사용하여 전역변수 이름과 다르게 만들기

def show_list(my_list):
    cpy_list=my_list.copy()
    cpy_list[-1]=100
    print(cpy_list,id(cpy_list))

my_list=[1,2,3,4]
show_list(my_list)
print(my_list,id(my_list))

