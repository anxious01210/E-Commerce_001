# Generated by Django 4.0.5 on 2022-06-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContectUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('add_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]