# 문자열 인덱스(String Index)
#  - 문자열은 각 문자마다 순서(인덱스)가 있음
#  - "ABC" → 인덱스(012), A(0), B(1), C(2)
#  - 인덱스 시작은 0
#  - 인덱스는 공백도 포함
#  ex) ABC → 문자열 길이(len): 3, 인덱스: 0~2

# ex) 회원가입시 ID를 이메일로 입력
#     → abc123@naver.com
#     → abc123님 반갑습니다.

# 1. 문자 추출
a = "I Love You"
print(a[2])  # L만 추출

# 2. 문자열 추출(슬라이싱)
#  - 문자열의 시작 인덱스: 0
#  - 문자열의 끝 인덱스: -1
# a[:] → 처음부터 끝까지  
# a[:5] → 0~4
# a[2:] → 2부터 끝까지  
# a[2:3] → 2
print(a[2:6])  # 2~5번 인덱스까지 추출

# 3. 문자열 함수
#  3-1. Upper & Lower : 대문자, 소문자 변환
print(a.upper())
print(a.lower())

#  3-2. replace() : 문자 치환
print(a.replace("o", "z"))

#  3-3. len() : 문자열 길이
print(len(a))

#  3-4. split() : 구분자를 기준으로 문자열 분할
print(a.split())  # 구분자(기본): 공백
print(a.split("o"))

#  3-5. strip() : 좌우 공백 제거
print(a.strip()) # "      I Love YOu          " 

#  3-6. find() and rfind() : 문자열 내부 특정 문자의 인덱스 찾기
#   - 중복문자의 경우 처음 찾는 문자의 인덱스를 반환
#   - find() 좌->우
#   - rfind() 좌<-우
print(a.find("o"))
print(a.rfind("o"))

#  3-7. in() : 특정 문자열 포함여부 확인
#   - 있으면 True, 없으면 False
#   - 대소문자 구별
#   - 문자 or 문자열 모두 가능
print("I" in a)
print("i" in a)
print("Love" in a)
print(" Love" in a)

#  3-8. 문제
id = "   CherrY1004  "
print(id.strip().lower())  # "cherry1004"

# "abc@google.com"
# "abcde@daum.net"
url = "a@naver.com"
idx = url.find("@")

print(url[:idx])  # "a", "abc", "abcde"