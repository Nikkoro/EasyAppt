# Generated by Django 3.1.6 on 2021-03-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210327_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
