# Generated by Django 4.1.4 on 2022-12-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_question', '0005_alter_ananswer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
    ]
