import requests
import datetime

# facebook page의 인사이트에 있는 "페이지 좋아요" 값을 날짜별로 크롤링해보자!
# facebook for developers에서 access token 발급 받기

fb_token = '~~~~'

fb_date = '1548144000' # date는 초 단위, date : 2019-01-21 00시 ~ 2019-01-21 24시(1일 : 86,400초)
fb_metric = 'page_fan_adds' # metric=page_fan_adds : page 좋아요

fb_int_date = int(fb_date) # 날짜값 int로 형변환
second_day = 86400 # 하루는 86400초

day_input = int(input("날짜 일수를 입력하세요 : " ))

start_date = (fb_int_date)-(second_day * day_input)
end_date = (fb_int_date)-(second_day * day_input)

dict_fan_adds = { } # dictionary 선언

while(start_date <= fb_int_date):

    str_start_date = str(start_date) # 날짜값 연산 후, string으로 형 변환
    str_end_date = str(end_date)

    address = 'https://graph.facebook.com/v3.2/1522501931348511/insights?fields=values&metric=' + fb_metric + '&until=' + str_start_date + '&since=' + str_end_date + '&pretty=0' + '&access_token=' + fb_token # access할 주소

    crawling_data = requests.get(address) # address에 access해서, data crawling하기

    str_crawling = crawling_data.text # crawling한 data를 text로 변환

    str_value = '"value"'
    str_comma = ','
    str_end_time = '"end_time"'

    f_v = str_crawling.find(str_value) # value값 추출, 여기서 value값은 좋아요 수
    f_c = str_crawling.find(str_comma) # 콤마 위치 알아내기(value 값 추출을 위해)
    f_t = str_crawling.find(str_end_time) # end_time값 추출, 날짜

    value = str_crawling[f_v + 8: f_c]
    end_time = str_crawling[f_t + 12: f_t + 22]

    dict_fan_adds[start_date] = value

    extract_year = end_time[0:4]

    print('좋아요 수(유기적 좋아요 수) : ' + value)
    print('종료 날짜 : ' + end_time + ' 08시 00분')
    print('\n')

    start_date += second_day
    end_date += second_day

print(dict_fan_adds) # dict 값 test

# facebook 초 데이터를 날짜로 변환

mydelta = datetime.timedelta(seconds=fb_int_date)
mytime = datetime.datetime.min + mydelta
str_mytime = str(mytime)
end_mytime = extract_year + str_mytime[4:10]  # 년도가 안맞아서, end_time 데이터에서 추출한 year 사용
print(end_mytime)