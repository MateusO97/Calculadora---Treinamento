# Generated by Django 2.2.4 on 2019-08-28 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subtracao', '0002_auto_20190827_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacao',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]