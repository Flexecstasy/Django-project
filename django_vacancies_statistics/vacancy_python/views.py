from django.shortcuts import render
from .models import MainPage, Demand, Geography, Skills, LastVacancy
from .api import ApiHeadHunter


def render_page(request, model, template_name):
    content = model.objects.all()
    return render(request, template_name, {'context': content})


def home_page(request):
    return render_page(request, MainPage, 'HomePage.html')


def demand_page(request):
    return render_page(request, Demand, 'Demend.html')


def geography_page(request):
    return render_page(request, Geography, 'Geography.html')


def skills_page(request):
    return render_page(request, Skills, 'Skills.html')


def last_vacancy(request):
    vacancy = LastVacancy.objects.first()
    if vacancy:
        hh_api = ApiHeadHunter(vacancy.vacancy_name_to_parse)
        vacs = hh_api.get_data_vacancies('2024-12-28', 10)
    else:
        vacs = []

    return render(request, 'LastVacancy.html', {'vacs': vacs, 'last_vacancies': [vacancy]})

def general_page(request):
    return render(request, 'All.html', {'context': []})
