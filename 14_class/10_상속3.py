# 다이아몬드 상속 : 다중상속의 한 사례

class A:
    def greeting(self):
        print('안녕하세요. A입니다')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다')


class D(B,C):  #메서드가 곂치면 가장 먼저 작성한 변수(클래스이름)가 수행함
    pass

obj=D()
obj.greeting()

# 다이아몬드 상속: 서로 다른 클래스에서 동일한 메서드를 상속받는경우,
# 메서드를 탐색하는 순서 (Method Resolution Order : MRO)
    # 클래스 다중 상속의 왼쪽에서 오른쪽 순서로 메서드 탐색

print(D.mro())  #상속순서를 확인하는 방법