from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blogs'),
    path('create/', create_blog_view, name='create'),
    path('update/<slug>', edit_blog_view, name='update'),
    path('detail/<slug>', detail_blog_view, name='detail'),
    path('delete/<slug>', delete_blog_view, name='delete')

]
