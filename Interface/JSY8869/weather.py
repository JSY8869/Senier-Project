import requests  # HTTP 요청을 보내는 모듈
import json  # json 파일 파싱하여 데이터 읽는 모듈
import datetime  # 날짜시간 모듈
from datetime import date, datetime, timedelta  # 현재 날짜 외의 날짜 구하기 위한 모듈



def how_weather(nx,ny):
    # 기상청_동네 예보 조회 서비스 api 데이터 url 주소
    vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
    # 실황정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 조회 조건으로
    # 자료구분코드, 실황값, 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능

    # 발급 받은 인증키 (Encoding Key)
    service_key = "zaLj9eycWY9pgOI72vYs6W8iFk1lag1uWZmjjvec69bhR48+1DatOVR50ZhB3oiS2wwqLSaRevnFHZENdSPRhg=="

    now = datetime.now()
    print("지금은", now.year, "년", now.month, "월", now.day, "일", now.hour, "시", now.minute, "분", now.second, "초입니다.")

    # 오늘
    today = datetime.today()  # 현재 지역 날짜 반환
    today_date = today.strftime("%Y%m%d")  # 오늘의 날짜 (연도/월/일 반환)
    print('오늘의 날짜는', today_date)

    # 어제
    yesterday = date.today() - timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y%m%d')
    print('어제의 날짜는', yesterday_date)

    # 1일 총 8번 데이터가 업데이트 된다.(0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300)
    # 현재 api를 가져오려는 시점의 이전 시각에 업데이트된 데이터를 base_time, base_date로 설정
    if now.hour < 2 or (now.hour == 2 and now.minute <= 10):  # 0시~2시 10분 사이
        base_date = yesterday_date  # 구하고자 하는 날짜가 어제의 날짜
        base_time = "2300"
    elif now.hour < 5 or (now.hour == 5 and now.minute <= 10):  # 2시 11분~5시 10분 사이
        base_date = today_date
        base_time = "0200"
    elif now.hour < 8 or (now.hour == 8 and now.minute <= 10):  # 5시 11분~8시 10분 사이
        base_date = today_date
        base_time = "0500"
    elif now.hour <= 11 or now.minute <= 10:  # 8시 11분~11시 10분 사이
        base_date = today_date
        base_time = "0800"
    elif now.hour < 14 or (now.hour == 14 and now.minute <= 10):  # 11시 11분~14시 10분 사이
        base_date = today_date
        base_time = "1100"
    elif now.hour < 17 or (now.hour == 17 and now.minute <= 10):  # 14시 11분~17시 10분 사이
        base_date = today_date
        base_time = "1400"
    elif now.hour < 20 or (now.hour == 20 and now.minute <= 10):  # 17시 11분~20시 10분 사이
        base_date = today_date
        base_time = "1700"
    elif now.hour < 23 or (now.hour == 23 and now.minute <= 10):  # 20시 11분~23시 10분 사이
        base_date = today_date
        base_time = "2000"
    else:  # 23시 11분~23시 59분
        base_date = today_date
        base_time = "2300"
    pageNo = "1"
    numOfRows = "100"
    params ={'serviceKey' : service_key, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'dataType' : 'JSON', 'base_date' : base_date, 'base_time' : base_time, 'nx' : nx, 'ny' : ny }

    # 값 요청 (웹 브라우저 서버에서 요청 - url주소와 )
    res = requests.get(vilage_weather_url, params)
    items = res.json().get('response').get('body').get('items')

    data = dict()
    data['date'] = base_date

    weather_data = dict()
    for item in items['item']:
        # 기온
        if item['category'] == 'T3H':
            weather_data['tmp'] = item['fcstValue']

        # 기상상태
        if item['category'] == 'PTY':

            weather_code = item['fcstValue']

            if weather_code == '1':
                weather_state = '비'
            elif weather_code == '2':
                weather_state = '비/눈'
            elif weather_code == '3':
                weather_state = '눈'
            elif weather_code == '4':
                weather_state = '소나기'
            else:
                weather_state = '없음'

            weather_data['code'] = weather_code
            weather_data['state'] = weather_state

    data['weather'] = weather_data

    print()

    state = data['weather']['state']

    day = (data['date'][0:4] + "년" + data['date'][4:6] + "월" + data['date'][6:8] + "일" + base_time + "시의 날씨 데이터입니다.")

    if state == '비':
        return(day + "\n비가 와요. 우산을 꼭 챙겨주세요!")
    elif state == '비/눈':
        return(day + "\n비 또는 눈이 와요. 쌀쌀하니 따뜻하게 입어요! 우산도 꼭 챙겨주세요!")
    elif state == '눈':
        return(day + "\n눈이 와요. 장갑을 꼭 챙기세요!")
    elif state == '소나기':
        return(day + "\n소나기가 와요. 비가 언제 올지 모르니, 우산을 꼭 챙겨주세요!")
    else:
        return(day + "\n날씨가 좋네요 :)")