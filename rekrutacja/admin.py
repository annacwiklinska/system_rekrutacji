from django.contrib import admin

# Register your models here.
from .models import University, Program, Candidate, Employee, Exam, Exams


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
    list_display = [field.name for field in Program._meta.get_fields() if
                    field.name != "id" and field.name != "description"]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dob', 'pesel', 'phone_number', 'street', 'city', 'zip_code', 'house_number', 'flat_number', 'country']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.get_fields() if field.name != "id"]

