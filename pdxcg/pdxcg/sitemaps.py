from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.core.urlresolvers import reverse

from pdxcodeguild import views

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    #TODO fix urls in stie map
    def items(self):
        return ['mainpage', 'about', 'apply', 'contact', 'gettechnical', 'individualized', 'jrdevbootcamp',
                'evening_bootcamp', 'partner', 'program', 'sponsor', 'advisors', 'ppm', 'team',
                ]

    def location(self, item):
        return reverse(item)


