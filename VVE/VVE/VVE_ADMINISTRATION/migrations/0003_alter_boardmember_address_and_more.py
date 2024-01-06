# Generated by Django 4.2.7 on 2024-01-06 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("VVE_ADMINISTRATION", "0002_alter_boardmember_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boardmember",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address_board_member",
                to="VVE_ADMINISTRATION.resident",
            ),
        ),
        migrations.AlterField(
            model_name="boardmember",
            name="last_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="last_name_board_member",
                to="VVE_ADMINISTRATION.resident",
            ),
        ),
    ]
