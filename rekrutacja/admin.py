from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Exams._meta.get_fields() if
                    field.name != "id"]


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    # pass
    # list_display = [field.name for field in Uczelnia._meta.get_fields() if field.name != "id"]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'level', 'form', 'type', 'academic_year', 'language']


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dob', 'pesel', 'phone_number', 'street', 'city', 'zip_code', 'house_number', 'flat_number', 'country']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'university', 'work_id']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'program', 'paid_admission_fee', 'date', 'status']

