# Generated by Django 2.0.3 on 2018-03-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatu', '0008_remove_userprofile_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default/avatar.png', upload_to='avatars'),
        ),
    ]
