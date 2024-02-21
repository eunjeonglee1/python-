# 리스트 메서드 (함수)

#1. append() : 리스트 맨 뒤에 항목을 추가

a=[]
a.append('apple')
a.append('hotdog')
a.append(10)
print(f'alist{a}')

#2. pop([index사용가능, 기본은 -1]) : 리스트의 맨 마지막 요소를 추출하고 요소를 제거(꺼냄)
value=a.pop()
print(f'alist : pop 적용 {a}, value={value}')

a.append('melon')
print(f'alist{a}')
print(f'alist : a.pop(0) {a.pop(0)} pop 적용 후 {a}')

#3. sort(reverse=false) : 리스트의 요소들을 큰 순서대로 정렬하여 정렬된 리스트로 변경
b=[6,3,8,5,1,-3]
print(f'blist {b}')
b.sort()
print(f'sort 적용후 {b}')

#3-1. sort(key=str.lower)
char = ['b','B','A','a','z']
print(f'charList : {char}')
char.sort() #대문자 앞으로, 소문자 뒤로 정렬
print(f'charList : sort() 적용 후 {char}')
char.sort(key=str.lower) #대소문자 구분없이 정렬
print(f'charList : sort(key=str.lower) 적용 후 {char}')
char.sort(key=str.lower,reverse=True) #대소문자 구분 정렬
print(f'charList : sort(key=str.lower,reverse=True) 적용 후 {char}')

#4. reverse() : 리스트를 역순으로 변경
b.reverse()
print(f'reverse 적용후 {b}')
a.reverse()
print(f'reverse 적용후 {a}')

#5. index() : 리스트에서 지정한 값의 위치를 반환 (제일 첫번째로 찾은값 반환), 값이 없는 경우 valueError발생
c=['홍길동','강감찬','성춘향','변학도','강감찬']
idx=c.index('강감찬')
print(f'{idx}')
# idx=c.index('원빈')
# print(f'{idx}')

#6. insert(위치, 값) : 리스트에 값(요소) 삽입 (위치 지정 가능)
print(f'insert 전 {c}')
c.insert(-1,'원빈')
print(f'insert 후 {c}')

c.insert(2,'피카소')
print(f'insert 후 {c}')

#7. remove(값) : 제일 첫번째에서 만나는 리스트에서 지정한 값을 제거
#8. count(값) : 리스트에서 지정한 값의 갯수 반환
print(f'c.remove("강감찬") 전 {c}')
#c.remove('강감찬') # 앞에 하나만 삭제됨
for item in range(c.count('강감찬')): #모든 값을 삭제시킬때
    c.remove('강감찬')
    print(f'강감찬 삭제 {c}')
print(f'c.remove("강감찬") 후 {c}')

#9. extend([f리스트]) : 리스트에 리스트를 추가(확장) => 하나의 리스트로 변경
print(f'blist{b}')
b.extend([10,11,12]) #extend는 b=b+[10,11,12]와 같음
print(f'extend([10,11,12]) 적용 후 blist{b}')
b.append([10,11,12])
print(f'append(([10,11,12]) 적용 후 blist{b}')
b.insert(3, [10,11,12])
print(f'insert(([10,11,12]) 적용 후 blist{b}')
# b.extend(100) #값 하나는 오류가 발생
# print(f'extend(100) 적용 후 blist{b}')

#10. sorted([reverse=false]) 내장 함수 : 리스트를 정렬한것을 새로운 리스트로 반환
a=[3,1,-10,11,2]
print(f'alist{a}')
new_a=sorted(a, reverse=True)
print(f'sorted()함수 적용후 alist{a}')
print(f'sorted()로 생선된 {new_a}')

#11. copy() : 리스트 복사
cpy_a =a.copy()
print(cpy_a)
cpy_a.sort()
print(cpy_a)

#12. clear() : 리스트 비우기 (빈 리스트로 만듬)
cpy_a.clear() #cpy_a[:]=[] 동일한 기능
print(cpy_a)

#13. del() : 리스트 요소 지우기, 리스트 전체를 지우기
del(cpy_a[3:]) # 요소 일부분 지울때
#del cpy_a #메모리에서 요소 자체를 지움
print(cpy_a)

#14. len() : 리스트의 길이
print(len(a))

#15. max() : 최대값을 반환하는 내장함수
#16. min() : 최소값을 반환하는 내장함수

ex_list=[100,7,-2,99,30]
print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')

ex_list=['hello','Exit','Zoo','hI']
print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')

# ex_list=['hello','Exit','Zoo','hI',100,7,-2,99,30] #서로다른 타입이면 Type Error발생
# print(ex_list)
# print(f'최대값 {max(ex_list)}')
# print(f'최소값 {min(ex_list)}')

ex_list=['hello','Exit','홍길동','춘향','방자','hI','100','7'] #알파벳보다 숫자가 먼저 나와서 최소값으로 나옴
print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')

#17. in, not in 연산자 : 리스트 내 원소 존재 여부 True/False 반환

num=[1,2,3,4,5]
result=10 in num
print(result)
result=1 in num
print(result)
result=10 not in num
print(result)

print('----------')
#18. > < >= <= == != : 리스트 일치 검사
list1 =[1,2,3]
list2 =[1,3,2]
print(list1==list2)
print(list1!=list2)

list1 =[1,2,3]
list2 =[5,6,7]
list3 =[1,2,3]
print(list1<list2)
print(list1>list3)
print(list1==list3)

