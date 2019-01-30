from django.shortcuts import render
from parsed_data.models import fb_insight

def window(request):

    fb_insight_list =  fb_insight.objects.all()

    pageName = 'Page Name'
    date_from = '시작 날짜'
    date_to = '종료 날짜'

    if request.method == "POST":
        temp = request.POST
        str_request = str(temp)

        print(str_request)

        str_pageSelect = 'pageSelect'
        str_bracket = '>'

        s1 = str_request.find(str_pageSelect)
        s2 = str_request.find(str_bracket)
        pageName = str_request[s1 + 15:s2 - 3]

        print(pageName)

        str_from = 'from'
        str_to = "'to'"

        f1 = str_request.find(str_from)
        t1 = str_request.find(str_to)

        date_from = str_request[f1+9 : f1+19]
        date_to = str_request[t1+8 : t1+18]

        print(date_from)
        print(date_to)

        int_date_from = int(date_from[0:4] + date_from[5:7] + date_from[8:10])
        int_date_to = int(date_to[0:4] + date_to[5:7] + date_to[8:10])

    data = {'lists' : fb_insight_list, 'names': pageName, 'from': date_from, 'to':date_to}

    return render(request, 'parsed_data/window.html', data)

# Create your views here.