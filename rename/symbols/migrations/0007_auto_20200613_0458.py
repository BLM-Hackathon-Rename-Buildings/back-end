# Generated by Django 3.0.7 on 2020-06-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbols', '0006_auto_20200613_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='zip_code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]