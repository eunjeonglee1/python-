# 메서드

s={10,1,3,4}
print(s)

# 1. 데이터 추가

# add() 메서드 : 집합에 요소 추가

s.add(100)
print(s)

# update()
s.update([5,6])
print(s)

# 2. 데이터 삭제, 추출

# pop() : 맨 앞의 요소 추출

result=s.pop()
print(result)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

# remove() : 값 지정해서 요소 삭제

s.update([10,11,12,13,14])
print(s)
s.remove(10)
print(s)

# s.remove(15) #삭제하려는 값이 없는경우 KeyError 발생
# print(s)

# discard() : remove 비슷하지만 Error발생 안하게 만들 경우
s.discard(6)
print(s)
print(s.discard(16)) #삭제하려는 값이 없으면 None 반환
print(s)

# clear() : 요소 전체 삭제
s.clear()
print(s)

# 3. 연산

s1 = {1,2,3}
s2 = {3,4,5}

# 합집합 : union() , | (비트 연산자 사용가능)

print(s1.union(s2))
print(s1|s2)

# 교집합 : intersection() , &

print(s1.intersection(s2))
print(s1&s2)

# 차집합 : differnce() , -

print(s1.difference(s2))
print(s2.difference(s1))
print(s1-s2)
print(s2-s1)

