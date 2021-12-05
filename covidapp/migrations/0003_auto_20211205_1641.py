# Generated by Django 3.1.7 on 2021-12-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0002_auto_20211205_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('CountryCode', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Country', models.CharField(max_length=30)),
                ('NewConfirmed', models.IntegerField(default=0)),
                ('TotalConfirmed', models.IntegerField(default=0)),
                ('NewDeaths', models.IntegerField(default=0)),
                ('TotalDeaths', models.IntegerField(default=0)),
                ('NewRecovered', models.IntegerField(default=0)),
                ('TotalRecovered', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='country',
        ),
    ]
