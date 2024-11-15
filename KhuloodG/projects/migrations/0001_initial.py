# Generated by Django 5.1.3 on 2024-11-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=1024)),
                ('project_brief', models.TextField()),
                ('project_model', models.URLField(max_length=1024)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Mobile App', 'Mobile App'), ('Website', 'Website')], max_length=20)),
            ],
        ),
    ]
