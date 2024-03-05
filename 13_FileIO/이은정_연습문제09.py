# 1. 정답:

with open('test/s.txt','r') as f:
    data=f.readlines()  #리스트형태로 나옴
    data.sort()
    print(data)

# 보충설명

# sort_data=sorted(data)
# for d in sort_data:
#     print(d,end='')
# print()

# 2. 정답:

with open('test/yesterday.txt','r') as f:
        text=f.readlines()

li = []
for i in text:
    x=i.split()
    for y in x:
        li.append(y.lower())

for k in sorted(set(li)):
    x=li.count(k)
    print(f"'{k}': {x}")


# 보충설명

# 사용된 단어들만 추출하기 위해 세트로 변경
# wordList=list(set(li))
# wordList.sort()

# 단어별 빈도 계산을 위한 딕셔너리 생성 및 이용
# wordDict=dict()
# for w in wordList:
#     wordDict[w]=li.count(w)
# for key,value in wordDict.items():
#     print(f'{key}:{value}')



# 3. 정답 :
def my_sum(inputfile,outputfile):
    with open(inputfile, 'r') as f:
        texts = f.readlines()
    for i in texts:
        n=i.split()
        y=float(n[0])+float(n[1])
        text=f'{n[0]}+{n[1]}={y},\n'
        with open(outputfile, 'a') as f:
            f.write(text)

my_sum('test/ex9-3.txt','test/ex9-3text.txt')



# def my_sum(inputfile,outputfile):
#     with open(inputfile, 'r') as f:
#         texts = f.readlines()
#         with open(outputfile,'w')as f:
#             for i in range(0,lan(texts))
#                 texts[i]=texts[i].replace('\n','')
#                 if texts[i]!='':
#                     value1,value2=texts[i].split()
#                     val1=float(value1)
#                     val2=float(value2)
#


# def my_sum(input_file, name):
#     with open(input_file,'r') as f:
#         rst = ''
#         for data in f.readlines():
#             a = int(data.split(' ')[0])
#             b = int(data.split(' ')[1])
#             rst += f"{a}+{b}={a+b:.1f}\n"
#         w = open(name, 'w', encoding='utf-8')
#         w.write(rst)
#
# input_file = 'data/number.txt'
# my_sum(input_file, 'result.txt')



# 4. 정답 :
# def input_member(input_filename):
#         namelist=[]
#         while True:
#             name = input('멤버를 입력하세요. (종료는 q) : ')
#             if name =='q':
#                 break
#             else:
#                 namelist.append(name)
#                 print('저장되었습니다.')
#                 print(namelist)
#         with open(input_filename, 'w', encoding='utf-8') as f:
#             for i in namelist:
#                 f.write(i)



# def output_member(output_filename):
#     with open(output_filename,'r',encoding='utf-8') as f:
#         wi=f.readlines()
#         # for mem in wi:
#         #     print(mem,end='')
#         print(wi)

def input_member(path):
    with open(path,'w',encoding='utf-8') as f:

        while True:
            temp=(input('멤버를 입력하세요.(종료는 q) : '))
            if temp=='q':
                return
            else:
                f.write(temp+'\n')

def output_member(save):
    with open(save,'r',encoding='utf-8') as f:
        print(f.read(),end="")

while True:
    x=input('저장 1, 출력 2, 종료 q : ')
    if x=='q':
        break
    elif x=='1':
        input_filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(input_filename)
    elif x=='2':
        output_filename = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(output_filename)
    else:
        print('입력이 잘못되었습니다.')
