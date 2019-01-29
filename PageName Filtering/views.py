from django.shortcuts import render
from parsed_data.models import fb_insight

def window(request):

    fb_insight_list =  fb_insight.objects.all()

    if request.method == "POST":
        temp = request.POST
        str_request = str(temp)

        str_pageSelect = 'pageSelect'
        str_bracket = '>'

        s1 = str_request.find(str_pageSelect)
        s2 = str_request.find(str_bracket)
        pageName = str_request[s1 + 15:s2 - 3]

        print(pageName)

    data = {'lists' : fb_insight_list, 'names': pageName}

    return render(request, 'parsed_data/window.html', data)

# Create your views here.