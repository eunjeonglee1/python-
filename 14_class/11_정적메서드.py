# 정적메서드(static method)
    # 인스턴스를 통하지않고 클래스에서 바로 호출하여 사용하는 메서드
    # 전역함수처럼 사용한다고 생각해야함
    # 그래서 Self가 나타나지 않음, 자신cls의 변수 접근 불가
    # 메서드 위에 @staticmethod 키워드를 지정하여 정의

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
    @staticmethod
    def sub(a,b):
        print(a-b)

myCal= Calc()
myCal.add(10,20)

Calc.add(10,20) #객체를 사용하지 않고 클래스이름으로 메서드 바로 호출