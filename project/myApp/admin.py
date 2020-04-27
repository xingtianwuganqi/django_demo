from django.contrib import admin

# Register your models here.
from .models import Grades,Students

class StudentsInfo(admin.TabularInline): # 在创建一个班级时，可以直接添加几个学生
    model = Students
    extra = 2
#class StudentsInfo(admin.StackedInline): #

#注册

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]  # 加两行
    # 列表页属性
    list_display = ["pk","gname","gdate","ggirlnum","gboynum","isdelete"] # 显示字段
    list_filter =  ["gname"] # 过滤字段
    search_fields = ["gname"] # 搜索字段
    list_per_page = 10 #分页
    # 添加修改页属性
    # fields = ["ggirlnum","gboynum","gname","gdate","isdelete"]    #规定属性的先后顺序
    fieldsets = [
        ("num",{"fields":["ggirlnum","gboynum"]}),
        ("base",{"fields":["gname","gdate","isdelete"]})
    ]  # 给属性分组 注意：fields,fieldsets 不能同时使用


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 列的名称
    gender.short_description = "性别"

    list_display = ["pk","sname","sage",gender,"scontend","sgrade","isdelete"]
    list_filter = ["sname"]
    search_fields = ["sname"]
    list_per_page = 10
    fields = ["sname","sage","sgender","scontend","sgrade","isdelete"]
    # 执行顺序问题
    actions_on_top = False
    actions_on_bottom = True
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentsAdmin)




