# seek(offset, whence) 함수 : 내가 탐색하고자 하는 위치 지정

print('파일 내에서 검색 : seek() ----')
f=open('test/seek_test_data.txt', 'r', encoding='utf-8')

f.seek(0,0)  # 시작위치: 0, 0: 파일처음
lines=f.readlines()
print(lines)

f.seek(3,0)
lines=f.readlines()
print(lines)

f.seek(8,0)
lines=f.readlines()
print(lines)

f.seek(16,0)  #utf-8은 3바이트이기때문에 한글은 3간격으로 작성
lines=f.readlines()
print(lines)

f.close()