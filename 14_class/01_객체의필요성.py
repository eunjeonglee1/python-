# 객체의 필요성

# 더하기 기능을 위한 계산기 구현
result=0
def adder(num):
    global result
    result+=num
    return result

print(adder(3))
print(adder(7))
print(adder(9))

#class 적용한 것
class AddCal:
    def __init__(self): #0으로 만들어주는 메소드
        self.result=0
    def adder(self,num):  #**인스턴스를 지정하기 위해 self를 쓰는것**
        self.result+=num
        return self.result

myadder=AddCal()
myadder.adder(10)
print(myadder.result)
myadder.adder(20)
print(myadder.result)
myadder.adder(30)
print(myadder.result)

youradd=AddCal()
print(youradd.result)
youradd.adder(100)
print(youradd.result)
print(type(myadder))

