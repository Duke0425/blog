from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render


from django.urls import reverse
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from article.form import  CateFrom
from article.models import Blog, Category

# 文章的方法:



def article(request):
    """
    文章界面
    :param request:
    :return:
    """
    if request.method == 'GET':
        blog_info = Blog.objects.all()

        page = int(request.GET.get('page',1))
        pg = Paginator(blog_info, 3)
        blog_info = pg.page(page)
        length = len(blog_info)

        return render(request, 'article.html', {'blog_info': blog_info,'length':length})


def comment(request):
    if request.method == 'GET':
        return render(request, 'comment.html')


def notice(request):
    """
    公告界面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'notice.html')


def category(request):
    """
    栏目
    :param request:
    :return:
    """
    if request.method == 'GET':
        category = Category.objects.all()
        num = 0
        return render(request, 'category.html', {'category': category, 'num': num})
    if request.method == 'POST':
        form = CateFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            nickname = form.cleaned_data['alias']
            fid = form.cleaned_data['fid']
            print(fid)
            c1 = Category.objects.filter(pk=fid).first()
            try:
                if nickname:
                    Category.objects.create(name=name,nickname=nickname,high_category=c1)
                else:
                    Category.objects.create(name=name,high_category=c1)
            except:
                pass
            return HttpResponseRedirect(reverse('article:category'))
        else:
            return render(request, 'category.html')

def flink(request):
    """
    友情链接
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'flink.html')

def manage_user(request):
    """
    用户管理
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'manage-user.html')

def loginlog(request):
    """
    登录日志
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'loginlog.html')

def setting(request):
    """
    用户设置
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'setting.html')

def readset(request):
    """
    阅读设置
    :param request:
    :return:
    """

    if request.method == 'GET':
        return render(request, 'readset.html')

def add_article(request):
    """
    添加文章
    :param request:
    :return:
    """
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'add-article.html', {'category':category})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_category = request.POST.get('tags')
        nick_name = request.POST.get('alias')
        title_pic = request.FILES.get('titlepic')
        c_id = request.POST.get('category')
        c1 = Category.objects.filter(pk=c_id).first()
        if new_category:
            Category.objects.create(name=new_category,high_category=c1,nickname=nick_name)
            Blog.objects.create(title=title,
                                content=content,
                                title_pic=title_pic,
                                category=Category.objects.filter(name=new_category).first())
        else:
            Blog.objects.create(title=title,
                                content=content,
                                title_pic=title_pic,
                                category=c1)
        return HttpResponseRedirect(reverse('article:add_article'))

def del_category(request):
    """
    删除指定栏目
    :param request:
    :return:
    """
    if request.method == 'POST':
        cate_id = request.POST.get('cate_id')
        Category.objects.filter(pk=cate_id).delete()
        cate = Category.objects.filter(pk=cate_id).first()
        Category.objects.filter(high_category=cate).delete()
        return JsonResponse({'code':'200','msg':'请求成功'})
def update_category(request, id):
    """
    更新栏目
    :param request:
    :return:
    """
    if request.method == 'GET':
        category = Category.objects.filter(pk=id).first()
        all_category = Category.objects.all()
        return render(request,'update-category.html',{'category':category,'all_category':all_category})
    if request.method == 'POST':
        form = CateFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            nickname = form.cleaned_data['alias']
            fid = form.cleaned_data['fid']
            c1 = Category.objects.filter(pk=fid).first()

            cate = Category.objects.filter(pk=id).first()
            cate.name = name
            cate.nickname = nickname
            cate.high_category = c1
            cate.save()
            return HttpResponseRedirect(reverse('article:category'))
        else:
            return HttpResponseRedirect(reverse('article:category'))

# class CateView(viewsets.GenericViewSet,
#                mixins.ListModelMixin,
#                mixins.RetrieveModelMixin,
#                mixins.CreateModelMixin,
#                mixins.UpdateModelMixin,
#                mixins.DestroyModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CateSerializer

def del_article(request):
    """
    删除文章
    :param request:
    :return:
    """
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        Blog.objects.filter(pk=blog_id).delete()

        return JsonResponse({'code':200,'msg':'请求成功'})

def update_article(request, id):
    """
    更新文章
    :param request:
    :param id:
    :return:
    """
    if request.method == 'GET':
        category = Category.objects.all()
        blog = Blog.objects.filter(pk=id).first()
        return render(request, 'update-article.html', {'category':category, 'blog':blog})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        title_pic = request.FILES.get('titlepic')
        c_id = request.POST.get('category')

        c1 = Category.objects.filter(pk=c_id).first()
        blogs = Blog.objects.filter(pk=id).first()

        blogs.title = title
        blogs.content = content
        blogs.category = c1
        blogs.title_pic=title_pic
        blogs.save()
        return HttpResponseRedirect(reverse('article:article'))