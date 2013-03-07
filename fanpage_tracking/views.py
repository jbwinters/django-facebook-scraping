from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from fanpage_tracking.models import Fanpage, DayLikes

def index(request):
    fanpages = Fanpage.objects.all()
    fanpage_likes = []
    for fanpage in fanpages:
        likes = fanpage.daylikes_set.all().order_by('datetime')
        fanpage_likes.append((fanpage, ', '.join(str(x.likes)
                for x in likes)))

    template = loader.get_template('fanpage_tracking/index.html')
    context = {'fanpage_likes': fanpage_likes,}

    return render(request, 'fanpage_tracking/index.html', context)

