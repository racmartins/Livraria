# Generated by Django 5.1.5 on 2025-05-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Editora",
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
                ("nome", models.CharField(max_length=200)),
                ("endereco", models.TextField()),
                ("website", models.URLField(blank=True, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=20)),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="editoras/"),
                ),
            ],
            options={
                "verbose_name": "Editora",
                "verbose_name_plural": "Editoras",
                "ordering": ["nome"],
            },
        ),
    ]
