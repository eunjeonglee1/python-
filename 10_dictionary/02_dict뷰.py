# 뷰(view)
# keys(), values(), items()
d={'one':1,'two':2,'three':3}

# key() 뷰
keys=d.keys()
print(keys,type(keys))

print(list(keys))

# 키(key)들에 대한 값(value)들을 출력

for key in d.keys():   #***중요
    print(key,d[key])

# values() 뷰

values = d.values()
print(values,type(values),tuple(values))
print(len(values))

for value in d.values():
    print(value,end=',')
print()

# items() 뷰

items=d.items()
print(items,type(items))
print(list(items))

for item in d.items():
    print(item, type(item))

for key,item in d.items():
    print(key,item)

# 연습문제
x={'학번':'1000','이름':'홍길동','학과':'컴퓨터학과'}
print(x)
x['연락처']='010-1111-1111'
print(x)
x['학과']='파이썬학과'
print(x)
del(x['학과'])
print(x)