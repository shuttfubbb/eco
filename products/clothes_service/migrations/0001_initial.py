# Generated by Django 4.0.1 on 2024-05-08 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('producer_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('style_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('clothes_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/clothes/')),
                ('price', models.FloatField()),
                ('sale', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.TextField(null=True)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes_service.producer')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes_service.style')),
            ],
        ),
    ]