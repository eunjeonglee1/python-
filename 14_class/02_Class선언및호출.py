# 클래스 선언 방법
# class 클래스 이름[(상속클래스)]:
#     클래스 변수(필드) 선언
#     메서드 정의
#     def 메서드이름(self, 매개변수들):
#         문장들

# 객체(인스턴스) 생성
# 객체(인스턴스)이름=클래스명() : 생성자
# 객체 : 단독으로 지칭할때
# 인스턴스(instance) : 클래스와 연관지어서 객체를 부를때

# ex. 자동차 클래스 선언

class Car:
    color=''
    speed=0
    def drive(self):  # self : 기존의 함수와 구분, 자신의 객체(인스턴스)임을 의미
        self.speed = 10


# 인스턴스 생성

car1=Car()  #car(): 인스턴스를 생성하는 생성자함수
car2=Car()
car3=Car()

# 인스턴스의 필드 이용 : 인스턴스이름.필드명

print(type(car1),id(car1))
print(type(car2),id(car2))
print(type(car3),id(car3))

print(f'car1의 speed {car1.speed}')
print(f'car2의 speed {car2.speed}')
print(f'car3의 speed {car3.speed}')


#istinstance(인스턴스명 ,클래스명) : 어떠한 클래스에서 만든 객체인지 확인

print(isinstance(car1,Car))



# 인스턴스 생성 후 필드 추가하고 값을 대입할 수 있다 (복잡해지기때문에 사용 잘 안함)
# car1.color='red'
# car2.color='blue'
# car3.color='yellow'
# car1.speed=0
# car2.speed=0
# car3.speed=0
#
# print(car1.color)

# 매서드 호출 : 인스턴스명.메서드명(인수들)

car1.drive()
print(car1.speed)

''' #참고용

# 파이썬의 클래스(내장함수)들 : int, float, str, set, dict, list, tuple,...
a=int(10)
print(a)
b=list(range(10))
print(b)
c=dict(x=10,y=20)
print(c)

print(type(a),type(b),type(c))
print(isinstance(a,int))
print(isinstance(a,float))
d=10.5
print(isinstance(d,float))
'''

