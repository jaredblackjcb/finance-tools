from django.urls import path, include
from backtester import views
urlpatterns = [
    path('', views.backtester, name='backtester')
]