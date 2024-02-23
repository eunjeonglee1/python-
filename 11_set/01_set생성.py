# 세트(집합)

#1. 순서가 없다 : 입력되는 순서와 출력되는 순서는 다를 수 있다
#2. 동일한 요소(값)는 중복될 수 없다
#3. 인덱스 사용 불가
#4. 요소 추가/삭제 가능
#5. 변경가능한 항목을 세트의 요소로 가질 수 없다
    # - 리스트(변경 가능)를 세트의 요소로 가질수 없다
    # - 튜플(변경 불가능)을 포함 할 수 있다

# key만 모아놓은 딕셔너리의 특수한 형태
# set(집합) 생성 : {}, set()

# set 생성
s1 = {1,2,3,4,5,1,2,4}
print(s1,type(s1))

s2=set([10,8,11,20,30,10])
print(s2)

s3=set((10,20,300)) #set함수로는 어떠한 형태로도 들어올 수 있다
print(s3)

s4=set({'one':1,'two':2})
print(s4)

# 인덱싱 불가

# s1[0]
# TypeError: 'set' object is not subscriptable

# 리스트는 세트의 요소가 될 수 없다

# s5={1,2,[4,3]}
# TypeError: unhashable type: 'list'

# hashable type => hashing
# 객체를 식별할 수 있는 코드를 부여하여 테이블에 저장하는 방식 : (key,value)

s5={1,2,(4,5)}
print(s5)

