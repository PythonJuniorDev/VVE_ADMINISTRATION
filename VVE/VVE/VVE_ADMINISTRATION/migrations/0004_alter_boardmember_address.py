# Generated by Django 4.2.7 on 2024-01-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VVE_ADMINISTRATION", "0003_alter_boardmember_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boardmember",
            name="address",
            field=models.CharField(max_length=100),
        ),
    ]