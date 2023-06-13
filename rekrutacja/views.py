from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import CreateView
from system_rekrutacji.settings import LOGIN_URL
from .decorators import *
from .forms import LoginForm, CandidateSignUpForm, EmployeeSignUpForm, EmployeeForm, CandidateForm, ExamsForm, \
    ProgramForm
from .models import Program, Candidate, Employee, Exams, RequiredExams, Exam, Application


def index(request):
    return render(request, 'recruitment/index.html')


def search(request):
    query = request.GET.get('query', '')
    programs = Program.objects.none()  # Pusty QuerySet

    if query:
        programs = Program.objects.filter(Q(name__icontains=query))

    context = {
        'query': query,
        'kierunki': programs
    }
    return render(request, 'recruitment/search.html', context)



def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    required_exams = RequiredExams.objects.filter(program=program)
    context = {
        'program': program,
        'required_exams': required_exams
    }
    return render(request, 'recruitment/kierunek_studiow_detail.html', context)


def logout_view(request):
    logout(request)
    return redirect(LOGIN_URL)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'recruitment/login.html', {'form': form, 'error': 'Niepoprawny login lub hasło'})
    else:
        form = LoginForm()
        return render(request, 'recruitment/login.html', {'form': form})


class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'recruitment/register_candidate.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


def candidate_signup(request):
    view = CandidateSignUpView.as_view()
    return view(request)


class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'recruitment/register_employee.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


def employee_signup(request):
    view = EmployeeSignUpView.as_view()
    return view(request)


def register(request):
    return render(request, 'recruitment/register.html')


# @login_required
# def candidate_profile(request):
#     candidate = Candidate.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = CandidateProfileForm(request.POST, instance=candidate)
#         if form.is_valid():
#             form.save()
#             return redirect('candidate_profile')
#     else:
#         form = CandidateProfileForm(instance=candidate)
#
#     context = {
#         'candidate': candidate,
#         'form': form
#     }
#     return render(request, 'recruitment/candidate_profile_edit.html', context)
#
#
# @login_required
# def employee_profile(request):
#     employee = Employee.objects.get(user=request.user)
#
#     if request.method == "POST":
#         form = EmployeeProfileForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect('employee_profile')
#     else:
#         form = EmployeeProfileForm(instance=employee)
#
#     context = {
#         "pracownik": employee,
#         "form": form
#     }
#     return render(request, 'recruitment/employee_profile_edit.html', context)

