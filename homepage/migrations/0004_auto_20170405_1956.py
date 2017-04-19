# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.TextField(blank=True, choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('snackApp', 'Snack or Appetizer'), ('beverage', 'Beverage')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.TextField(blank=True, choices=[('cup', 'Cup'), ('tsp', 'Teaspoon'), ('tbsp', 'Tablespoon'), ('oz', 'Ounces'), ('count', '(No Units)')], null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_text',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='meal',
        ),
        migrations.AddField(
            model_name='recipemeal',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Recipe'),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Recipe'),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Unit'),
        ),
    ]