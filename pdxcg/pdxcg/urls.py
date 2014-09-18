from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

admin.autodiscover()

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),
    url(r'^$|^index.html?$', 'pdxcodeguild.views.index', name='mainpage'),
    url(r'^about/$', 'pdxcodeguild.views.about', name='about'),
    url(r'^apply/$', 'pdxcodeguild.views.apply', name='apply'),
    url(r'^thanks/$', 'pdxcodeguild.views.thanks', name='thanks'),
    url(r'^contact/$', 'pdxcodeguild.views.contact', name='contact'),
    url(r'^faq/$', 'pdxcodeguild.views.faq', name='faq'),
    url(r'^gettechnical/$', 'pdxcodeguild.views.gettechnical', name='gettechnical'),
    url(r'^individualized/$', 'pdxcodeguild.views.individualized', name='individualized'),
    url(r'^jrdevbootcamp/$', 'pdxcodeguild.views.jrdevbootcamp', name='jrdevbootcamp'),
    url(r'^evening_bootcamp/$', 'pdxcodeguild.views.evening_bootcamp', name='evening_bootcamp'),
    url(r'^partner/$', 'pdxcodeguild.views.partner', name='partner'),
    url(r'^program/$', 'pdxcodeguild.views.program', name='program'),
    url(r'^sponsor/$', 'pdxcodeguild.views.sponsor', name='sponsor'),
    url(r'^team/$', 'pdxcodeguild.views.team', name='team'),
    url(r'^advisors/$', 'pdxcodeguild.views.advisors', name='advisors'),
    url(r'^value/$', 'pdxcodeguild.views.value', name='value'),
    url(r'^ppm/$', 'pdxcodeguild.views.ppm', name='ppm'),
    (r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^blog/', include('pdx_blog.urls', namespace='blog')),
    url(r'^blog/comments/', include('fluent_comments.urls')),
    url(r'^articles/comments/', include('django.contrib.comments.urls')),
    url(r'^markitup/', include('markitup.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)

if settings.DEBUG:
    urlpatterns += patterns(
    'django.views.static',
    (r'media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}),)