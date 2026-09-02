from django.urls import path
from . import views


urlpatterns=[
    path('projects/list',views.projectlistview.as_view(),name='project_list'),
    path('projects/create',views.projectcreateview.as_view(),name='project_create'),
    path('projects/delete/<int:pk>',views.projectdeleteview.as_view(),name='project_delete'),
    path('projects/update/<int:pk>',views.projectupdateview.as_view(),name='project_update'),
    path('task/create',views.taskcreateview.as_view(),name='task_create'),
    path('task/delete/<int:pk>',views.taskdeleteview.as_view(),name='task_delete'),
    path('task/create/<int:pk>',views.taskupdateview.as_view(),name='task_update')
]