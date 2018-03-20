# Generated by Django 2.0.3 on 2018-03-20 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tatu', '0005_auto_20180318_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='favourites',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tatu.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posters', to=settings.AUTH_USER_MODEL),
        ),
    ]
