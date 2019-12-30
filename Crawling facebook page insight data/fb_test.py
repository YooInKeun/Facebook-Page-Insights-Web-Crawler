import requests

# facebook page의 인사이트에 있는 "페이지 좋아요" 값을 날짜별로 크롤링해보자!

# facebook for developers에서 access token 발급 받기

token = ''

date = '1547884800' # date는 초 단위, date : 2019-01-18 ~ 2019-01-19(1일 : 86,400초)
metric = 'page_fan_adds' # metric=page_fan_adds : page 좋아요

int_date = int(date) # 날짜값 int로 형변환
day = 86400 # 하루는 86400초

start_date = int_date-day*30 # 한 달(30일)을 측정해보자

while(start_date < int_date):
    start_date +=day

    str_date = str(start_date) # 날짜값 연산 후, string으로 형 변환
    address = 'https://graph.facebook.com/v3.2/1522501931348511/insights?fields=values&metric=' + metric + '&until=' + str_date + '&since=' + str_date + '&pretty=0' + '&access_token=' + token # access할 주소

    crawling_data = requests.get(address)  # address에 access해서, data crawling하기

    str_crawling = crawling_data.text  # crawling한 data text로 변환

    #print(str_crawling)  # test

    str_value = '"value"'
    str_comma = ','
    str_end_time = '"end_time"'

    f_v = str_crawling.find(str_value)  # value값 추출, 여기서 value값은 좋아요 수
    f_c = str_crawling.find(str_comma) # 콤마 위치 알아내기(value 값 추출을 위해)
    f_t = str_crawling.find(str_end_time)  # end_time값 추출, 날짜

    value = str_crawling[f_v + 8: f_c]
    end_time = str_crawling[f_t + 12: f_t + 22]

    print('좋아요 수 : ' + value)
    print('종료 날짜 : ' + end_time)
    print('\n')