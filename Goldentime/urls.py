"""Goldentime URL Configuration

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
from baseapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
        path('admin_page/', views.admin_page),
    path('addtestuser',views.addtestuser),
    path('/',views.into_index),
    path('',views.into_index),
    path('index/',views.into_index),#測試用
    path('upload/',views.into_upload),
    path('login/',views.login),
    path('mypost/',views.into_mypost),
    path('search/<str:searchname>',views.search),
    path('mylove/',views.into_mylove),
    path('myinfo/',views.myinfo),
    path('into_sigin/',views.sigin),
    path('logout/',views.logout),
    path('into_login/',views.login),
    path('showdata/',views.showdata),
    path('addtestdata',views.addtestdata),
    path('edit/', views.edit), # 由 瀏覽器 開啟
    path('delete/<str:id>/', views.delete),
    path('quote_post/<str:food_no>',views.quote_post),
    path('search/',views.name_search),
    path('joinlove/<str:food_no>',views.joinlove),
    path('comment/<str:food_no>',views.comment),
    path('kill/<str:food_no>',views.kill),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
