# Generated by Django 3.1.3 on 2021-01-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_probes', '0002_auto_20210103_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveprobe',
            name='response_time',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Response time(milliseconds)'),
        ),
    ]