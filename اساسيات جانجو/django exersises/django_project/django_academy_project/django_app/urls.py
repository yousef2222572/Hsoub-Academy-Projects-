from django.urls import path
from . import views

urlpatterns=[

    # path('article/<int:id>/<int:age>/<slug:name>',views.article),
    path('about',views.about),
    path('home',views.home),
    path('',views.Articlelistviews.as_view(),name='article_list'),
    path('articles/<int:pk>',views.Articledetailview.as_view(),name='article_view'),
    path('articles/create',views.Articleformview.as_view(),name='create_article'),
    path('author/create',views.authorcreateview.as_view(),name='create_author'),
    # path('articles/<int:id>/delete',views.delete_article),
    path('article/<int:pk>/update',views.Articleupdateview.as_view(),name='update_article'),
]
