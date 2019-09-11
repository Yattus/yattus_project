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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from django.views.generic import TemplateView
from blog.views import PostListView


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),  # urls to admin
    re_path(
        r'^accueil',
        TemplateView.as_view(template_name='base.html'),
        name='base'),
    re_path(r'^$', PostListView.as_view(), name='home'),
    re_path(r'^blog/', include('blog.urls')),  # urls to blog
    re_path(r'^store/', TemplateView.as_view(template_name='store_page.html'),
            name='store_page'),  # urls to store page

    #  re_path(
    #  r'^home/',
    #  TemplateView.as_view(template_name='home_page.html'),
    #  name='home_page'),  # urls to home page
    #  re_path(
    #  r'^services/',
    #  TemplateView.as_view(template_name='services_page.html'),
    #  name='services_page'),  # urls to services page
    #  re_path(
    #  r'^contacts/',
    #  TemplateView.as_view(template_name='contacts_page.html'),
    #  name='contacts_page'),
    #  re_path(
    #  r'^portofolio/',
    #  TemplateView.as_view(template_name='portofolio_page.html'),
    #  name='portofolio_page'),  # urls to portofolio page
    re_path(
        r'^recherche/',
        TemplateView.as_view(template_name='home_page'),
        name='recherche'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
