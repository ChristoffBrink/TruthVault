# Generated by Django 4.2.1 on 2023-06-05 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truthlist', '0008_alter_question_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reason',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reasons/'),
        ),
    ]