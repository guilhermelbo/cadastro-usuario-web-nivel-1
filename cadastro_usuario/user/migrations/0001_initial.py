# Generated by Django 4.1.1 on 2022-09-14 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                ("pais", models.CharField(max_length=50)),
                ("estado", models.CharField(max_length=50)),
                ("municipio", models.CharField(max_length=50)),
                ("cep", models.CharField(max_length=8)),
                ("rua", models.CharField(max_length=50)),
                ("numero", models.IntegerField(blank=True, null=True)),
                ("complemento", models.CharField(default="", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("nome", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50, unique=True)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("pis", models.CharField(max_length=11, unique=True)),
                ("senha", models.CharField(max_length=64)),
                (
                    "endereco_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="user.endereco"
                    ),
                ),
            ],
        ),
    ]
