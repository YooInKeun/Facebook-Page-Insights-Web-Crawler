import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from datetime import datetime
from django.shortcuts import render, render_to_response
from parsed_data.models import fb_insight
from parsed_data import parser

def window(request):

    fb_insight_list = fb_insight.objects.values('fb_page', 'fb_metric', 'fb_date', 'fb_value').order_by('fb_date').distinct()
    fb_insight_page_name = fb_insight.objects.values('fb_page', 'fb_page_name').distinct()

    page_name = '페이지 이름'
    page_id = '페이지 ID'
    date_from = '시작 날짜'
    date_to = '종료 날짜'

    if request.method == "POST":
        temp = request.POST
        str_request = str(temp)

        print(str_request)

        str_pageSelect = 'pageSelect'
        str_sharp = '#'
        str_bracket = '>'

        s1 = str_request.find(str_pageSelect)
        s2 = str_request.find(str_sharp)
        s3 = str_request.find(str_bracket)

        page_name = str_request[s1 + 15 : s2]
        page_id = str_request[s2 + 1 : s3 - 3]

        print(page_name)
        print(page_id)

        str_from = 'from'
        str_to = "'to'"

        f1 = str_request.find(str_from)
        t1 = str_request.find(str_to)

        date_from = str_request[f1+9 : f1+19]
        date_to = str_request[t1+8 : t1+18]

        print(date_from)
        print(date_to)

        if(date_from == "'], 'to':" or date_to == "'], 'pageS" ):

            date_from = "시작 날짜"
            date_to = "종료 날짜"

    data = {'lists' : fb_insight_list, 'name': page_name, 'id' : page_id, 'from': date_from, 'to': date_to, 'name_sets' : fb_insight_page_name}

    return render(request, 'parsed_data/window.html', data)

def data_collection(request):

    fb_insight_page_name = fb_insight.objects.values('fb_page','fb_page_name','fb_token').distinct()

    data = {'name_sets' :fb_insight_page_name}

    if request.method == "POST": # form post
        temp = request.POST
        str_request = str(temp)

        if str_request.find("'page_id'") == -1 and str_request.find("'page_remove_select'") == -1: # 데이터 수집하기 실행시

            print(str_request)

            fb_array = "'fb_array'"
            days = "'days'"
            str_bracket = '>'

            pos_fb_array = str_request.find(fb_array)
            pos_days = str_request.find(days)
            pos_bracket = str_request.find(str_bracket)

            str_name = str_request[pos_fb_array + 14: pos_days - 4]
            str_days = str_request[pos_days +10 : pos_bracket - 3]

            fb_string = str_name.split("#")

            arr_size = len(fb_string)

            page_num = (arr_size-1)/4

            loop_cnt = 0
            cnt = 0

            fb_page_name = []
            fb_page = []
            fb_token = []
            fb_days = str_days

            print(fb_string)

            while(loop_cnt<page_num) :

                print(cnt)
                fb_page_name.append(fb_string[1 + cnt*4])
                fb_page.append(fb_string[2 + cnt*4])
                fb_token.append(fb_string[3 + cnt*4])

                cnt+=1
                loop_cnt+=1

            print(fb_page_name)
            print(fb_page)
            print(fb_token)

            second_to_day = 86400  # 하루는 86400초
            now = datetime.now()  # 현재 날짜
            elapsed_day = datetime(now.year, now.month, now.day) - datetime(2019, 1, 21)  # 1월 21일부터 흐른 시간 계산
            str_elapsed_day = str(elapsed_day)

            blank = ' '

            f_b = str_elapsed_day.find(blank)

            cal_day = str_elapsed_day[0: f_b]  # day 값 추출

            # page_fan_adds_unique : 페이지 유기적 좋아요
            # page_fan_removes_unique : 페이지 좋아요 취소
            # page_fan_pure_adds_unique : 페이지 순 좋아요 (page_fan_adds_unique) - (page_fan_removes_unique) 값으로 직접 만들기

            # page_actions_post_reactions_like_total : 페이지 총 게시물 좋아요
            # page_impressions_organic_unique : 게시물 유기적 도달
            # page_post_engagements : 게시물 참여

            fb_metric = ['page_fan_adds_unique', 'page_fan_removes_unique', 'page_fan_pure_adds_unique','page_actions_post_reactions_like_total', 'page_impressions_organic_unique','page_post_engagements']
            fb_until = 1548144000 + int(cal_day) * second_to_day  # 금일 날짜로 계산(날마다 갱신), 날짜는 초 단위 (1548144000은 1월 21일을 나타냄)
            fb_since = fb_until - second_to_day * int(fb_days)

            for i in range(0, len(fb_page)):

                for j in range(0, len(fb_metric)):

                    if fb_metric[j] == 'page_fan_pure_adds_unique':  # 페이지 순 좋아요 저장

                        insights_data_dict = parser.making_data(fb_page[i], fb_metric[0], fb_metric[1], fb_since, fb_until, fb_token[i])

                    else:
                        insights_data_dict = parser.crawling_data(fb_page[i], fb_metric[j], fb_since, fb_until, fb_token[i])

                    for e, v in insights_data_dict.items():
                        fb_insight(fb_page=fb_page[i], fb_metric=fb_metric[j], fb_value=v, fb_date=e, fb_token=fb_token[i], fb_page_name=fb_page_name[i]).save()


        elif str_request.find("'name'") == -1 and str_request.find("'page_remove_select'") == -1: # 페이지 등록 기능

            page_id = "'page_id'"
            page_name = "'page_name'"
            page_token = "'page_token'"
            str_bracket = '>'

            pos_id = str_request.find(page_id)
            pos_name = str_request.find(page_name)
            pos_token = str_request.find(page_token)
            pos_bracket = str_request.find(str_bracket)

            str_id = str_request[pos_id + 13: pos_name - 4]
            str_name = str_request[pos_name + 15: pos_token - 4]
            str_token = str_request[pos_token + 16: pos_bracket - 3]

            print(str_name)
            print(str_id)
            print(str_token)

            fb_insight(fb_page=str_id, fb_metric="none", fb_value="none", fb_date="none", fb_token=str_token, fb_page_name=str_name).save()

        elif str_request.find("'page_id'") == -1 and str_request.find("'name'") == -1: # 페이지 제거 기능

            print(str_request)

            page_remove_select = "'page_remove_select'"
            str_bracket = '>'
            pos_bracket = str_request.find(str_bracket)

            pos_r_s = str_request.find(page_remove_select)

            str_page_remove_select = str_request[pos_r_s + 24 : pos_bracket-3]

            print(str_page_remove_select)

            fb_insight_remove_list = fb_insight.objects.filter(fb_page_name=str_page_remove_select)

            fb_insight_remove_list.delete()

    return render(request, 'parsed_data/data_collection.html', data)

