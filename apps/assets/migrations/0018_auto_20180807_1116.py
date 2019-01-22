# Generated by Django 2.0.7 on 2018-08-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_auto_20180702_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='label',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='hostname',
            field=models.CharField(max_length=128, verbose_name='Hostname'),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='adminuser',
            unique_together={('name', 'org_id')},
        ),
        migrations.AlterUniqueTogether(
            name='asset',
            unique_together={('org_id', 'hostname')},
        ),
        migrations.AlterUniqueTogether(
            name='gateway',
            unique_together={('name', 'org_id')},
        ),
        migrations.AlterUniqueTogether(
            name='systemuser',
            unique_together={('name', 'org_id')},
        ),
    ]
