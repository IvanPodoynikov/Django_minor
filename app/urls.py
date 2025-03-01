from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # пример главной страницы
    path('task/', views.algorithmic_task, name='algorithmic_task'),  # пример страницы задачи
    path('about/', views.about, name='about'),    # страница "О проекте"
]
