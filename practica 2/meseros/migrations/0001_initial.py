# Generated by Django 4.1.6 on 2023-02-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meseros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(default='Perú', max_length=50)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
    ]
