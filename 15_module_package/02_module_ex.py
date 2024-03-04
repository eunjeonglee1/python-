# import show_info
# show_info.show_name()
# show_info.show_phone()

# import show_info as si  # 모듈 이름이 너무 긴 경우 이름 줄여서 사용한 경우
# si.show_phone()
# si.show_phone()

# from show_info import show_name,show_phone  # 필요한 함수만 적용
# show_name()
# show_phone()

from show_info import * #비공개 메서드 빼고 전체
show_name()

from show_info import show_phone as si  # 모듈이름부터 함수이름까지 묶어 줄여서 사용하는 경우
si()
show_phone()