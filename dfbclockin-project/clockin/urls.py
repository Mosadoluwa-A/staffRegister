
from django.urls import path
from . import views

app_name = 'clockin'

urlpatterns = [
    path('clock_in/', views.clock_in, name='clock_in'),

]
