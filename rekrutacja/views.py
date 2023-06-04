from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import CreateView
from system_rekrutacji.settings import LOGIN_URL
from .forms import LoginForm, CandidateSignUpForm, EmployeeSignUpForm, EmployeeForm, CandidateForm, ExamsForm
from .models import Program, Candidate, Employee, Exams


def index(request):
    return render(request, 'recruitment/index.html')


def search(request):
    query = request.GET.get('query', '')

    programs = Program.objects.filter(Q(name__icontains=query))

    context = {
        'query': query,
        'kierunki': programs
    }
    return render(request, 'recruitment/search.html', context)


def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    context = {
        'kierunek': program
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


def edit_exams(request):
    candidate = Candidate.objects.get(user=request.user)
    exams = Exams.objects.filter(candidate=candidate)

    if request.method == 'POST':
        form = ExamsForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.candidate = candidate
            exam.save()
            return redirect('edit_exams')
    else:
        form = ExamsForm()

    return render(request, 'recruitment/edit_exams.html', {'form': form, 'exams': exams})
