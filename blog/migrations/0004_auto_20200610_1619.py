# Generated by Django 3.0.6 on 2020-06-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200610_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
