from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.generic import ListView
from pdx_blog.models import Category, Post, Tag, PostForm


def new_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/blog/')
        else:
            print form.errors
    else:
        form = PostForm()
    return render_to_response('pdx_blog/new_post.html', {'form': form}, context)


class SubListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter()
        context['tags'] = Tag.objects.filter()
        return context


class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()


class TagListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()
