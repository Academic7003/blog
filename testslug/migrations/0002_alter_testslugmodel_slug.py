# Generated by Django 3.2.13 on 2022-04-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testslug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testslugmodel',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
