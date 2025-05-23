# Generated by Django 5.1.7 on 2025-04-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ride", "0005_location_carpoolorder_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("passenger", "Passenger"), ("driver", "Driver")],
                default="passenger",
                max_length=10,
            ),
        ),
    ]
