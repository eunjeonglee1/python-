# 텍스트파일 읽기 : read(), readline(), readlines(), seek()

# 텍스트파일 생성 : 메모장을 이용
# study_data.txt : 한글
# study_data2.txt : 영문

# 1단계 : 파일열기(open)
# 파일이 같은 경로가 없을 시에 경로위치까지 작성해야함
f= open('test/study_data.txt', mode='r', encoding='utf-8')

# 오류 : UnicodeDecodeError: 'cp949' codec <encoding을 지정하지 않았을때 발생
# 영어가 아닌 다른언어면 utf설정해야 오류발생 안함
# 또는 텍스트파일을 'Ansi'로 저장하면 오류발생 안함
# f= open('study_data3.txt',mode='r')

# 2단계 : 파일처리(읽기)


# text=f.read()  # 파일 전체를 읽음

# readline()사용하여 파일 읽기

# text=f.readline() #문장의 '\n'까지 한줄 읽음
# print(text)
# text2=f.readline()
# print(text2)

# 마지막줄을 몇 줄인지 모를때에 while문 사용
# while True:
#     text=f.readline()
#     if not text:  #'not' : 읽을 내용이 없으면(마지막 줄까지)
#         break
#     print(text)

# readlines()사용하여 파일 읽기

# print(f.readlines()) : **리스트형으로 한줄씩 파일전체를 읽음**
# for textline in f.readlines():
#     print(textline,end='') #'\n'를 없애는 방법
#     print(textline)

# readlines()없이 파일 읽기

for textline in f:
    print(textline,end='')

# 3단계 : 파일닫기(close())
f.close()

# 영문으로 된 텍스트파일 읽기
# f1= open('study_data2.txt',mode='r')
# text=f1.read()
# print(text)
# f1.close()
