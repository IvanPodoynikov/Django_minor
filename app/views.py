from django.shortcuts import render
import sys
import io

def home(request):
    return render(request, 'home.html')

def solver(input_data):
    """
    Функция, которая получает три строки:
    1) Страны через пробел
    2) ВВП (float) через пробел
    3) Пороговое значение (float)

    Возвращает список стран (каждую на новой строке),
    ВВП которых >= порогу. Если нет таких стран, возвращает пустую строку.
    """
    lines = input_data.strip().split('\n')
    if len(lines) < 3:
        return "Ошибка: необходимо ввести 3 строки данных."

    # Разбиваем строки
    countries_str = lines[0].strip()
    gdp_str = lines[1].strip()
    threshold_str = lines[2].strip()

    countries = countries_str.split()
    gdps = gdp_str.split()

    # Пробуем преобразовать threshold в число
    try:
        threshold = float(threshold_str)
    except ValueError:
        return "Ошибка: пороговое значение не является числом."

    # Проверяем, что количество стран совпадает с количеством ВВП
    if len(countries) != len(gdps):
        return "Ошибка: количество стран не совпадает с количеством показателей ВВП."

    # Формируем результат
    result_list = []
    for country, gdp_value_str in zip(countries, gdps):
        try:
            gdp_value = float(gdp_value_str)
        except ValueError:
            # Если значение не преобразуется в float, пропустим
            continue

        if gdp_value >= threshold:
            result_list.append(country)

    # Выводим каждую страну с новой строки
    return "\n".join(result_list)

def algorithmic_task(request):
    """
    Страница /task/, на которой показывается JPG с условием
    и форма для ввода данных (3 строки).
    После отправки формы запускается solver() и отображается результат.
    """
    result = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        result = solver(user_input)

    return render(request, 'algorithmic_task.html', {'result': result})

def solver2(input_data):
    """
    Принимает строку вида "A B C" и проверяет, выполняются ли
    A < B < C или A < B > C.
    """
    try:
        A_str, B_str, C_str = input_data.strip().split()
        A, B, C = float(A_str), float(B_str), float(C_str)
    except:
        return "Ошибка: введите три вещественных числа через пробел"

    if A < B < C:
        return "Выполняется A < B < C"
    elif A < B > C:
        return "Выполняется A < B > C"
    else:
        return "Ни одно из неравенств не выполняется"


def algorithmic_task2(request):
    """
    Отображает страницу /task/ с условием задачи и формой для ввода данных.
    После отправки формы решает задачу и выводит результат.
    """
    result = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        result = solver2(user_input)

    return render(request, 'algorithmic_task2.html', {'result': result})

ABOUT_DATA = {
    "education_link": "https://github.com/vmarshirov/WebApplicationsDevelopment/blob/main/task1/education.txt",
    "my_info": {
        "fio": "Подойников Иван Александрович",
        "photo": "images/maxresdefault.jpg",     # лежит в static/images/maxresdefault.jpg
        "email": "podoynikov@example.com",
        "phone": "+7 (953) 456-78-90"
    },
    "program_info": {
        "name": "Математика",
        "description": "Математика",
        "director": {
            "fio": "Скрипченко Александра Сергеевна",
            "photo": "images/decan.jpg",
            "email": "skripchenko@example.com"
        },
        "manager": {
            "fio": "Иванова Татьяна Сергеевна",
            "photo": "images/manager.jpg",
            "email": "ivanovats@example.com"
        }
    },
    "classmates": [
        {
            "name": "Яковчук Николай Павлович",
            "photo": "images/kolya.jpg",
            "email": "yakovchuk@example.com",
            "phone": "+7 (111) 111-11-11"
        }
    ]
}

def about(request):
    """
    Страница /about/ — О проекте.
    Данные берутся из словаря ABOUT_DATA.
    """
    return render(request, 'about.html', ABOUT_DATA)
