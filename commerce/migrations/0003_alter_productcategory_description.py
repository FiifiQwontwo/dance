# Generated by Django 3.2.4 on 2021-06-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_auto_20210620_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
