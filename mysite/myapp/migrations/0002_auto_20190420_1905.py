# Generated by Django 2.0.4 on 2019-04-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='portrait',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='signature',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
