# Generated by Django 4.2 on 2024-08-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "myapp1",
            "0011_alter_actividad_aprendiz_alter_actividad_experiencia_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="actividad",
            name="aprendiz",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name="actividad",
            name="experiencia",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="actividad",
            name="nivel",
            field=models.CharField(max_length=30),
        ),
    ]
