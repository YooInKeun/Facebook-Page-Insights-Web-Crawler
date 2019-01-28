from django.shortcuts import render
from parsed_data.models import fb_insight

def window(request):

    fb_insight_list =  fb_insight.objects.all()
    data = {'lists':fb_insight_list}

    return render(request, 'parsed_data/window.html', data)

# Create your views here.
