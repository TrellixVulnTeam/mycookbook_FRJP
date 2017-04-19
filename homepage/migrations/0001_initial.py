# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.TextField(blank=True, null=True)),
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
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
                ('date_submitted', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Ingredient')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Meal')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.TextField(blank=True, choices=[('cup', 'Cup'), ('tsp', 'Teaspoon'), ('tbsp', 'Tablespoon'), ('oz', 'ounces')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Unit'),
        ),
    ]