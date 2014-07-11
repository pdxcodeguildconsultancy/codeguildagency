from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from pdx_blog.models import Post, Category, Tag
from pdx_blog.views import CategoryListView, TagListView, SubListView

urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', SubListView.as_view(
        model=Post,
        paginate_by=5,
        )),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        )),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryListView.as_view(
        paginate_by=5,
        model=Category,
        )),

    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagListView.as_view(
        paginate_by=5,
        model=Tag,
        )),
    url(r'^new_post/$', 'pdx_blog.views.new_post', name='new_post'),
    url(r'^new_category/$', 'pdx_blog.views.new_category', name='new_category'),
    url(r'^new_tag/$', 'pdx_blog.views.new_tag', name='new_tag'),
    url(r'^blog_admin/$', 'pdx_blog.views.blog_admin', name='blog_admin'),
)