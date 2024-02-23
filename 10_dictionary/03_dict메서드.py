# 1. get() 메서드

d={'one':1,'two':2,'three':3}
print(d)
print(f'd["two"]: {d['two']} ')
print(f"d.get('two'): {d.get('two')}")

#print(d['four']) #KeyError발생 : 없는key 접근
print(d.get('four')) #key가 없는 경우 'None'으로 반환
print(d.get('four',4)) #key가 없는경우 두번째 인수를 반환

# 2. setdefault() 메서드

print(d)
print(d.setdefault('two')) #값으로 반환
print(d.setdefault('two',20)) #key가 기존에 있기 때문에 값을 그대로 반환
d.setdefault('four',4) #key가 없는경우만 새롭게 만들어서 반환
print(d)

# 3. pop(), popitme()

print(d.popitem())
key,value=d.popitem()  #맨 마지막에 저장된 것을 빼옴
print(f'key={key},value={value}')
print(d)

d['six']=6
d['ten']=10
print(d)

result=d.pop('two') #key값을 반드시 지정해야함
print(result)
print(d)

'''
result=d.pop('seven') #Key가 없는것이기 때문에 KeyError 발생
print(result)
print(d)
'''

# 4. copy()

d2=d.copy()
print(d,id(d))
print(d2,id(d2))
d2['four']=4
print(d)
print(d2)

# 5. update() : 기존 딕셔너리 뒤에 추가시켜 새로 딕셔너리를 만들어줌

d3={'five':5,'two':2,'seven':7}
print(d3)
d3.update(d2)
print(d3)

# 6. clear()

print(d,id(d2))
d.clear()  #기존 딕셔너리를 지움
print(d,id(d2))

print(d2, id(d2))
d2={}  #새로운 딕셔너리 생성
print(d2, id(d2))