# Generated by Django 4.1.4 on 2022-12-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zones", "0002_agency_zone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agency",
            options={"ordering": ("agency_name",), "verbose_name_plural": "agencies"},
        ),
        migrations.AlterModelOptions(
            name="zone",
            options={"ordering": ("zone_name",)},
        ),
        migrations.AlterField(
            model_name="agency",
            name="agency_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="zone",
            name="zone_name",
            field=models.CharField(max_length=100),
        ),
    ]
