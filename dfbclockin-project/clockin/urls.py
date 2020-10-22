
from django.urls import path
from . import views

app_name = 'clockin'

urlpatterns = [
    path('clock_in/', views.clock_in, name='clock_in'),
    path('clock_out/', views.clock_out, name='clock_out'),

]
