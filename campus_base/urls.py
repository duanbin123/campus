# coding=utf-8
"""campus_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import archives

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books_system/',include('books_system.urls'))
    url(r'^login/',include('teacher.urls')),
    url(r'^dologin/',include('sysmessage.urls'))
    # 成绩模块
    url(r'^mark/',include('mark.urls')),
    # 登录 数据库
    url(r'^',include('database.urls')),
    # 代码维护
    url(r'^maintain/',include('maintain.urls')),
    url(r'^archive/',include('archives.urls')),
    url(r'^users/',include('users.urls')),
]