@login_required
def edit_profile(request):
    user = request.user
    if user.is_employee:
        profile_instance = Employee.objects.get(user=user)
        form_class = EmployeeForm
        template_name = 'recruitment/employee_profile_edit.html'
    elif user.is_candidate:
        profile_instance = Candidate.objects.get(user=user)
        form_class = CandidateForm
        template_name = 'recruitment/candidate_profile_edit.html'
    else:
        return HttpResponse("Nie masz dostępu do tej strony.")

    if request.method == 'POST':
        form = form_class(request.POST, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = form_class(instance=profile_instance)

    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    user = request.user

    if user.is_candidate:
        profile_instance = Candidate.objects.get(user=user)
        template_name = 'recruitment/candidate_profile.html'
    elif user.is_employee:
        profile_instance = Employee.objects.get(user=user)
        template_name = 'recruitment/employee_profile.html'
    elif user.is_superuser:
        return HttpResponsePermanentRedirect('/admin/')
    else:
        return HttpResponse("Nie masz dostępu do tej strony.")

    context = {
        'profile': profile_instance,
        'user': user
    }
    return render(request, template_name, context)


@login_required
def delete_account(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        return HttpResponse("Twoje konto zostało usunięte.")

    template_name = 'recruitment/delete_account.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)


@candidate_required
def edit_exams(request):
    candidate = Candidate.objects.get(user=request.user)
    exams = Exams.objects.filter(candidate=candidate)

    if request.method == 'POST':
        form = ExamsForm(request.POST)
        if form.is_valid():
            new_exam = form.save(commit=False)
            new_exam.candidate = candidate

            existing_exam = Exams.objects.filter(candidate=candidate, name=new_exam.name).first()
            if existing_exam:
                messages.warning(request,
                                 'Masz już wpisany wynik z tego przedmiotu. Możesz go jedynie edytować lub usunąć.')
                return redirect('edit_exams')
            else:
                new_exam.save()

            return redirect('edit_exams')
    else:
        form = ExamsForm()

    return render(request, 'recruitment/edit_exams.html', {'form': form, 'exams': exams})


@candidate_required
def edit_exam(request, exam_id):
    exam = get_object_or_404(Exams, id=exam_id)

    if request.method == 'POST':
        form = ExamsForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('edit_exams')
    else:
        form = ExamsForm(instance=exam)

    return render(request, 'recruitment/edit_exam.html', {'form': form, 'exam': exam})


@candidate_required
def delete_exam(request, exam_id):
    exam = get_object_or_404(Exams, id=exam_id)
    exam.delete()
    return redirect('edit_exams')


# def university_programs(request):
#     employee = Employee.objects.get(user=request.user)
#     programs = Program.objects.filter(university=employee.university)
#     return render(request, 'recruitment/university_programs.html', {'programs': programs, 'employee': employee})


# def university_programs(request):
#     employee = Employee.objects.get(user=request.user)
#     programs = Program.objects.filter(university=employee.university)
#
#     if request.method == 'POST':
#         form = ProgramForm(request.POST)
#         if form.is_valid():
#             program = form.save(commit=False)
#             program.university = employee.university
#             program.save()
#             return redirect('university_programs')
#     else:
#         form = ProgramForm()
#
#     return render(request, 'recruitment/university_programs.html',
#                   {'programs': programs, 'form': form, 'employee': employee})

def university_programs(request):
    employee = Employee.objects.get(user=request.user)
    programs = Program.objects.filter(university=employee.university)

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.university = employee.university
            program.save()

            required_exams = request.POST.getlist('required_exams')
            for exam_id in required_exams:
                exam = Exam.objects.get(pk=exam_id)
                multiplier = request.POST.get('multiplier_' + exam_id)
                RequiredExams.objects.create(program=program, name=exam, multiplier=multiplier)

            return redirect('university_programs')
    else:
        form = ProgramForm()

    exams = Exam.objects.all()
    return render(request, 'recruitment/university_programs.html',
                  {'programs': programs, 'form': form, 'employee': employee, 'exams': exams})


@employee_required
def edit_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('university_programs')
    else:
        form = ProgramForm(instance=program)

    return render(request, 'recruitment/edit_program.html',
                  {'form': form, 'program': program, 'program_id': program_id})


@employee_required
def delete_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    if request.method == 'POST':
        program.delete()
        return redirect('university_programs')

    return render(request, 'recruitment/delete_program.html', {'program': program})


@candidate_required
def submit_application(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    candidate = request.user.candidate

    existing_application = Application.objects.filter(candidate=candidate, program=program).first()
    if existing_application:
        messages.warning(request, 'Już aplikowałeś na ten kierunek. Nie możesz tego zrobić dwa razy')
        return redirect('kierunek_detail', program.id)

    application = Application.objects.create(candidate=candidate, program=program)
    application.status = "nieopłacony"
    application.save()

    return redirect('application_payment', application.id)


@candidate_required
def application_payment(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if application.status == "opłacony":
        return render(request, 'recruitment/payment_confirmation.html', {'application': application})

    context = {
        'application': application,
    }
    return render(request, 'recruitment/application_payment.html', context)


@candidate_required
def confirm_payment(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    application.paid_admission_fee = True
    application.status = "opłacony"
    application.save()

    return render(request, 'recruitment/payment_confirmation.html', {'application': application})


@candidate_required
def candidate_applications(request):
    user = request.user
    applications = Application.objects.filter(candidate=user.candidate)
    context = {
        'applications': applications,
    }
    return render(request, 'recruitment/candidate_applications.html', context)


@employee_required
def program_applications(request):
    employee = Employee.objects.get(user=request.user)
    applications = Application.objects.filter(program__university=employee.university)
    return render(request, 'recruitment/program_applications.html', {'applications': applications})


@employee_required
def edit_application_status(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        application.status = new_status
        application.save()
        return redirect('program_applications')

    return render(request, 'recruitment/edit_application_status.html', {'application': application})


def access_denied(request):
    return render(request, 'recruitment/access_denied.html')
