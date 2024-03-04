# main

name=''
def input_name():
    global name
    name=input('이름입력: ')
    print(f'__name__:{__name__}')

def get_name():
    print(f'__name__:{__name__}')
    if name == '':
        return 'no name'
    else:
        return name

if __name__ == '__main__':  #자신의 모듈들을 호출함(다른 모듈에선 사용안됨)
    # 다른파일에서 __name__을 쓰면 'main'이 나오지 않고 모듈을 실행한 이름이 뜸
    # 단독으로 실행되면 수행되고 다른파일에 import되면 수행되지 않음
    # 현재 모듈의 이름 또는 __main__값을 저장하고 있는 내장(시스템) 변수
    print(f'__name__:{__name__}')
    input_name()
    print(get_name())