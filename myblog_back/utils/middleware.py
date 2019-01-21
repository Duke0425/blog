from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User

# 中间件
class TestMiddleware1(MiddlewareMixin):

    def process_request(self, request):
        print('test1 process request')
        # 对所有的请求进行登录状态的校验
        path = request.path
        if path in ['/user/login/']:
            # 跳过以下所有代码,直接访问路由对应的视图函数
            return None
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponseRedirect(reverse('user:login'))
        user = User.objects.get(pk=user_id)
        request.user = user
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('test1 view')

    def process_response(self, request,response):
        print('test1 process response')
        return response