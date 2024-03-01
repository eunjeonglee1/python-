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

for k in sorted(set(li)):
    x=li.count(k)
    print(f"'{k}': {x}")


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

# 4. 정답 :
def input_member(input_filename):
        namelist=[]
        while True:
            name = input('멤버를 입력하세요. (종료는 q) : ')
            if name =='q':
                break
            else:
                namelist.append(name)
                print('저장되었습니다.')
                print(namelist)
        with open(input_filename, 'w', encoding='utf-8') as f:
            for i in namelist:
                f.write(i)


def output_member(output_filename):
    with open(output_filename,'r',encoding='utf-8') as f:
        wi=f.readlines()
        print(wi)

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
