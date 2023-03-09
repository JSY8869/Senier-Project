# U.S.A.N
## [한이음](https://www.hanium.or.kr/portal/hanium/mainOverview.do)
- 이 repository는 2022년 한이음 공모전을 준비하기 위한 repository입니다.
## 팀원 소개
### 정세영
- github-name : [JSY8869](https://github.com/JSY8869)
- 역할 : 팀장, 총괄
- 사용 가능 언어 : JAVA, C, C++, Python, Kotlin, JPA, Spring
- 개발환경 : VSCODE, Visual Studio, Intellij IDEA
- 희망 진로 : Backend Developer
### 이수혁
- 역할 : 팀원
- 사용 가능 언어 : visual basic, c언어, c++ , python 
- 개발환경 : vsocde,visual studio
- 희망 진로 : 반도체공정 엔지니어
### 조윤설
- 역할 : 팀원
- 사용 가능 언어 : python, C, MATLAB
- 개발환경 : visual studio, pycharm
- 희망 진로 : 방송기술직, 통신연구원
### 장중기
- 역할 : 팀원
- 사용 가능 언어 : Python, C
- 개발환경 : visual studio
- 희망 진로 : 마게팅, 영상 직무 (미정)
## 목표
- 2022 한이음 공모전 대상
- 4학년 1학기 전공 캡스톤디자인 A+
# [인터페이스 소스](https://github.com/JSY8869/Senier-Project/tree/Interface_Develop/Interface)
### main.py
- 그냥 main 파일
- main_page.py의 PyShine_THREADS_APP 클래스를 호출하며 프로그램 시작
### weather.py
날씨를 조회하는 코드가 들어있는 파일이다.
1. [ipstack](https://ipstack.com/) 사이트에서 제공하는 api를 통해 현재 ip 주소로 위도와 경도를 불러온다.
2. 불러온 위도와 경도를 IpToXY 파일의 코드를 이용하여 격자 주소로 변경한다.
3. [기상청 단기예보 api](https://www.data.go.kr/data/15084084/openapi.do)를 이용하여 격자 주소와 현재 시간에 가장 가까운 단기 예보를 불러온다.
4. 현재 날씨에 해당하는 text를 반환한다.
### IpToXY.py
- 위도와 경도를 격자 주소로 바꿔주는 코드
### main_page.py
가장 중요한 파일이며 각종 기능 구현 및 디자인, 각종 함수를 호출하는 main 기능 파일
- start 버튼과 stop 버튼의 생성 및 디자인 설정, 기능 구현
- ThreadClass를 이용하여 progress_bar_count 함수에서 progress bar의 값 설정
- weather.py 파일을 호출하여 현재 날씨에 해당하는 text를 불러와 textEdit창에 text 출력 및 날씨 호출 버튼의 디자인 변경
### ThreadClass.py
- 쓰레드를 생성 및 1부터 101까지 count 하는 기능을 구현한 파일
- time.sleep(0.01) 값을 변경하여 작동 시간을 설정 가능
### image 폴더
- 디자인에 사용되는 각종 이미지가 저장되어 있는 폴더
### ui 폴더
- qt designer를 이용하여 디자인한 ui파일이 저장되어 있는 폴더
# 기능 설명
### 날씨 조회
- 사용자의 ip주소를 조회하여 해당 위치의 가장 가까운 시간의 일기예보를 불러와 날씨 정보를 제공함
### 우산 건조 시작 및 정지 버튼
- 우산 건조를 시작하고, 중간에 정지할 수 있는 버튼
- progress bar를 통해 진행도를 표현함
### 신발 건조 시작 및 정지 버튼
- 신발 건조를 시작하고, 중간에 정지할 수 있는 버튼
- progress bar를 통해 진행도를 표현함
# 실행 환경
### python 3.9.0
```
brotlipy           0.7.0
certifi            2021.5.30
cffi               1.14.6
charset-normalizer 2.0.4
cryptography       35.0.0
idna               3.3
pip                21.2.2
pycparser          2.21
pyOpenSSL          22.0.0
PyQt5              5.15.6
PyQt5-Qt5          5.15.2
PyQt5-sip          12.9.1
PySocks            1.7.1
requests           2.27.1
setuptools         58.0.4
urllib3            1.26.8
wheel              0.37.1
win-inet-pton      1.1.0
wincertstore       0.2
```
글씨체 - 한초롬돋움 확장
### 사진
![눈](https://user-images.githubusercontent.com/65009713/165900732-a0c239cd-f434-409e-8002-86a52eeef282.jpg)
![소나기](https://user-images.githubusercontent.com/65009713/165900734-60015b21-3541-45da-a3c1-4f0607f12f02.jpg)
![맑음](https://user-images.githubusercontent.com/65009713/165900737-bf949381-5816-44c9-98c4-90b52da30e18.jpg)
![비](https://user-images.githubusercontent.com/65009713/165900738-819ded3f-644d-46d9-85b0-5c65ee0db4b2.jpg)
![눈비](https://user-images.githubusercontent.com/65009713/165900739-598b8709-30a8-4f37-b73d-4b76bc298052.jpg)
# [아두이노 소스](https://github.com/JSY8869/Senier-Project/tree/Interface_Develop/arduino)
### motor
- 우산 건조시 라즈베리파이로부터 신호를 받아 RC서보모터를 회전시키는 코드
### shoe
- 신발 건조시 라즈베리파이로부터 신호를 받아 팬을 작동시키는 코드
### umbrella1
- 우산 건조시 라즈베리파이로부터 신호를 받아 팬을 회전시키는 코드

# 개발 도구
- Pycharm
- qt designer
- arduino

# 예상되는 오류
- 라즈베리파이의 프로그램 처리 속도가 느리기 때문에 버튼을 너무 빠르게 반복해서 눌렀을 경우 튕김 현상
# Manual
- 모든 개발은 `Develop` 폴더에서 진행한다.
  - 각자 작업은 닉네임 폴더 만들어서 할 것(ex: JSY8869)
  - `README` 파일 활용하여 본인의 폴더 및 코드에 대한 설명 적어 둘 것
- `branch` 작성 양식
  - `Develop/[닉네임]` 으로 본인의 개발용 `branch`사용
  - 커밋 할 때 불필요한 파일 제외하고 소스 코드만 커밋 할 수 있도록 할 것
  - 특별한 기능 혹은 업데이트 시 `Feature/[닉네임]/[해당 기능 설명]` `branch`를 만들어 작업 후 `PR`을 통해 공유하고 `Develop/[닉네임]` 에 커밋한다.
  - `PR`을 통해 질문하고, 이를 해결한 후 커밋하는 방법도 있다.
- 진행 방식
  - 질문이 있을 경우 `Issue`를 최대한 활용할 것
  - 새로 알게 된 정보나 공유하고 싶은 내용을 `Wiki`에 최대한 정리할 것
  - 매 주 각자 `Plan`을 세우고 이를 수행할 것
  - 의논하고 싶은 주제나 정보는 `Issue`를 활용
  - 매 주 1번 수요일 `meeting`을 가질 것
  - `Issue`나 `PR`은 72시간 내에 답을 줄 것
  - `Issue`를 읽고 확인 및 이해가 된 경우 이모티콘을 남긴다.
  - 매주 meeting이 끝난 후 48시간 내에 meeting issue에 review를 댓글로 남긴다.
- 아이디어 회의
  - 매일 오후 10시~11시 Google meet을 이용하여 아이디어 구상 시간을 가진다.
  - 1시간의 meeting이 종료된 후 `issue`에 `review`를 통해 각자의 생각과 활동을 공유한다.
