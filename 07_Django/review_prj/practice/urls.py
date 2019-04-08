from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('practice/new/', views.practice_new),
    path('practice/create/', views.practice_create),
    path('practice/', views.practice_list),
    path('practice/<int:id>/', views.practice_detail),
    path('practice/<int:id>/edit/', views.practice_edit),
    path('practice/<int:id>/update/', views.practice_update),
    path('practice/<int:id>/delete/', views.practice_delete),
]