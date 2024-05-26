# Generated by Django 5.0 on 2024-02-16 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_remove_recipe_catgory_recipe_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.category",
            ),
        ),
    ]
