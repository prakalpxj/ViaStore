# Generated by Django 3.0.3 on 2020-03-11 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0003_productdetails_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetails',
            old_name='image',
            new_name='imag',
        ),
    ]
