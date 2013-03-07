from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from fanpage_tracking.models import Fanpage, Record

def index(request):
    fanpage = Fanpage.objects.get(url_id='DunkinDonuts')
    fanpage_likes = fanpage.record_set.all().order_by('datetime')

    template = loader.get_template('fanpage_tracking/index.html')
    context = {'fanpage_likes': fanpage_likes,}

    return render(request, 'fanpage_tracking/index.html', context)
