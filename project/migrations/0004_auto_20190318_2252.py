# Generated by Django 2.1.2 on 2019-03-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_split_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='split_pattern',
            field=models.CharField(blank=True, help_text='(optional) regex pattern to parse document in sentences.', max_length=255),
        ),
    ]
