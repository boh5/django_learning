"""

@Author  : dilless
@Time    : 2018/6/30 22:51
@File    : urls.py
"""
from django.urls import path

from login import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
