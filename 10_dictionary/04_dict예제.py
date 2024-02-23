# in / not in 연산자
# 딕셔너리에서는 키가 있는지 확인

d={'nine':9,'ten':10}
print('two' in d)
print('two' not in d)

# 예제.
book={}
book['저자']='홍길동'
book['책제목']='파이썬'
book['출판일']='2020-01-30'
book['가격']='25000'

#문제. 북 딕셔너리의 키와 값을 모두 출력

for key in book.keys():
    # print('%s %s'%(key,book[key]))
    # print('{0}=>{1}'.format(key,book[key]))
    # print(f'{key}=>{book[key]}')
    print(key,'=>',book[key])
