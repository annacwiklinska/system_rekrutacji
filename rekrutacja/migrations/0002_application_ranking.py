# Generated by Django 4.2.1 on 2023-06-05 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rekrutacja", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("paid_admission_fee", models.BooleanField(default=False)),
                ("date", models.DateField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.candidate",
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
                "verbose_name": "Wniosek",
                "verbose_name_plural": "Wnioski",
            },
        ),
        migrations.CreateModel(
            name="Ranking",
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
                ("points", models.IntegerField()),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rekrutacja.application",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ranking",
                "verbose_name_plural": "Rankingi",
            },
        ),
    ]
