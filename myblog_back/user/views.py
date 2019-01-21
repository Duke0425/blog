from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from user.models import User

# 主页面
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if user.password == password:
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse( 'user:index'))
            else:
                msg = '账号密码错误'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = '账号密码错误'
            return render(request, 'login.html', {'msg':msg})
