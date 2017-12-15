from django.db import models
from django.contrib import admin


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量，默认值表示在创建模型对象时，不指定这个属性值，这个值就为0
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    bremark = models.CharField(max_length=100, null=True)  # 备注

    class Meta:  #元信息类
        db_table = 'book_info'  #指定表的名称


class AreaInfo(models.Model):
    atitle = models.CharField('地区名称', max_length=30)  # 区域名称
    aparent = models.ForeignKey('self', null=True, blank=True)
    list_filter = ['atitle']

    class Meta:
        db_table = "areas"

    def __str__(self):
        return self.atitle

    def parent(self):
        return self.aparent

    def title(self):
        return self.atitle

    parent.admin_order_field = 'atitle'
    parent.short_description = '上级地区'


class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')