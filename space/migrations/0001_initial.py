# Generated by Django 4.1 on 2022-10-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=50)),
                ('gender', models.TextField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')])),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]