# Generated by Django 4.2.5 on 2023-09-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userInfo_name', models.CharField(max_length=50)),
                ('userInfo_email', models.CharField(max_length=60)),
                ('userInfo_phone', models.IntegerField()),
                ('userInfo_comment', models.TextField()),
            ],
        ),
    ]
