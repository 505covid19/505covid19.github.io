"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import views  # +

urlpatterns = [
    path('admin/', admin.site.urls),
    # 每个URL函数包含三个参数：URL(正规表达式)、对应方法、名称。
    path('', views.index),  # + 新增一个新的URL
    path('new1.html', views.new1),
    path('new2.html', views.new2),
    path('new3.html', views.new3),
    path('new4.html', views.new4),
    path('new5.html', views.new5),
    path('new6.html', views.new6),
    path('new7.html', views.new7),
    path('new8.html', views.new8),
    path('new9.html', views.new9),
    path('index1.html', views.index1),
    path('index2.html', views.index2),
    path('index3.html', views.index3),
    path('index4.html', views.index4),
    path('index5.html', views.index5),
    path('index6.html', views.index6),
    path('index7.html', views.index7),

]
