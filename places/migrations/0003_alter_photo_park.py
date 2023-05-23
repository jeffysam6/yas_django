# Generated by Django 4.2.1 on 2023-05-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_photo_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="park",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="places.park",
            ),
        ),
    ]
