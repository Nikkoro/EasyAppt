# Generated by Django 3.1.6 on 2021-03-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]