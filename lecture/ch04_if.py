# 제어문(Control)
#  1. 조건문(Condition) → if
#  2. 반복문(Loop)      → for, while

# 조건문
#  - 특정조건을 만족하는 경우 수행할 작업에 사용
#  - 모든 조건은 boolean으로 표현 됨
#  - 조건문의 경우 if, elif, else 블록 내 들여쓰기
#  - 모든 블록문의 시작점의 마지막 콜론(:) 추가
# if (조건) {
#     내용
# }
# if 조건:
#     내용
# print()


# if 문법
#  1. 하나의 if문에서 if와 else 1번만 사용 가능
#  2. 하나의 if문에서 elif 여러번 사용 가능
#  3. 하나의 if문에서 실행되는 문은 반드시 1개(위에서 아래로 실행)
#  4. else는 위의 모든 조건이 만족하지 못하는 경우 실행(최하단 작성)

# if 조합식
#  1. if()
#  2. if()~elif()
#  3. if()~else
#  4. if()~elif()~else

# # if 조건1:
#     내용
# elif 조건2:
#     내용
# elif 조건3:
#     내용
# else:
#     내용
    
# 논리연산자(AND, OR, NOT)
#  1. AND → 모든 조건이 참인 경우 실행 
#  2. OR  → 조건 중 하나라도 참이면 실행
#  3. NOT → True -> False로 False -> True로 

score = 4.2

# C, JAVA
if score >= 4.1 and score <= 4.5:
    print("A")
elif score >= 3.6 and score <= 4.0:
    print("B")
elif score >= 3.1 and score <= 3.5:
    print("C")
elif score >= 2.6 and score <= 3.0:
    print("D")
else:
    print("F")
    
# Python
if 4.5 >= score >= 4.1:
    print("A")
elif 4.0 >= score >= 3.6:
    print("B")
elif 3.5 >= score >= 3.1:
    print("C")
elif 3.0 >= score >= 2.6:
    print("D")
else:
    print("F")
