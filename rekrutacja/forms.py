from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import transaction

from .models import User, Candidate, University, Employee, Exams, Program


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class CandidateSignUpForm(UserCreationForm):
    data_urodzenia = forms.DateField(label="Data urodzenia")
    pesel = forms.CharField(max_length=11, label="PESEL")
    imie = forms.CharField(max_length=100, label="Imię")
    nazwisko = forms.CharField(max_length=100, label="Nazwisko")
    telefon = forms.CharField(max_length=20, label="Telefon")
    ulica = forms.CharField(max_length=100, label="Ulica")
    miejscowosc = forms.CharField(max_length=100, label="Miejscowość")
    kod_pocztowy = forms.CharField(max_length=10, label="Kod pocztowy")
    nr_domu = forms.CharField(max_length=10, label="Numer domu")
    numer_mieszkania = forms.CharField(max_length=10, label="Numer mieszkania")
    kraj = forms.CharField(max_length=100, label="Kraj")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidate = True
        user.save()
        candidate = Candidate.objects.create(
            user=user,
            dob=self.cleaned_data.get('data_urodzenia'),
            pesel=self.cleaned_data.get('pesel'),
            first_name=self.cleaned_data.get('imie'),
            last_name=self.cleaned_data.get('nazwisko'),
            phone_number=self.cleaned_data.get('telefon'),
            street=self.cleaned_data.get('ulica'),
            city=self.cleaned_data.get('miejscowosc'),
            zip_code=self.cleaned_data.get('kod_pocztowy'),
            house_number=self.cleaned_data.get('nr_domu'),
            flat_number=self.cleaned_data.get('numer_mieszkania'),
            country=self.cleaned_data.get('kraj')
        )
        return user


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        labels = {
            'dob': 'Data urodzenia',
            'pesel': 'PESEL',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'phone_number': 'Numer telefonu',
            'street': 'Ulica',
            'city': 'Miasto',
            'zip_code': 'Kod pocztowy',
            'house_number': 'Numer domu',
            'flat_number': 'Numer mieszkania',
            'country': 'Kraj',
        }
        fields = ['first_name', 'last_name', 'dob', 'pesel', 'phone_number', 'street', 'city', 'zip_code',
                  'house_number', 'flat_number', 'country']


class EmployeeSignUpForm(UserCreationForm):
    imie = forms.CharField(max_length=100, label="Imię")
    nazwisko = forms.CharField(max_length=100, label="Nazwisko")
    nr_sluzbowy = forms.IntegerField(label="Numer służbowy")
    uczelnia = forms.ModelChoiceField(queryset=University.objects.all(), label="Uczelnia")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(
            user=user,
            first_name=self.cleaned_data.get('imie'),
            last_name=self.cleaned_data.get('nazwisko'),
            work_id=self.cleaned_data.get('nr_sluzbowy'),
            university=self.cleaned_data.get('uczelnia')
        )
        return user


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
        }


class ExamsForm(forms.ModelForm):
    class Meta:
        model = Exams
        fields = ['name', 'score']
        labels = {
            'name': 'Przedmiot',
            'score': 'Wynik',
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'level', 'form', 'type', 'description', 'academic_year', 'language')
        labels = {
            'name': 'Nazwa',
            'level': 'Stopień',
            'form': 'Forma',
            'type': 'Typ',
            'description': 'Opis',
            'academic_year': 'Rok akademicki',
            'language': 'Język',
        }
