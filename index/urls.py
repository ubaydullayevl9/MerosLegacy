from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('teacher/<slug:slug>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('test/', views.static_test),  # 👈 временный путь для проверки
    path('meros/', views.meros_list, name='meros_list'),
    path('meros/<slug:slug>/', views.meros_detail, name='meros_detail'),
    path('search/', views.search_view, name='search'),
    path("maqomlar/", views.makom_list, name="makom_list"),
    path("maqom/<slug:slug>/", views.makom_detail, name="makom_detail"),
    path("maqom/<slug:makom_slug>/<slug:bolim_slug>/", views.bolim_detail, name="bolim_detail"),
    path("maqom/<slug:makom_slug>/<slug:bolim_slug>/<slug:shoba_slug>/", views.shoba_detail, name="shoba_detail"),
    path("kuy/<slug:slug>/", views.kuy_detail, name="kuy_detail")
]

