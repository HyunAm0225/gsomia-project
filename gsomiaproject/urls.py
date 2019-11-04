"""gsomiaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import webprotect.views
from django.conf.urls import url,handler400,handler404,handler500

# 에러페이지 넘기기
handler400 = 'webprotect.views.bad_request_page'
handler404 = 'webprotect.views.page_not_found_page'
handler500 = 'webprotect.views.server_error_page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',webprotect.views.index,name='index'),
    path('search',webprotect.views.search,name='search'),

]
