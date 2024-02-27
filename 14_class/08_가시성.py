# 가시성 : 정보은닉
# 비공개 필드, 비공개 메서드

# 비공개 필드
    # 직접 접근가능한 메서드를 구현하여 사용하거나
    # 데코레이터(@property)를 이용하여 직접 사용

class Product:
    pass

class Inventory:
    def __init__(self):
        self.__items=[]

    def addNewItem(self,product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')
    def getNumberofitems(self):
        return len(self.__items)

    def getitem(self):
        print(self.__items)

    @property   #데코레이터 : 숨겨진 변수 반환
    def items(self):
       return self.__items

myInvent=Inventory()
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())

myInvent.getNumberofitems()
myInvent.getitem()
print(myInvent.items)