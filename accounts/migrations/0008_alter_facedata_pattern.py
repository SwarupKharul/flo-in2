# Generated by Django 3.2.3 on 2021-06-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_facedata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedata',
            name='pattern',
            field=models.BigIntegerField(default=0),
        ),
    ]
