# Generated by Django 2.2.4 on 2019-08-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_x', models.IntegerField()),
                ('number_y', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
