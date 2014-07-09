from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdxcodeguild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pdxcodeguild.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/', 'student.views.hello'),
    url(r'^about/$', 'pdxcodeguild.views.about', name='about'),
    url(r'^apply/$', 'pdxcodeguild.views.apply', name='apply'),
    url(r'^contact/$', 'pdxcodeguild.views.contact', name='contact'),
    url(r'^faq/$', 'pdxcodeguild.views.faq', name='faq'),
    url(r'^gettechnical/$', 'pdxcodeguild.views.gettechnical', name='gettechnical'),
    url(r'^individualized/$', 'pdxcodeguild.views.individualized', name='individualized'),
    url(r'^jrdevbootcamp/$', 'pdxcodeguild.views.jrdevbootcamp', name='jrdevbootcamp'),
    url(r'^partner/$', 'pdxcodeguild.views.partner', name='partner'),
    url(r'^program/$', 'pdxcodeguild.views.program', name='program'),
    url(r'^sponsor/$', 'pdxcodeguild.views.sponsor', name='sponsor'),
    url(r'^team/$', 'pdxcodeguild.views.team', name='team'),
    url(r'^value/$', 'pdxcodeguild.views.value', name='value'),

)
