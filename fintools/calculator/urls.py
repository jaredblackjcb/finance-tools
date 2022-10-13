from django.urls import path, include
from calculator import views
urlpatterns = [
    path('pmi/', views.pmi_calculator, name='pmi_calculator'),
    path('annuity/', views.annuity_calculator, name='annuity_calculator')
]