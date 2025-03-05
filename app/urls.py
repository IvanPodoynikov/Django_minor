from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # пример главной страницы
    path('main_page', views.main_page, name='main_page'), # пример информационной страницы
    path('task/', views.algorithmic_task, name='algorithmic_task'),  # пример страницы задачи
    path('about/', views.about, name='about'),    # страница "О проекте"
]
