"""
URL configuration for system_rekrutacji project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from rekrutacja.views import index, search, program_detail, login_view, logout_view, register, \
    candidate_signup, employee_signup, profile, edit_profile, delete_account, edit_exams

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', search, name='wyszukiwarka_kierunkow'),
    path('kierunek/<int:kierunek_id>/', program_detail, name='kierunek_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name='register'),
    path('register/candidate/', candidate_signup, name='candidate_signup'),
    path('register/employee/', employee_signup, name='employee_signup'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='profile_edit'),
    path('profile/delete/', delete_account, name='delete_account'),
    path('edit_exams/', edit_exams, name='edit_exams'),
    # path('profile/edit/', edit_profile, name='profile_edit'),
    # path('candidate_profile/', candidate_profile, name='candidate_profile'),
    # path('employee_profile/', employee_profile, name='employee_profile')
]
