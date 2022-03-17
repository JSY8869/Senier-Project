import datetime  # 날짜시간 모듈
from datetime import date, datetime, timedelta  # 현재 날짜 외의 날짜 구하기 위한 모듈
import requests
import json


def how_weather():
    key = 'a3efa2941fb3fcf4f3877cc063439f9b'
    send_url = 'http://api.ipstack.com/check?access_key=' + key
    r = requests.get(send_url)
    j = json.loads(r.text)

    # 경도
    ny = int(j['longitude'])

    # 위도
    nx = int(j['latitude'])

    # 기상청_동네 예보 조회 서비스 api 데이터 url 주소
    vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
    # 실황정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 조회 조건으로
    # 자료구분코드, 실황값, 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능

    # 발급 받은 인증키 (Encoding Key)
    service_key = "zaLj9eycWY9pgOI72vYs6W8iFk1lag1uWZmjjvec69bhR48+1DatOVR50ZhB3oiS2wwqLSaRevnFHZENdSPRhg=="

    now = datetime.now()

    # 오늘
    today = datetime.today()  # 현재 지역 날짜 반환
    today_date = today.strftime("%Y%m%d")  # 오늘의 날짜 (연도/월/일 반환)

    # 어제
    yesterday = date.today() - timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y%m%d')

    # 1일 총 8번 데이터가 업데이트 된다.(0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300)
    # 현재 api를 가져오려는 시점의 이전 시각에 업데이트된 데이터를 base_time, base_date로 설정
    if now.hour < 2 or (now.hour == 2 and now.minute <= 10):  # 0시~2시 10분 사이
        base_date = yesterday_date  # 구하고자 하는 날짜가 어제의 날짜
        base_time = "2300"
        voice_time = "오후 11시"
    elif now.hour < 5 or (now.hour == 5 and now.minute <= 10):  # 2시 11분~5시 10분 사이
        base_date = today_date
        voice_time = "오전 2시"
        base_time = "0200"
    elif now.hour < 8 or (now.hour == 8 and now.minute <= 10):  # 5시 11분~8시 10분 사이
        base_date = today_date
        base_time = "0500"
        voice_time = "오전 5시"
    elif now.hour <= 11 or now.minute <= 10:  # 8시 11분~11시 10분 사이
        base_date = today_date
        base_time = "0800"
        voice_time = "오전 8시"
    elif now.hour < 14 or (now.hour == 14 and now.minute <= 10):  # 11시 11분~14시 10분 사이
        base_date = today_date
        base_time = "1100"
        voice_time = "오전 11시"
    elif now.hour < 17 or (now.hour == 17 and now.minute <= 10):  # 14시 11분~17시 10분 사이
        base_date = today_date
        base_time = "1400"
        voice_time = "오후 2시"
    elif now.hour < 20 or (now.hour == 20 and now.minute <= 10):  # 17시 11분~20시 10분 사이
        base_date = today_date
        base_time = "1700"
        voice_time = "오후 5시"
    elif now.hour < 23 or (now.hour == 23 and now.minute <= 10):  # 20시 11분~23시 10분 사이
        base_date = today_date
        base_time = "2000"
        voice_time = "오후 8시"
    else:  # 23시 11분~23시 59분
        base_date = today_date
        base_time = "2300"
        voice_time = "오후 11시"
    pageNo = "1"
    numOfRows = "100"
    params ={'serviceKey' : service_key, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'dataType' : 'JSON', 'base_date' : base_date, 'base_time' : base_time, 'nx' : nx, 'ny' : ny }

    # 값 요청 (웹 브라우저 서버에서 요청 - url주소와 )
    try:
        res = requests.get(vilage_weather_url, params)
        items = res.json().get('response').get('body').get('items')
    except:
        return("날씨 불러오기 실패 (wifi 설정을 먼저 해주세요)")
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

    state = data['weather']['state']

    if state == '비':
        return("\n비가 와요. 우산을 꼭 챙겨주세요!", 0)
    elif state == '비/눈':
        return("\n비 또는 눈이 와요. 쌀쌀하니 따뜻하게 입어요! 우산도 꼭 챙겨주세요!", 1)
    elif state == '눈':
        return("\n눈이 와요. 장갑을 꼭 챙기세요!", 2)
    elif state == '소나기':
        return("\n소나기가 와요. 비가 언제 올지 모르니, 우산을 꼭 챙겨주세요!", 3)
    else:
        return("\n날씨가 좋네요. 좋은 하루 보내세요!", 4)