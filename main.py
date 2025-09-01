import warnings
warnings.filterwarnings('ignore')

import logging
logging.basicConfig(level=logging.INFO) # ERROR하면 없어짐(주석제거)




##################
# 코드 정의 영역 #
##################

# import뒤에는 함수 또는 클래스만 작성하자!
# from 뒤에는 폴더 또는 파일명만 작성하자! 
from print_hello import print_hi
from service.print_gg import print_goodgame   
# print_hello -> 같은 폴더 안
# print_gg -> 다른 폴더 안 ( 이 경우에는 import를 다르게 해주면 됨.)

def main(num):
    # 2. Hi도 프린트 
    new_num = print_hi(num=num)
    # 1. 코딩 좋아 ㅎㅎ 
    logging.info(f"코딩 좋아 ㅎㅎ{'ㅎ'* new_num}")
    
    # service 폴더 안의 print_gg를 import 후 함수 호출
    print_goodgame(num1=num, num2=new_num)


# 앞: print_hello에서 정의한 num
# 뒤: main의 num

if __name__ == "__main__":

##################
# 코드 실행 영역 #
##################
    
    main(num=2) # 코딩좋아, Hi가 2번씩 실행됨

