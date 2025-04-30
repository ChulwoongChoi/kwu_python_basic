# 라이브러리(Library) >= 패키지(Package) >= 모듈(Module)
# 
# 라이브러리: 여러 패키지와 모듈의 묶음
# 패키지: 특정 기능과 관련한 여러 모듈의 묶음
# 모듈: 이미 작성된 프로그램(일반적으로 한 파일(.py)을 의미)

# 1. 라이브러리 다운로드 및 설치
#   - pip install [라이브러리명]
# 2. 호출(import)
#  가. import requests
#   - requests 라이브러리 모든 코드 호출
#   - requests.get()
#  나. from requests import get
#   - requests 라이브러리에서 get 모듈만 호출
#   - get()
#  다. as(Alias: 별칭)
#   - import requests as req
#   - req.get()