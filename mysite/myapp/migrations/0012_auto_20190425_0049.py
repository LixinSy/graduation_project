# Generated by Django 2.0.4 on 2019-04-24 16:49

from django.db import migrations, models
import myapp.tool


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20190425_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='figure',
            field=models.ImageField(default='/media/user_figures/default_profile.jpg', null=True, storage=myapp.tool.FigureImageStorage, upload_to='user_figures'),
        ),
    ]
