# 1. 정답:

with open('test/s.txt','r') as f:
    data=f.readlines()  #리스트형태로 나옴
    data.sort()
    print(data)

# 2. 정답:


with open('test/yesterday.txt','r') as f:
        text=f.readlines()

li = []
for i in text:
    x=i.split()
    for y in x:
        li.append(y.lower())

print(li)
