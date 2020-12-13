"""dfbclockin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views
from day.views import attendance

urlpatterns = [
    path('admin/', admin.site.urls),
    #AUTH
    path('', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('home/<str:msg>', views.home_msg, name='homemsg'),
    path('home/<str:error>', views.home_error, name='home_error'),
    path('admin_clockin/', views.admin_clockin, name='admin_clockin'),
    path('users/clockins/<int:user_id>', views.user_clockins, name='user_clockins'),
    #CLOCKIN
    path('clockin/', include('clockin.urls')),

    #Days
    path('day/', include('day.urls', namespace='days')),
    path('day/attendance/<int:day_id>', attendance, name='attendance'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
