# Generated by Django 4.2.2 on 2023-06-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=3, upload_to=''),
            preserve_default=False,
        ),
    ]
