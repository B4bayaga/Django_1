# Generated by Django 5.0 on 2024-02-14 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="catgory",
        ),
        migrations.AddField(
            model_name="recipe",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.category",
            ),
        ),
    ]