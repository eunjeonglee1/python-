# 재귀함수(recursive function)
# 함수 내부에서 자신의 함수를 다시 호출

# 1~n까지의 합 재귀함수

def my_sum(n):
    if n ==1:
        return 1
    return n+my_sum(n-1)

print(my_sum(10))

# 1*2*3*....*n : n! 계산하는 재귀함수

#재귀함수 사용하지 않았을때
def my_fact1(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

#재귀함수를 사용했을때
def my_fac2(n):
    if n <= 1:
        return 1
    return n*my_fac2(n-1)


print(my_fact1(5))
print(my_fac2(5))

# 내부함수

def outfunc(x,y):
    def infunc(a,b):
        return a+b
    return infunc(x,y) #위에있는 outfunc의(x,y)를 가져와서 infunc(a,b)에 적용시킨다는 뜻

print(outfunc(10,30))

# 람다(lambda) 함수
# 한줄짜리 함수, return문을 사용하지 않음
# 변수명 = lambda <인수들>:<반환할식>
# 람다함수는 함수 참조를 반환
# 변수로 람다함수 객체를 받아서 함수호출
# 람다를 변수이름대신에 사용한것
# 전역변수를 사용
# 문장에서 새로운 변수를 지정할 수 없다.

f= lambda :1
print(f())

add=lambda x,y:x+y
print(add(2,3))

add=lambda x,y=30:x+y
print(add(10))
print(add(10,50))

# 람다 표현식: 함수이름을 명명하지 않고(변수에 할당하지 않고) 바로 호출 가능
# (lambda 매개변수들:식) (인수들)

print((lambda x:x+10)(10))

# 람다표현식 안에서는 변수생성 불가
# (lambda x: y=10:x+y)(10)  #SyntaxError발생

# 람다표현식 바깥에서 정의된 변수를 람다표현식 안에서 사용
y=10
(lambda x:x+y)(10)

# (lambda x,y,z:x+y)(10) #인수를 매개변수의 수와 맞게 작성해야함

def plus_ten(x):
    return x+10

#[1,2,3,4,5]+10 를 만드는 여러가지 방법
new=[]
for n in [1,2,3,4,5]:
    new.append(n+10)
print(new)

print(list(map(plus_ten,[1,2,3,4,5])))  # map(fuct,데이터들)로 사용
print(list(map(lambda x:x+10,[1,2,3,4,5]))) #map에 람다함수 사용한 예시

# 두 개의 리스트 요소 더하기

def add_list(x,y):
    new_list=[]
    for i in range(len(x)):
        new_list.append(x[i]+y[i])
    return new_list

a=[1,2,3,4]
b=[10,11,12,13]
print(add_list(a,b))

# map(func,iterable_data)함수
def add_two(x,y):
    return x+y
print(list(map(add_two,a,b)))
print(list(map(lambda x,y:x+y,a,b)))

