import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from datetime import datetime
from datetime import timedelta
from parsed_data.models import fb_insight

def crawling_data(fb_page, fb_metric, fb_since, fb_until, fb_token):  # facebook API를 통해, data를 crawling하고 이를 dict에 저장(key : 날짜 & value : 값)

    dict = {}

    second_to_day = 86400  # 하루는 86400초, facebook의 날짜 데이터가 초 단위로 되어 있음

    while (fb_since <= fb_until):
        address = 'https://graph.facebook.com/v3.2/' + fb_page + '/insights?&pretty=0&fields=values&metric=' + fb_metric + \
                  '&since=' + str(fb_since) + '&until=' + str(fb_since) + '&access_token=' + fb_token  # access할 주소

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

        extract_year = end_time[0:4]  # facebook 날짜 데이터에서, 년도가 맞지 않아 년도만 따로 추출해놓기

        end_time = datetime(int(end_time[0:4]),int(end_time[5:7]),int(end_time[8:10]))
        end_time -= timedelta(days=1)
        end_time = str(end_time)
        end_time = end_time[0:10]

        dict[end_time] = value  # key 값은 날짜, value는 값으로 하는 dict에 저장

        fb_since += second_to_day  # 하루 더하기(다음 날 값 구하기 위해)

        print('page name : ' + fb_page)
        print(fb_metric + ': ' + value)  # test
        print('종료 날짜 : ' + end_time + ' 08시 00분')  # test
        print('\n')

    return dict

def making_data(fb_page, fb_metric1, fb_metric2, fb_since, fb_until, fb_token):  # 페이지 순 좋아요 값은 metric 값이 존재하지 않으므로 따로 연산해서 저장하기

    dict1 = {}
    dict2 = {}
    pure_fan_dict = {}

    second_to_day = 86400  # 하루는 86400초, facebook의 날짜 데이터가 초 단위로 되어 있음

    while (fb_since <= fb_until):

        address = 'https://graph.facebook.com/v3.2/' + fb_page + '/insights?&pretty=0&fields=values&metric=' + fb_metric1 + \
                  '&since=' + str(fb_since) + '&until=' + str(fb_since) + '&access_token=' + fb_token  # access할 주소

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

        extract_year = end_time[0:4]  # facebook 날짜 데이터에서, 년도가 맞지 않아 년도만 따로 추출해놓기

        end_time = datetime(int(end_time[0:4]), int(end_time[5:7]), int(end_time[8:10]))
        end_time -= timedelta(days=1)
        end_time = str(end_time)
        end_time = end_time[0:10]

        dict1[end_time] = value  # key 값은 날짜, value는 값으로 하는 dict에 저장

        ################################################################################################################

        address = 'https://graph.facebook.com/v3.2/' + fb_page + '/insights?&pretty=0&fields=values&metric=' + fb_metric2 + \
                  '&since=' + str(fb_since) + '&until=' + str(fb_since) + '&access_token=' + fb_token  # access할 주소

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

        extract_year = end_time[0:4]  # facebook 날짜 데이터에서, 년도가 맞지 않아 년도만 따로 추출해놓기

        end_time = datetime(int(end_time[0:4]), int(end_time[5:7]), int(end_time[8:10]))
        end_time -= timedelta(days=1)
        end_time = str(end_time)
        end_time = end_time[0:10]

        dict2[end_time] = value  # key 값은 날짜, value는 값으로 하는 dict에 저장

        tmp = int(dict1[end_time]) - int(dict2[end_time])
        pure_fan_dict[end_time] = str(tmp)

        fb_since += second_to_day  # 하루 더하기(다음 날 값 구하기 위해)

        print('page name : ' + fb_page)
        print('page_fan_pure_adds_unique' + ': ' + value)  # test
        print('종료 날짜 : ' + end_time + ' 08시 00분')  # test
        print('\n')

    return pure_fan_dict

if __name__=='__main__':

    second_to_day = 86400  # 하루는 86400초

    now = datetime.now()  # 현재 날짜 (나중에 페이지 열 때마다 now 함수 적용되게끔 해야할 필요가 있음)
    elapsed_day = datetime(now.year, now.month, now.day) - datetime(2019, 1, 21)  # 1월 21일부터 흐른 시간 계산
    str_elapsed_day = str(elapsed_day)

    blank = ' '

    f_b = str_elapsed_day.find(blank)

    cal_day = str_elapsed_day[0: f_b]  # day 값 추출

    estimate_day = input('최근 몇 일 동안의 데이터를 저장하시겠습니까? ')  # 저장할 데이터 기간(단위 : 1일)

    # 133755520063453 : 토이 인터랙티브
    # 570813366394251 : TOY interactive
    # 740318106321385 : KDB Hi 뱅킹

    fb_page = ['133755520063453', '570813366394251', '740318106321385']

    # page_fan_adds_unique : 페이지 유기적 좋아요
    # page_fan_removes_unique : 페이지 좋아요 취소
    # page_fan_pure_adds_unique : 페이지 순 좋아요 (page_fan_adds_unique) - (page_fan_removes_unique) 값으로 직접 만들기

    # page_actions_post_reactions_like_total : 페이지 총 게시물 좋아요
    # page_impressions_organic : 게시물 도달
    # page_post_engagements : 게시물 참여

    fb_metric = ['page_fan_adds_unique', 'page_fan_removes_unique', 'page_fan_pure_adds_unique', 'page_actions_post_reactions_like_total', 'page_impressions_organic', 'page_post_engagements']
    fb_until = 1548144000 + int(cal_day) * second_to_day  # 금일 날짜로 계산(날마다 갱신), 날짜는 초 단위 (1548144000은 1월 21일을 나타냄)
    fb_since = fb_until - second_to_day * int(estimate_day)

    # fb_token index는 fb_page와 동일

    fb_token = [

        ]

    for i in range(0, len(fb_page)):

        for j in range(0, len(fb_metric)):

            if fb_metric[j] == 'page_fan_pure_adds_unique': # 페이지 순 좋아요 저장

                insights_data_dict = making_data(fb_page[i], fb_metric[0], fb_metric[1], fb_since, fb_until, fb_token[i])

            else :
                insights_data_dict = crawling_data(fb_page[i], fb_metric[j], fb_since, fb_until, fb_token[i])

            for e, v in insights_data_dict.items():
                fb_insight(fb_page=fb_page[i], fb_metric=fb_metric[j], fb_value = v, fb_date = e, fb_token=fb_token[i]).save()

