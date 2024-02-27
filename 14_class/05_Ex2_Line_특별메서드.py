# ex. Line 클래스
# https://docs.python.org/ko/3/reference/datamodel.html#object.__del__

class Line:
    def __init__(self,length):  #생성자
        self.length=length
        print(f'{self.length} 길이의 선이 생성되었습니다.')
    def __del__(self):   #소멸자 (객체소멸시 자동으로 호출됨)
        print(f'{self.length} 길이의 선이 삭제되었습니다.')

    # def __repr__(self):  #print함수로 표현하기 위한 메서드
    #     return f'선의 길이 : {self.length}인 선분'

    def __str__(self):
        return f'선분 {self.length}'

    def __add__(self, other):
        return self.length + other.length
    def __sub__(self, other):
        return self.length - other.length
    def __lt__(self, other):
        return self.length < other.length
    def __gt__(self, other):
        return self.length > other.length
    def __le__(self, other):
        return self.length <= other.length
    def __ge__(self, other):
        return self.length >= other.length
    def __eq__(self, other):
        return self.length == other.length
    def __ne__(self, other):
        return self.length != other.length


line1=Line(10)
line2=Line(20)
# del(line1)
print(line1)
print(line2)

print(line1 + line2)
print(line1 - line2)
print(line1 >= line2)

if line1>line2:
    print('선분1이 길어요')
else:
    print('선분2가 길어요')