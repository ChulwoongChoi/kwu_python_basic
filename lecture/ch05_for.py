# 반복문(Loop)
#  1. for: 반복횟수를 아는 경우
#  2. while: 반복횟수를 모르는 경우
#  - 반복적인 작업을 가능하게 해주는 도구
#  - list, str, tuple 등 컬렉션 타입의 아이템을
#    한나씩 순회하면서 사용 가능(for)
#  - 특정 조건을 만족하는 경우(while)

# for문 기본 문법(list 활용)
for num in [1, 2, 3]:
    print(num)

# for(int i=0; i<=2; i++) {
#     print(i)
# }

# for문은 반복횟수를 알아야하기 때문에
# i(index)값을 사용해서 반복횟수를 체크
#  → C, JAVA는 i값을 활용해서 반복횟수를 조절
#  → Python은 range() 사용해서 반복횟수를 조절

# range() 함수
#  - range(시작, 끝, 증감)
#  - default: 시작(0), 증감(+1) 
#  - range(3):         0, 1, 2 
#  - range(1, 10):     1, 2, 3, 4, 5, 6, 7, 8, 9  
#  - range(2, 5, 2):   2, 4 

# 구구단 2단
for i in range(1, 10):
    print(f"2x{i}={2*i}")
    
# enumerate() 함수
#  - C, JAVA에서는 i변수가 index 정보를 전달
#  - Python은 enumerate()가 index 정보를 전달
temp = ["A", "B", "C"]
for i, alpha in enumerate(temp):
    print(i, alpha)