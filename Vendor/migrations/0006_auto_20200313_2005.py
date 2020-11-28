# Generated by Django 3.0.3 on 2020-03-13 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Vendor', '0005_regisvendor_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regisvendor',
            name='buscat',
        ),
        migrations.RemoveField(
            model_name='regisvendor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='regisvendor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='regisvendor',
            name='shopname',
        ),
        migrations.AddField(
            model_name='regisvendor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regisvendor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]