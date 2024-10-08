# Generated by Django 5.1.1 on 2024-09-17 09:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nameclass',
            field=models.CharField(default='Ameera Khaira Tawfiqa - KKI 2023', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
