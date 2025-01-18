from django.urls import path

from .views import DemendPage, GeographyPage, HomePage, LastVacancy, SkillsPage, AllPage


urlpatterns = [
    path('', HomePage, name='home'),
    path('all/', AllPage, name='all'),
    path('demend/', DemendPage, name='demend'),
    path('geography/', GeographyPage, name='geography'),
    path('skills/', SkillsPage, name='skills'),
    path('lastVacancy/', LastVacancy, name='lastVacancy'),
]