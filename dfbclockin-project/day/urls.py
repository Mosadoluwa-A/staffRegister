from django.urls import path
from . import views

app_name = "days"

urlpatterns = [
    path('all_days/', views.all_days, name='all_days'),
]
