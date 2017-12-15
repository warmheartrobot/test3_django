from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from booktest.models import BookInfo, PicTest, AreaInfo


# Create your views here.
def index(request, canshu1, canshu2):
    context = {'value1': canshu1, 'value2': canshu2}
    return render(request, 'booktest/index.html', context)


def get(request):
    # 通过GET属性获取地址栏上的数据，获取QueryDict对象
    dict = request.GET

    a = dict.getlist('a')
    b = dict.get('b')
    context = {'a': a, 'b': b}

    return render(request, 'booktest/get.html', context)


def wish(request):
    dict = request.GET
    name = dict.get('name')
    list = dict.getlist('a')
    textlist = ['生日快乐', '节日快乐', '学习进步', '四季发财']
    str = ''
    for i in list:
        str += textlist[int(i)] + '   '

    context = {'name': name, 'wish': str}
    return render(request, 'booktest/wish.html', context)


def post(request):
    return render(request, 'booktest/post.html')


# 获取表单提交的参数
def post1(request):
    dict = request.POST
    username = dict.get('username')
    password = dict.get('password')
    gender = dict.get('gender')
    hobbies = dict.getlist('hobby')
    context = {
        'name': username,
        'password': password,
        'gender': gender,
        'hobbies': hobbies
    }

    return render(request, 'booktest/post1.html', context)


def json(request):
    return render(request, 'booktest/json.html')


def json1(request):
    books = BookInfo.objects.all()
    list = []
    for book in books:
        list.append({'btitle': book.btitle, 'bpub_date': book.bpub_date})
    return JsonResponse({'books': list})


def variable(request):
    dict = {'title': '字典键值'}
    book = BookInfo.objects.get(id=1)
    list = ['列表成员01', '列表成员02', '列表成员03']
    context = {'dict': dict, 'book': book, 'list': list}
    return render(request, 'booktest/variable.html', context)


def label(request):
    context = {'list': BookInfo.objects.all()}
    return render(request, 'booktest/label.html', context)


def filter_test(request):
    context = {'list': BookInfo.objects.all()}
    return render(request, 'booktest/filter_test.html', context)


def filter_test2(request):
    context = {'list': BookInfo.objects.all()}
    return render(request, 'booktest/filter_test2.html', context)


def inherit(request):
    context = {'title': '继承', 'list': BookInfo.objects.all()}
    return render(request, 'booktest/inherit.html', context)


# 定义转义视图
def transfer(request):
    context = {
        'title': '<h1>标签文字<h1>',
        'title2': '<script>document.body.style.background="gold"</script>'
    }
    return render(request, 'booktest/transfer.html', context)


# CSRF视图
def csrf(request):
    return render(request, 'booktest/csrf.html')


# 处理POST请求
def csrf1(request):
    dict = request.POST
    uname = dict.get('uname')
    money = dict.get('money')

    # 获取csrf验证码
    token = dict.get('csrfmiddlewaretoken')

    str = '%s--%s--%s' % (uname, money, token)
    return HttpResponse(str)


# 登录页视图
def login(request):
    return render(request, 'booktest/login.html')


# 创建验证码视图
def verify(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point（）函数绘制躁点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象,“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制四个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# 创建登陆验证视图
def login_check(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('password')
    # 获取用户输入的验证码
    veri = post.get('verify')

    # 从session读取已存的验证码
    sess = request.session.get('verifycode')

    # 比较用户名、密码和验证码
    if name == 'tom' and pwd == '123456' and veri == sess:
        return HttpResponse('<h2>恭喜登录成功</h2>')
    else:
        return HttpResponse('<h2>登录失败，请重试</h2>')


# 反向解析
def reverse_de(request):
    return render(request, 'booktest/reverse_de.html')


def reverse_de1(request):
    return HttpResponse('成功跳转到reverse_de1')


# 重定向反向解析
def redirect(request):
    return HttpResponseRedirect(reverse('booktest:reverse_de1'))


def redirect2(request):
    return HttpResponseRedirect(reverse('booktest:reverse3', args=(18, 188)))


# 定义视图，可以接收两个参数
def reverse3(request, v1, v2):
    return HttpResponse('%s----%s' % (v1, v2))


# 定义视图，静态文件
def staticfile(request):
    return render(request, 'booktest/staticfile.html')


# 定义文件上传视图
def pic_upload(request):
    return render(request, 'booktest/pic_upload.html')


# 定义文件上传后视图
def pic_handle(request):
    f1 = request.FILES.get('pic')
    fname = "%s/booktest/%s" % (settings.MEDIA_ROOT, f1.name)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("OK")


# 创建图片显示视图
def pic_show(request):
    pic = PicTest.objects.get(id=1)
    context = {'pic': pic}
    return render(request, 'booktest/pic_show.html', context)


# 分页视图
def pagelist(request, pindex):
    province = AreaInfo.objects.filter(aparent__isnull=True)
    paginator = Paginator(province, 10)

    if pindex == "":
        pindex = 1

    page = paginator.page(pindex)
    return render(request, 'booktest/pagelist.html', {'page': page})


# 省市区选择视图
def area_select(request):
    return render(request, 'booktest/area_select.html')


def areas(request):
    parent = request.GET.get('parent')
    if parent == 'None':
        areas = AreaInfo.objects.filter(aparent_id=None)
    else:
        areas = AreaInfo.objects.filter(aparent_id=int(parent))
    jsonstr = []

    for area in areas:
        jsonstr.append({'id': area.id, 'atitle': area.atitle, 'aparent': area.aparent_id})

    return JsonResponse({'data': jsonstr})
