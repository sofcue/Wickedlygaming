# Generated by Django 3.0.7 on 2020-07-06 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200610_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='NULL', upload_to='images/'),
            preserve_default=False,
        ),
    ]