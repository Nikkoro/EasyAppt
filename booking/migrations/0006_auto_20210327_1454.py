# Generated by Django 3.1.6 on 2021-03-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20210327_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='service',
            field=models.CharField(choices=[('Haircut with clippers 10$', 'Haircut with clippers 10$'), ('HCS', 'Haircut with clippers & scissors 15$'), ('HBC', 'Haircut and beard combo 25$'), ('B', 'Beard 5$'), ('HE', 'Haircut & eyebrows 15$'), ('DGH', 'Dying gray hair 25$')], max_length=200),
        ),
    ]
