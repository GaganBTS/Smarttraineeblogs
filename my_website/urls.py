"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from blogs.sitemaps import *
from django.views.generic import TemplateView

sitemaps={
    'static':StaticViewsSitemap,
    'posts':PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('api',include('api.urls'),name='api'),
    path('robots.txt',TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    path('',include('blogs.urls')),
    path('tinymce/', include('tinymce.urls')),
   

] 

handler_404 = 'blogs.views.page_not_found_view'