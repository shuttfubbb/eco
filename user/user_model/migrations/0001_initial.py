# Generated by Django 4.0.1 on 2024-05-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
        ),
    ]