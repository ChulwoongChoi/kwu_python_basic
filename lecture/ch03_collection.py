# Collection Type or Framework
#  - 변수: 하나의 값을 저장할 수 있는 메모리 공간
#  - 배열(Array): 복수의 값을 저장할 수 있는 메모리 공간(동일한 타입만 저장)
#  - 컬렉션 프레임워크: 다양한 타입의 복수 값을 저장할 수 있는 메모리 공간

# 학번, 이름(정수), 학과(문자열), 나이(정수), 학점(실수), 주소...

# 1. 컬렉션 타입 4가지
#  가. LIST(기차) → []
#   - 시퀀스 자료형(연속된 값 저장)
#   - 인덱스 사용(Slicing)
#   - 정렬 가능
#   - mutable(생성 된 후 변경 가능)
#   - packing과 unpacking 가능
#   - 멤버 함수: append(), extend(), insert(),
#               remove(), pop(), index(),
#               sorted() 등   
#   1) 리스트 생성
list_a = [1, 2, 3]
list_b = []
list_c = [1, 3.14, "A", True]

#   2) Packing과 Unpacking
#    - 변수 개수와 LIST 값의 개수가 동일해야함
list_d = ["A", "B", "C"]  # Packing
a, b, c = list_d          # Unpacking

#   3) 값 추출
print(list_a[1])
print(list_a[:2])  # 0~1

#   4) append()와 insert() → 삽입
#    - append(): 리스트의 맨 마지막에 값을 추가
#    - insert(): 원하는 인덱스에 값을 추가, 한칸씩 뒤로 이동
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]

b = [1, 2, 3]
b.insert(1, 9)
print(b) # [1, 9, 2, 3]

#   5) extend() : LIST 확장(LIST + LIST)

a = [1, 2]
b = [3, 4]

# [1, 2, 3, 4]
# a.append(b)  # → [1, 2, [3, 4]]
a.extend(b)  # == a+b    / a를 기준으로 b를 합침
print(a)

#   6) remove(), pop() → 제거
#    - remove(): 실제값으로 삭제
#    - pop(): index값으로 삭제
abc = [1, 2, 3, 4, 5]
abc.remove(3)
print(abc)
val = abc.pop(0)
print(abc)
print(val)

#   7) indexx()
#    - () 안의 값의 인덱스 출력
a = ["A", "B"]
print(a.index("B"))  # 1

#   8) sort(), sorted() : 정렬
#    - sort(): 원본 정렬(원본 상실)
#    - sorted(): 복제 정렬(원본 유지)
#    - 디폴트(오름차순), reverse=True(내림차순)
a = [95, 1, 3, 55, 27, 45]
# sort() 사용을 지양!
# a.sort(reverse=True)
# print(a)

sorted_a = sorted(a, reverse=True)
print(sorted_a)


#  나. TUPLE(기차) → ()
#   - LIST와 대부분 동일
#   - 시퀀스 자료형, index 사용
#   - Packing과 Unpacking 가능
#   - ()를 생략 가능
#   → immutable(생성 된 후 변경불가)
#   ＊ 값이 변하면 안되는 결과값 담는 용도로 많이 사용
a = [1, 2]  # 리스트
b = (1, 2)  # 튜플
c = 1, 2    # 튜플
d = (1)     # 튜플
e = 1       # 정수
f = 1,      # 튜플
a, b = 1, 2 


#  다. SET(파우치) → {}
#   - 수학에서 집합과 동일한 개념
#   - 중복값 허용하지 않음(자동으로 제거)
#   - 인덱스 없음(순서 없음)

a = [1, 2, 2, 3]
b = {1, 2, 2, 3}
print(a)
print(b)

# ※ SET 활용법(중복값 제거)
a = [1, 2, 2, 2, 3, 3, 1, 2, 3]
# set(a) → {1, 2, 3}
print(list(set(a))) # → [1, 2, 3]

#  라. DICTIONARY(DICT) → {}
#   - {key: value} 데이터 구조
#   - 인덱스 없음(순서 없음)
#   - key는 Unique해야함(중복 안됨)
#   - value는 중복 가능
#   - value는 key로만접근 가능
#   - 데이터 포맷 JSON과 동일한 형태

a = {
    "Korea": "Seoul",
    "Canada": "Ottawa",
    "USA": "Washington D.C"
}
b = {
    0: 1,
    1: 6,
    7: 9
}

#   1) 아이템 추가 및 변경
#    - 기존에 key가 존재하면, 새로운 값으로 업데이트(덮어쓰기)
#    - 기존에 key가 존재하지 않으면, 새로운 key:value 생성
a["Japan"] = "Tokyo"  # New 생성
a["USA"] = "Newyork"  # 업데이트(Value 덮어쓰기)
print(a)

#   2) 업데이트 → Dict 병합
a = {"a": 1, "b": 2}
b = {"b": 5, "c": 10}
a.update(b)  # a를 기준으로 b를 합치기
print(a)

#   3) 삭제
#    - del 키워드 사용(범용적으로 삭제: 추천하지 않음)
#    - pop 함수 이용
print(a)
a.pop("b")  # Key가 "b"인 아이템 삭제
# del a["b"]
print(a)

#   4) clear
#    - dict의 모든 값을 초기화
print(a)
a.clear()
print(a)

#   5) in
a = {
    "Korea": "Seoul",
    "Canada": "Ottawa",
    "USA": "Washington D.C"
}
print("USA" in a)  # True

#   6) Value Access
#    - dict["key"] → 해당 key가 없으면 Error 발생
#    - dict.get("key") → 해당 Key가 없으면 None 출력(Error X)
# print(a["France"])
print(a.get("France"))

#    - keys()    : key만 반환
#    - values()  : value만 반환
#    - items()   : key, value 반환
#    → for문(반복문)과 자주 사용
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))