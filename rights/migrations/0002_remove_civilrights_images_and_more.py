# Generated by Django 4.2.6 on 2024-08-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='directiveprincipleofourstatepolicy',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='economicrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='environmentalrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='fundamentalrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='humanrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='legalrights',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='politicalrights',
            name='Images',
        ),
        migrations.AlterField(
            model_name='directiveprincipleofourstatepolicy',
            name='Description',
            field=models.CharField(max_length=50002),
        ),
    ]
