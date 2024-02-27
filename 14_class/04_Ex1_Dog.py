# ex. Dog 클래스

class Dog:
    dog_id=0    #클래스 변수
    def __init__(self,name='',breed='',size='',age='',Color=''):
        self.name=name    #인스턴스 변수
        self.breed=breed
        self.size=size
        self.age=age
        self.Color=Color
        Dog.dog_id+=1    #클래스변수로 작성

    def eat(self,food):
        print(f'{self.name}이(가) {food}를 먹는다')
    def sleep(self):
        print(f'{self.name}이(가) 잠잔다')
    def sit(self):
        print(f'{self.name}이(가) 앉아있다')
    def run(self):
        print(f'{self.name}이(가) 뛴다')

    def __repr__(self):
        return f'{self.name}은 품종 : {self.breed}, 나이: {self.age}'

dog1=Dog('삐삐','Maltese','small','2','white')
print(f'dog1의 id {dog1.dog_id}')
dog2=Dog('벤','Chow Chow','medium','3','brown')
print(f'dog2의 id {dog2.dog_id}')
dog3=Dog('뭉치','Mastiff','large','5','black')
print(f'dog3의 id {dog3.dog_id}')

dog1.eat('사료')
dog2.sleep()
dog3.sit()
dog1.run()

print(dog1)
print(dog2)

dog4=Dog()
print(f'dog4의 id {dog4.dog_id}')

# 인스턴스 변수 : 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
    # 클래스이름.클래스변수명 <으로 메서드 내부에서 사용
    # 인스턴스이름.클래스변수명으로 인스턴스 사용