# csv(comma separated value) 파일읽기
# csv 모듈 임포트
# https://docs.python.org/ko/3/library/csv.html

import csv

# csv.reader()

# path='test/scores2.csv'
# with open(path,'r',encoding='utf-8') as f:
#     data=csv.reader(f)
#     for x in data:
#         print(x)

# csv.writer(csvfile,delimiter(구별할 기호))

# 객체.writerows(객체 - csv파일에 쓸 객체) : 여러줄의 데이터를 작성해줌

data_list=[['구','전체','내국인','외국인'],['관악구',519864,502089.17775],
           ['강남구',547602,542498,5014],['송파구',686181,679247,6934],
           ['강동구',428547,424235,4312]]

print(data_list)

with open('test/pop.csv','w',encoding='utf-8',newline='') as f:
    obj=csv.writer(f,delimiter=',')
    obj.writerows(data_list)

#함수 정의로 csv 파일 작성
def writecsv(filename,datalist,encoding):
    with open(filename, 'w', encoding=encoding, newline='') as f:
        obj = csv.writer(f, delimiter=',')
        obj.writerows(datalist)

writecsv('test/pop1.csv',data_list,'utf-8')
