# Generated by Django 2.0.4 on 2019-04-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190424_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='figure',
            field=models.ImageField(default='/media/user_figures/default_profile.jpg', null=True, upload_to='user_figures'),
        ),
    ]
