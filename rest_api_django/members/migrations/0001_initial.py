# Generated by Django 3.2.4 on 2021-06-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]
