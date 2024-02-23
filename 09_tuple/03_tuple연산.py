# 복수개 자료 치환

a,b=1,2
print(a,b,type(a),type(b))

a,b=b,a
print(a,b)

(a,b),(c,d)=(10,11),(12,13)
print(a,b,c,d)

# 패킹(packing)

t=1,2,'hello'
print(t)

# 언패킹(unpacking)

x,y,z=t
print(x,y,z,type(x),type(y),type(z))

t2=(1,2,3,4,5)
a,*b=t2  # '*': 여러가지 집합요소를 갖고있다는 뜻 (나머지를 갖고감)
print(a,b,type(a),type(b))
a,b,*c=t2
print(a,b,c)
*a,b,c=t2
print(a,b,c)
#*a,*b,c=t2   #SyntaxError 발생
#print(a,b,c)