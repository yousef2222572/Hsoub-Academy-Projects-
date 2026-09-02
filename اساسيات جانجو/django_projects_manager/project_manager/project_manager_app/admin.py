from django.contrib import admin
from . import models
from django.db.models import Count

admin.site.register(models.Category)


@admin.register(models.Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','category','user','task_count']
    list_per_page=2
    list_editable=['title']
    list_select_related=['category','user']

    def task_count(self,obj):

        return obj.task_count
    
    def get_queryset(self, request):    
        query=super().get_queryset(request)
        query=query.annotate(task_count=Count('task'))
        return query
        
        





@admin.register(models.Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=['id','description','is_completed','project','task_count']
    list_per_page=2
    list_editable=['title']
    list_select_related=['project']

    # def task_count(self,obj):

    #     return obj.task_count
    
    # def get_queryset(self, request):    
    #     query=super().get_queryset(request)
    #     query=query.annotate(task_count=Count('task'))
    #     return query
        
        
