# 반복 횟수를 알지못하는 경우 사용

#  1. 기본문법
#   - 조건이 만족하는 동안 반복 실행
#   while 조건:
#         실행문

#  2. 무한 루프
#   - Critical Error → 다음 코드 실행 불가
#   - 조건으로 반복문을 빠져나가는 코드가 반드시 필요!
#   while True:

while True:
    print("메뉴 선택")
    print("1. 햄버거")
    print("2. 사이드")
    print("3. 드링크")
    sel_num = input(">> 번호: ")
    
    if sel_num == "999":
        print("키오스크를 종료합니다.")
        break