# Generated by Django 4.2.5 on 2023-09-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_icon', models.CharField(max_length=50)),
                ('features_title', models.CharField(max_length=50)),
                ('features_des', models.TextField()),
            ],
        ),
    ]
