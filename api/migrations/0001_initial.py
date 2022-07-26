# Generated by Django 4.0.6 on 2022-07-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('difficulty', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('date_solved', models.DateTimeField(auto_now_add=True)),
                ('date_revised', models.DateTimeField(auto_now=True)),
                ('shared_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]