from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.text import slugify
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit

import datetime

class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Tag, self).save()

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Category, self).save()

    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)
    site = models.ForeignKey(Site)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def get_absolute_url(self):
        return "/%s" % self.slug

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


#class PostForm(ModelForm):
#    class Meta:
#        model = Post
#        fields = ['title', 'pub_date', 'text', 'slug', 'author', 'site', 'category', 'tags']


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Post'))

    class Meta:
        model = Post

    title = forms.CharField()

    pub_date = forms.DateTimeField(
        label="Date and Time",
        initial = datetime.datetime.now(),
    )

    slug = forms.SlugField()