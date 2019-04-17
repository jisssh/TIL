from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/update/', views.update_post, name='update_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comments/create/', views.creat_comment, name='create_comment'),
]