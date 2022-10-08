from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('details/', views.details, name="personal"),
]
