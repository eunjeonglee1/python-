# 클래스 메서드(class method)
    # - 인스턴스를 통하지 않고 클래스에서 바로 호출
    # - 순수함수(pure function)
    # - @classmethod를 지정하여 사용
    # 클래스 자체에서 호출하고 싶을때에 사용

class Person:
    count=0  #클래스 변수

    def __init__(self):
        Person.count+=1

    @classmethod
    def print_count(cls):   #cls : 클래스 의미
        print(f'{cls.count}명 태어났어요')

    @classmethod
    def create(cls):  #생성자와 같은 메서드 (클래스 메서드로 인스턴스 생성)
        p=cls()       #'Person()' 클래스와 같음
        return p


kim = Person()
Person.print_count()

choi = Person()
Person.print_count()

lee=Person.create()
Person.print_count()