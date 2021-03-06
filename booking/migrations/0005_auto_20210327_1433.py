# Generated by Django 3.1.6 on 2021-03-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210327_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='barber',
            field=models.CharField(choices=[('FA', 'First Available'), ('KA', 'Keith Apelon'), ('FS', 'Frank Swan'), ('DT', 'Dario Tequila')], max_length=200),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='service',
            field=models.CharField(choices=[('HC', 'Haircut with clippers'), ('HCS', 'Haircut with clippers & scissors'), ('HBC', 'Haircut and beard combo'), ('B', 'Beard'), ('HE', 'Haircut & eyebrows'), ('DGH', 'Dying gray hair')], max_length=200),
        ),
    ]
