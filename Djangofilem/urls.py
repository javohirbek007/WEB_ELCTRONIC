"""Djangofilem URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Djangofilem import settings
from myfiles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('single/',single,name='single'),
    path('products/',products,name='products'),
    path('codes/',codes,name='codes'),
    path('faq/',faq,name='faq'),
    path('icons/',icons,name='icons'),
    path('mail/',mail,name='mail'),
    path('products1/',products1,name='products1'),
    path('products2/',products2,name='products2'),
    path('pro/<str:id>/',pro,name='pro'),
    path('pro1/<str:id>/',pro1,name='pro1'),
    path('pro2/<str:id>/',pro2,name='pro2'),
    path('karzinka',karzinka,name='karzinka')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIAFILES_DIRS)