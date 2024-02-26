# with문 : close()가 자동으로 수행
# with open(파일명, 모드) as 파일객체:
#           수행문장들

# with open('test/study_data2.txt','r') as f:
#     text=f.read()
#     print(text)
#
# with open('test/file1.txt','a',encoding='utf-8') as f:
#     f.write(text)

# scores.txt : 탭으로 구분한 데이터 파일
with open('test/scores.txt','r',encoding='utf-8') as f:
    data=f.readlines()
    print(data)

# scores2.txt : ,로 구분한 데이터 파일
with open('test/scores2.txt','r',encoding='utf-8') as f:
    data=f.readlines()
    print(data)

print(len(data))