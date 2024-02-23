# zip() 함수

foods=['떡볶이','짜장면','피자','라면']
sides=['김치','단무지','피클']
zip_list=list(zip(foods,sides)) #짝지어서 리스트로 생성
zip_dic=dict(zip(foods,sides))  #딕셔너리로 생성
print(zip_list)
print(zip_dic)

# 리스트 컴프리헨션

xlist=[x*2 for x in range(1,11)]
print(xlist)

ylist=[x+y for x in range(1,11) for y in range(10,21)]
print(ylist,'\n', len(ylist))

foodlist = [(x,y) for x in ['밥','국수','짜장면'] for y in ['김치','단무지']]
print(foodlist)

# 세트 컴프리헨션

print([x+y for x in range(1,5) for y in range(10,15)])
yset={x+y for x in range(1,5) for y in range(10,15)}
print(yset,'\n', len(yset))

# 딕셔너리 컴프리헨션

print({food:side for food in foods for side in sides})  #key의 유일한 속성때문에 마지막 하나의 값인 '피클'만 나옴

stds=['철수','영희','길동','순희']
std_dic = {std:0 for std in stds}
print(std_dic)
print(std_dic.items())

stds={'철수':90,'영희':50,'길동':60,'순희':100}
std_scores={name:'pass'if score > 60 else 'non-pass' #if의 한줄문을 반복문장으로 만든것
            for name, score in stds.items()}
print(std_scores)

#위의 구조를 풀어서 코딩한 것
std_scores2=dict()
for name,score in stds.items():
    if score>60:
        std_scores2[name]='pass'
    else:
        std_scores2[name]='non-pass'
print(std_scores2)