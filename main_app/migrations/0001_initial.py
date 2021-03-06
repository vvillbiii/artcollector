# Generated by Django 4.0.2 on 2022-02-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=500)),
                ('period', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
