# Generated by Django 3.2.8 on 2021-10-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(default=1, max_length=32),
        ),
    ]