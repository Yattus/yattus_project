"""alex_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
#  from django.views.generic import TemplateView
from .views import PostListView, PostDetailView, CategorieListView
# from django.urls import reverse_lazy
# from django.views.generic.base import RedirectView

urlpatterns = [
    re_path('home/(?P<page>\d+)$', PostListView.as_view(),
            name='blog_home_page'),
    re_path(r'categorie/(?P<categorie>\w+)/(?P<page>\d+)$',
            CategorieListView.as_view(), name='blog_custom_page'),
    re_path(
        r'post/(?P<slug>.+)-(?P<pk>\d+)$',
        PostDetailView.as_view(),
        name='detail_post'),
    #  re_path(r'^categorie/(?P<slug>.+)$' )
    #  re_path(r'^article/(?P<id>\d+)/(?P<slug>.+)$', )
]
