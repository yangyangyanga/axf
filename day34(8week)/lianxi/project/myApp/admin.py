from django.contrib import admin

# Register your models here.
from .models import Grades,Students
# 注册
class StudentsInfo(admin.TabularInline):# StackedInline
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ["pk", "gname", "gdate", "gboynum",
                    "ggirlnum", "isDelete"]
    list_filter = ["gname"]
    search_fields = ["gname"]
    list_per_page = 2
    # 添加、修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate',
    #           'isDelete']
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']})
    ]
admin.site.register(Grades, GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def sex(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    # 设置页面列的名称
    sex.short_description = "性别"
    def name1(self):
        return self.sname
    name1.short_description = "姓名"
    list_display = ['pk', name1, sex, 'sage', 'scontend','sGrade',
                    'isDelete']
    list_filter = ["sname"]
    search_fields = ["sname"]
    fields = ['sname', 'sage', 'scontend', 'isDelete', 'sgender','sGrade']
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

# admin.site.register(Students, StudentsAdmin)