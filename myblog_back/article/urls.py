from django.urls import path
from rest_framework.routers import SimpleRouter

from article import views



urlpatterns = [

    # 界面渲染:

    # 文章界面
    path('article/', views.article, name='article'),
    # 公告界面
    path('notice/', views.notice, name='notice'),
    # 评论界面
    path('comment/', views.comment, name='comment'),
    # 栏目界面
    path('category/',views.category, name='category'),
    # 友情链接界面
    path('flink/',views.flink, name='flink'),
    # 用户管理界面
    path('manage_user/',views.manage_user, name='manage_user'),
    # 登录日志界面
    path('loginlog/',views.loginlog, name='loginlog'),
    # 设置界面
    path('setting/',views.setting, name='setting'),
    # 阅读设置界面
    path('readset/',views.readset, name='readset'),



    # 功能如下:
    # 添加文章
    path('add_article/', views.add_article, name='add_article'),

    # 删除文章
    path('del_article/', views.del_article, name='del_article'),
    # 删除栏目
    path('del_category/', views.del_category, name='del_category'),
    # 更新文章
    path('update_article/<int:id>', views.update_article, name='update_article'),
    # 更新栏目
    path('update_category/<int:id>', views.update_category, name='update_category'),



]

# 声明路由对象
# router = SimpleRouter()
# # 定义资源
# router.register('category1', views.CateView)
# # 添加路由地址
# urlpatterns += router.urls