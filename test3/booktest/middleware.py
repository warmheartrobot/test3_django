from django.http import HttpResponse


class MyMid:

    def __init__(self):
        print("--------------------init")

    def process_request(self, request):
        print("--------------------request")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("--------------------view")

    def process_template_response(self, request, response):
        print("--------------------template")
        return response

    def process_response(self, request, response):
        print("--------------------response")
        return response

    # 服务器程序错误，会执行下面的方法
    def process_exception(self, request, exception):
        print("--------------------异常")


# 中间件阻止ip访问
class IpForbidden:

    def process_request(self, request):
        ip_list = ['192.168.20.3']

        # 获取用户的地址
        user_id = request.META['REMOTE_ADDR']

        if user_id in ip_list:
            return HttpResponse('<h1>禁止访问<h1>')

