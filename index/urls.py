from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('teacher/<slug:slug>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('test/', views.static_test),  # 👈 временный путь для проверки
    path('meros/', views.meros_list, name='meros_list'),
    path('meros/<slug:slug>/', views.meros_detail, name='meros_detail'),
    path('search/', views.search_view, name='search')
]
