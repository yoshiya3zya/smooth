# Generated by Django 3.2 on 2022-10-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221031_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placephoto',
            name='image1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='placephoto',
            name='image2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='placephoto',
            name='image3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='placephoto',
            name='image4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
