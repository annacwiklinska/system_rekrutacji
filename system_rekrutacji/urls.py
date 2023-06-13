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

from rekrutacja.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('access-denied/', access_denied, name='access_denied'),
    path('search/', search, name='wyszukiwarka_kierunkow'),
    path('kierunek/<int:program_id>/', program_detail, name='kierunek_detail'),
    path('all_programs/', all_programs, name='all_programs'),
    path('random_program/', random_program, name='random_program'),
    path('university_list/', university_list, name='university_list'),
    path('university_detail/<int:university_id>/', university_detail, name='university_detail'),
    path('faq/', faq, name='faq'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name='register'),
    path('register/candidate/', candidate_signup, name='candidate_signup'),
    path('register/employee/', employee_signup, name='employee_signup'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='profile_edit'),
    path('profile/delete/', delete_account, name='delete_account'),
    path('edit_exams/', edit_exams, name='edit_exams'),
    path('edit_exam/<int:exam_id>/', edit_exam, name='edit_exam'),
    path('delete_exam/<int:exam_id>/', delete_exam, name='delete_exam'),
    path('university_programs/', university_programs, name='university_programs'),
    path('edit_program/<int:program_id>/', edit_program, name='edit_program'),
    path('delete_program/<int:program_id>/', delete_program, name='delete_program'),
    path('application_payment/<int:application_id>/', application_payment, name='application_payment'),
    path('submit_application/<int:program_id>/', submit_application, name='submit_application'),
    path('confirm_payment/<int:application_id>/', confirm_payment, name='confirm_payment'),
    path('candidate_applications/', candidate_applications, name='candidate_applications'),
    path('program_applications/', program_applications, name='program_applications'),
    path('edit_application_status/<int:application_id>/', edit_application_status, name='edit_application_status'),
]
