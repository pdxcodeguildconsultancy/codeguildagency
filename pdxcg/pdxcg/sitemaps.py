from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.core.urlresolvers import reverse

from pdxcodeguild import views


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'mainpage',
            'about',
            'apply',
            'contact',
            'gettechnical',
            'devbootcamp',
            'evening_bootcamp',
            'partner',
            'program',
            'sponsor',
            'advisors',
            'ppm',
            'team',
            'students',
            ]

    def location(self, item):
        return reverse(item)


