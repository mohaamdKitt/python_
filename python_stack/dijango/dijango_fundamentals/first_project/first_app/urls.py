
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('blog',views.blog),
    path("blog/new",views.newBlog),
    path('blog/create',views.creat),
    path('blog/<int:number>',views.show),
    path('blog/<int:number>/edit',views.edit),
    path('blog/<int:number>/delete',views.destroy),
    # path('root2',views.root2),
]