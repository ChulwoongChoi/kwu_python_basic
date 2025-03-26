# 주석(Comment)
#  - 개발자 메모(코드 리뷰)
#  - 프로젝트 초기에는 다양한 주석을 활용
#  - 프로젝트 종료 후 배포시에는 주석 삭제

# 1. 출력함수(print)
#  - () 안의 값을 출력,
#  - 변수값 확인 용도로 많이 사용
print("Hello Python")
print("=" * 200) # "=" 200번 출력


# 2. 자료형(Data Type)
#  - 정수형(int): 3, -1, 0
#  - 실수형(float): 3.14, 0.0, -2.2
#  - 논리형(boolean): True, False
#  - 문자열형(String): "Hello", 'Hi'
#  ※ Python은 문자형(char) 없음
#     JAVA, C는 'A'(문자형), "Hello"(문자열형)

# 3. 변수(Variable)
#  - 하나의 값을 저장할 수 있는 메모리 공간
#  - 문법
#    num = 4 → 변수선언 및 초기화
#    변수명 대입연산자 값(실제)
#    대입연산자(=) : 우측항을 좌측항에 대입
#    동등연산자(==)
#  - 변수명(전부다 소문자 사용)
name = "cherry"

# 4. 상수
#  - 변하지 않는 수
#  - 상수는 반드시 처음 대입한 값을 유지(변경 불가)
#  - 변수명(전부다 대문자 사용)
MAX_VALUE = 30

# 5. 명명규칙(Naming Rule)
#  * 변수, 함수, 클래스 등의 사용자 정의 이름에 사용
#  * 명확하고 알아보기 쉽게 정할것!
#  가. 영문 대소문자, 숫자, 특수문자(_)만 사용
#  나. 숫자로 시작할 수 없음
#    abc1(o), 1abc(x)
#  다. 영어 대소문자 구별
#    abc, ABC, Abc, aBC, AbC 모두 다른 변수로 인식
#  라. 예약어 사용 불가
#    - 프로그래밍 언어에서 미리 선점하여 사용중인 키워드 → 예약어
#    - print, for, if, while, else, class, and, return, ...

# 6. 네이밍 메서드
#  - 변수, 함수, 클래스 등의 사용자 정의 이름에 사용하는 기법
#  - 프로그래밍 언어별로 사용하는 Naming Method가 다름

#  가. snake_case: 소문자만 사용, 합성어는 _사용
#    ex) student_name
#  나. camelCase: 첫글자 소문자, 합성어 첫글자 대문자
#    ex) studentName
#  다. PascalCase: 첫글자 대문자, 합성어 첫글자 대문자
#    ex) StudentName
#  라. kebab-case: 소문자만 사용, 합성어는 -사용
#    ex) student-name

#               변수           함수            클래스
#  Python      snake         snake()           Pascal
#  Java, C     camel         camel()           Pascal

# 7. 동적 출력(Dynamic Print)
#  - print("Hello") → 정적 출력
#  - print("1학년 2반 홍길동") → 1, 2, 홍길동 변경 → 동적 출력

#  가. format() 사용
print("광주여자대학교 {}학년 {}입니다.".format(2, "이순신"))

#  나. f-string
grade = 2
name = "이순신"
print(f"광주여자대학교 {grade}학년 {name}입니다.")

# 8. 사칙연산
#  +   : 더하기
#  -   : 빼기
#  *   : 곱하기
#  /   : 나누기(5/2 → 2.5)
#  %   : 나누기(5/2 → 1)
#  //  : 나누기(5/2 → 2)
print(5//2)



