# Generated by Django 4.1.4 on 2022-12-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lfipayload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='xsspayload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
