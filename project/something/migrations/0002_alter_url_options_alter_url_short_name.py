# Generated by Django 4.0.5 on 2022-06-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('something', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterField(
            model_name='url',
            name='short_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Краткое имя'),
        ),
    ]
