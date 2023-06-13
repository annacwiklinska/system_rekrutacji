from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError


class Exam(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Matura"
        verbose_name_plural = "Matury"

    def __str__(self):
        return str(self.name)


class University(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    establishment_date = models.DateField()
    official_university_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Uczelnia"
        verbose_name_plural = "Uczelnie"


class Program(models.Model):
    LEVEL_CHOICES = (
        ('I stopień', 'I stopień'),
        ('II stopień', 'II stopień'),
        ('jednolite', 'jednolite')
    )
    FORM_CHOICES = (
        ('stacjonarne', 'stacjonarne'),
        ('niestacjonarne', 'niestacjonarne'),
        ('online', 'online'),
        ('hybrydowe', 'hybrydowe'),
    )
    TYPE_CHOICES = (
        ('licencjackie', 'licencjackie'),
        ('inżynierskie', 'inżynierskie'),
    )

    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    form = models.CharField(max_length=20, choices=FORM_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    academic_year = models.CharField(max_length=9)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def clean(self):
        if self.level != 'I stopień' and self.type:
            raise ValidationError(
                {'type': 'Pole "typ" może być uzupełnione tylko dla kierunków studiów stopnia "I stopień".'})
        if self.level == 'I stopień' and not self.type:
            self.type = "licencjackie"

    class Meta:
        verbose_name = "Kierunek Studiów"
        verbose_name_plural = "Kierunki Studiów"


class User(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField(null=True, blank=True)
    pesel = models.CharField(max_length=11, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    house_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Kandydat"
        verbose_name_plural = "Kandydaci"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    work_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id}"

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"


class Exams(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        verbose_name = "Wyniki Matur"
        verbose_name_plural = "Wyniki Matur"
        unique_together = ('candidate', 'name')

    def __str__(self):
        return str(self.name)


class RequiredExams(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.ForeignKey(Exam, on_delete=models.CASCADE)
    multiplier = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Wymagane Matury"
        verbose_name_plural = "Wymagane Matury"
        unique_together = ('program', 'name')


class Application(models.Model):
    STATUS_CHOICES = (
        ('nieopłacony', 'nieopłacony'),
        ('opłacony', 'opłacony'),
        ('przyjęty', 'przyjęty'),
        ('odrzucony', 'odrzucony'),
        ('na liście rezerwowej', 'Na liście rezerwowej'),
    )
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    paid_admission_fee = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.candidate.first_name} {self.candidate.last_name}, {self.program.name}, {self.program.university.name}"

    class Meta:
        verbose_name = "Wniosek"
        verbose_name_plural = "Wnioski"
        unique_together = ('candidate', 'program')


class Ranking(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        verbose_name = "Ranking"
        verbose_name_plural = "Rankingi"
