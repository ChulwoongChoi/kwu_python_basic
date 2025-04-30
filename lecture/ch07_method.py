# 함수(Method, Function)
#  - 어떤 일을 수행하는 코드 묶음
#  - 반복적으로 동작해야하는 일!

# 함수 개발 가이드라인
#  1. 함수 이름 및 내용
#   - 함수 이름에 함수의 역할과 의도 명확히 드러낼 것!
#   - 함수 내용은 가능하면 짧게 작성(Code Line 줄이기)

# 사칙연산 계산기 → 사칙연산 함수() X
#               → 덧셈(), 뺄셈(), 곱셈(), 나눗셈() O             

#  2. 함수의 역할
#   - 하나의 함수에 유사한 역할을 하는 코드만 포함
#   - 하나의 함수는 한가지 기능만 명확히 정의

#  3. 함수를 만들어야 하는 경우
#   - 공통적으로 사용되는 코드는 함수로 생성
#   - 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수 생성

#  4. 함수의 종류
#   가. 내장 함수(Built-in function)
#    - Python에서 기본적으로 제공하는 함수
#   나. 외장 함수(Library or Module)
#    - 다른 개발자가 개발한 코드 묶음
#   다. 사용자 정의 함수
#    - 직접 만들어서 사용하는 함수

#  5. 함수 이름 규칙
#   - snake_case 사용

#  6. 함수 정의
#   가. 기본 함수 문법
```python
    def 함수명(parameter1, parameter2, ...):
        실행문
        return 반환값
```
#   나. 함수 정의시 "def" 키워드 사용(define)
#   다. 인자(argument or parameter) 정의: 함수 입력값
#   라. return: 함수 종료 의미
#   마. return 반환값: 함수 종료 + 호출문으로 반환값 전달(tuple)
#   바. 함수 종료: 1.return, 2. 블록문 끝
#   사. parameter와 return은 생략가능(입력과 반환이 없는 함수도 존재)

# 1. 함수 정의문(생성)
def sum_two_values(x, y):  # x, y -> parameter(매개변수)
    n = x+y
    print(n)
    return n  # n -> 리턴값(반환값)

# 2. 함수 호출문(사용)
result = sum_two_values(5, 10)  # 5, 10 -> argument(인자)  
print(result)

# 3. 매개변수 or 인자
#  - 함수에 전달되는 입력값(input)
#  - 함수 정의문과 호출문의 parameter 갯수가 동일해야함
#  - parameter로는 기본자료형 + 컬렉션 프레임워크 + 객체 등 가능
#  - parameter는 정의된 순서대로 전달됨

# 4. Type Hint
#  - 입력매개변수와 반환값의 타입을 힌트로 미리 적기
#  - 안적어도 실행하는데 문제 없음(가독성을 위함)
def sum(a, b):
    return a+b
def sum(a: int, b: int) -> int:
    return a+b

# 5. 변수의 범위
#  - 변수가 참조 가능한 코드상의 범위를 명시
#  - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
#  - 이렇게 특정 코드블록에 선언된 변수를 지역변수
#  - 반대로 가장 상단에 정의되어 프로그램 종료 전까지
#    유지되는 변수를 전역변수
#  - 같은 이름의 지역변수와 전역변수 존재하는 경우
#    가까운(지역변수) 우선순위가 높음
num1 = 10  # 전역
num2 = 20  # 전역

def test(num1, num2):
    print(num1, num2)
    return
test(30, 40)
print(num1, num2)

