from django.urls import path

from user import views

urlpatterns=[
    # 登录校验
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),

]