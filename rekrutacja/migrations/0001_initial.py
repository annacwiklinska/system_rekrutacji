

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("is_candidate", models.BooleanField(default=False)),
                ("is_employee", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
            ],
            options={
                "verbose_name": "Matura",
                "verbose_name_plural": "Matury",
            },
        ),
        migrations.CreateModel(
            name="University",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("kind", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("establishment_date", models.DateField()),
                ("official_university_id", models.IntegerField(unique=True)),
                ("status", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Uczelnia",
                "verbose_name_plural": "Uczelnie",
            },
        ),
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                ("pesel", models.CharField(blank=True, max_length=11, null=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("street", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=10)),
                ("house_number", models.CharField(max_length=10)),
                ("flat_number", models.CharField(blank=True, max_length=10, null=True)),
                ("country", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Kandydat",
                "verbose_name_plural": "Kandydaci",
            },
        ),
        migrations.CreateModel(
            name="Program",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("I stopień", "I stopień"),
                            ("II stopień", "II stopień"),
                            ("jednolite", "jednolite"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "form",
                    models.CharField(
                        choices=[
                            ("stacjonarne", "stacjonarne"),
                            ("niestacjonarne", "niestacjonarne"),
                            ("online", "online"),
                            ("hybrydowe", "hybrydowe"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("licencjackie", "licencjackie"),
                            ("inżynierskie", "inżynierskie"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("academic_year", models.CharField(max_length=9)),
                ("language", models.CharField(max_length=50)),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.university",
                    ),
                ),
            ],
            options={
                "verbose_name": "Kierunek Studiów",
                "verbose_name_plural": "Kierunki Studiów",
            },
        ),
        migrations.CreateModel(
            name="RequiredExams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "multiplier",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.exam",
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.program",
                    ),
                ),
            ],
            options={
                "verbose_name": "Wymagane Matury",
                "verbose_name_plural": "Wymagane Matury",
                "unique_together": {("program", "name")},
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("work_id", models.IntegerField()),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.university",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pracownik",
                "verbose_name_plural": "Pracownicy",
            },
        ),
        migrations.CreateModel(
            name="Exams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ]
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.exam",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.candidate",
                    ),
                ),
            ],
            options={
                "verbose_name": "Wyniki Matur",
                "verbose_name_plural": "Wyniki Matur",
                "unique_together": {("candidate", "name")},
            },
        ),
    ]
