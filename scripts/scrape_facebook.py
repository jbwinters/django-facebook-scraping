import urllib2
import re
from bs4 import BeautifulSoup

from django.core.management import setup_environ
from facebook_likes_scraping import settings
setup_environ(settings)
from django.utils import timezone

from fanpage_tracking.models import Fanpage, Record

def update_likes():
    for fanpage in Fanpage.objects.all():
        if not fanpage.url_id:
            continue

        url = 'https://www.facebook.com/%s/likes' % (fanpage.url_id)
        try:
            html = ''.join(urllib2.urlopen(url).readlines())
        except urllib2.HTTPError:
            continue
        html_soup = BeautifulSoup(html)

        likes_listed_on_page = [] # there are currently two; the second is correct
        for tag in html_soup.findAll('code'):
            soup = BeautifulSoup(tag.text)
            for span in soup.findAll('span'):
                if 'class' not in span.attrs:
                    continue
                if 'timelineLikesBigNumber' in span['class']:
                    likes = span.string
                    likes_listed_on_page.append(int(''.join(likes.split(','))))
        new_likes = Record(fanpage=fanpage, datetime=timezone.now(),
                                likes=likes_listed_on_page[1])
        new_likes.save()

if __name__ == '__main__':
    update_likes()
