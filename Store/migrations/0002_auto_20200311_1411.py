# Generated by Django 3.0.3 on 2020-03-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regisvendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('mobileno', models.CharField(max_length=50)),
                ('shopname', models.CharField(max_length=50)),
                ('buscat', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('gstno', models.CharField(max_length=10)),
                ('adhar', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='stock',
            field=models.CharField(max_length=3),
        ),
    ]
