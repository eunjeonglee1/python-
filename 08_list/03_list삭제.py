# 리스트 삭제

a = [10, 20, 30]
b = [1,2,3]
c = ['apple','coconut','melon','hotdog']

# 1) 리스트의 한 값을 삭제
print(f'삭제전 alist: {a}')
del(a[1])
print(f'삭제후 alist: {a}')

print(f'삭제전 blist: {b}')
b[1:2] =[]
print(f'삭제후 blist: {b}')

# 2) 리스트 자체를 삭제
a.append(50)
b.append(5)
print(f'삭제전 alist: {a}')
a=[]
print(f'삭제후 alist: {a}') #데이터가 없어지지만 요소를 만들고 싶은경우
print(f'a type : {type(a)}')

print(f'삭제전 blist: {b}')
b=None
print(f'삭제후 alist: {b}') #데이터는 존재함
print(f'b type : {type(b)}')

print(f'삭제전 clist: {c}')
del(c)
print(f'삭제후 clist: {c}') #메모리에서 제거