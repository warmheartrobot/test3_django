from django.contrib import admin
from booktest.models import AreaInfo, PicTest


# Register your models here.
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo  # 关联子对象
    extra = 2  # 额外编辑2个子对象


class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'atitle', 'parent']
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False

    list_filter = ['atitle']
    search_fields = ['atitle']

    # fields = ['aparent', 'atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aparent']})
    )

    inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]



admin.site.register(AreaInfo, AreaAdmin)
admin.site.register(PicTest)
