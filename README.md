# kwu_python_basic
광주여대 AI미디어콘텐츠학과 2학년 파이썬 기초 프로그래밍

## 1. README.md
- github repository(저장소)의 가이드 또는 설명서
- x.md → md: Markdown 언어

## 2. 개발환경 구축
### 2-1. 다운로드 및 설치
1. ANACONDA 다운로드 및 설치
  - 가상환경과 라이브러리 관리
  - 파이썬은 가상환경을 사용해서 개발환경을 세밀하게 나눔
    + 데이터 분석 가상환경
    + 인공지능 개발 가상환경 
  - 라이브러리는 미리 개발된 코드 묶음
    + 대부분의 기능들은 라이브러리로 구현되 있음(찾아서 사용)
    + 라이브러리는 반드시 다운로드 후 사용
    + matplotlib → 그래프 시각화 라이브러리
    + pytorch → 인공지능 개발 라이브러리
2. Visual Studio Code(VSCode) 다운로드 및 설치
  - IDE(통합개발환경) 도구
  - 개발할 때는 다양한 프로그램을 사용 → VSCode 연결 후 VSCode만 사용해서 개발
  - VSCode 최초 설치 후 확장팩(Extensions)을 설치해서 해당 언어 환경으로 세팅 필요!
    + Atom Material Icons
    + Atom Material Theme
    + Bracket Pair Color DLW
    + indent-rainbow
    + Image preview
    + Code Runner
    + Python
    + Python Extension Pack
  - 폰트 설정(글씨체: D2Coding, 글씨 크기) 
  - Tab 간격 설정
  - Mouse Wheel Zoom 설정
### 2-2. Github
  1. Github 회원가입
  2. Repository(저장소) 생성
  3. Repository 다운로드
  4. 압축 풀기
  5. VSCode 열기 → 압축 푼 Repository
### 2-3. 가상환경 설정
  1. venv → 특정 프로젝트 단위로 동작하는 가상환경
    + 프로젝트에 한정된 독립된 가상환경 생성(재사용 X)
    + 가벼움, 설치필요 없음
  2. anaconda → 사용자 정의 가상환경
    + 생성 된 가상환경을 재사용
    + 무거움, 설치필요!
  3. anaconda 가상환경 생성(anaconda prompt)
    - conda env list (가상환경 목록 출력) 
    - conda create -n dev python=3.11 (dev 가상환경 생성)
    - conda activate dev (dev 가상환경 접속)
    - pip list (가상환경에 설치된 라이브러리 목록)
    - pip install [라이브러리명] (가상환경에 라이브러리 설치)
  4. VSCode와 가상환경 연결
        
            



