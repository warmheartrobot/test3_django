# 引入注册对象
from django.template import Library
register = Library()


# 使用装饰器
@register.filter
# 定义求余函数mod，将value对2求余
def mod(value):
    return value % 2


@register.filter
# 定义求余函数mod_num，将value对num求余
def mod_num(value, num):
    return value % num
