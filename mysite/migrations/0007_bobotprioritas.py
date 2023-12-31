# Generated by Django 4.1.2 on 2023-11-16 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0006_subalternatif"),
    ]

    operations = [
        migrations.CreateModel(
            name="BobotPrioritas",
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
                ("bobotPrio", models.TextField(blank=True, null=True)),
                ("k1", models.TextField(blank=True, null=True)),
                ("k2", models.TextField(blank=True, null=True)),
                ("k3", models.TextField(blank=True, null=True)),
                ("k4", models.TextField(blank=True, null=True)),
                (
                    "codeBF",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mysite.kriteria",
                        to_field="codeK",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Bobot-Prioritas",
            },
        ),
    ]
