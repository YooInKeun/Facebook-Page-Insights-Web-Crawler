import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from datetime import datetime
from parsed_data.models import fb_insight

def crawling_data(fb_page, fb_metric, fb_since, fb_until, fb_token):  # facebook API를 통해, data를 crawling하고 이를 dict에 저장(key : 날짜 & value : 값)

    dict = {}

    second_to_day = 86400  # 하루는 86400초, facebook의 날짜 데이터가 초 단위로 되어 있음

    while (fb_since <= fb_until):
        address = 'https://graph.facebook.com/v3.2/' + fb_page + '/insights?&pretty=0&fields=values&metric=' + fb_metric + \
                  '&since=' + str(fb_since) + '&until=' + str(
            fb_since) + '&access_token=' + fb_token  # access할 주소

        crawling_data = requests.get(address)  # address에 access해서, data crawling하기
        str_crawling = crawling_data.text  # crawling한 data text로 변환

        str_value = '"value"'
        str_comma = ','
        str_end_time = '"end_time"'

        f_v = str_crawling.find(str_value)  # value값 위치 알아내기
        f_c = str_crawling.find(str_comma)  # comma 위치 알아내기(value 값 추출을 위해)
        f_t = str_crawling.find(str_end_time)  # end_time값 위치 알아내기

        value = str_crawling[f_v + 8: f_c]  # value값 추출
        end_time = str_crawling[f_t + 12: f_t + 22]  # end_time값 추출 (참고 : 실제 날짜값은 end_time에서 하루 빼기)

        dict[fb_since] = value  # key 값은 날짜, value는 값으로 하는 dict에 저장

        extract_year = end_time[0:4]  # facebook 날짜 데이터에서, 년도가 맞지 않아 년도만 따로 추출해놓기

        fb_since += second_to_day  # 하루 더하기(다음 날 값 구하기 위해)

        print('page name : ' + fb_page)
        print(fb_metric + ': ' + value)  # test
        print('종료 날짜 : ' + end_time + ' 08시 00분')  # test
        print('\n')

    return dict

if __name__=='__main__':

    second_to_day = 86400  # 하루는 86400초

    now = datetime.now()  # 현재 날짜 (나중에 페이지 열 때마다 now 함수 적용되게끔 해야할 필요가 있음)
    elapsed_day = datetime(now.year, now.month, now.day) - datetime(2019, 1, 21)  # 1월 21일부터 흐른 시간 계산
    str_elapsed_day = str(elapsed_day)

    blank = ' '

    f_b = str_elapsed_day.find(blank)

    cal_day = str_elapsed_day[0: f_b]  # day 값 추출

    estimate_day = input('최근 몇 일 동안의 데이터를 저장하시겠습니까? ')  # 저장할 데이터 기간(단위 : 1일)

    # 1522501931348511 : 현대건설배구단
    # 740318106321385 : KDB Hi뱅킹
    # 611418572386248 : 삼성화재멤버십
    # 483308331873326 : 맘쏙케어22
    # 1559207541044807 : 세계한인벤처네트워크 - INKE
    # 1680512022212737 : 홈씨씨인테리어

    fb_page = ['1522501931348511', '740318106321385', '611418572386248',     '483308331873326', '1559207541044807', '1680512022212737']

    # page_total_actions : 페이지 행동
    # page_views_total : 페이지 조회
    # page_fan_adds : 페이지 좋아요
    # page_impressions_organic : 게시물 도달
    # page_post_engagement : 게시물 참여
    # page_video_views : 동영상 조회

    fb_metric = ['page_total_actions', 'page_views_total', 'page_fan_adds', 'page_impressions_organic', 'page_post_engagements', 'page_video_views']
    fb_until = 1548144000 + int(cal_day) * second_to_day  # 금일 날짜로 계산(날마다 갱신), 날짜는 초 단위 (1548144000은 1월 21일을 나타냄)
    fb_since = fb_until - second_to_day * int(estimate_day)

    # fb_token index는 fb_page와 동일

    fb_token = [
        '~~~~'
        ]

    for i in range(0, len(fb_page)):

        for j in range(0, len(fb_metric)):

            insights_data_dict = crawling_data(fb_page[i], fb_metric[j], fb_since, fb_until, fb_token[i])

            for d, v in insights_data_dict.items():
                fb_insight(fb_page=fb_page[i], fb_metric=fb_metric[j], fb_value = v, fb_date = d, fb_token=fb_token[i]).save()