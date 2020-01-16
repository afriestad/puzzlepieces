# Generated by Django 3.0.2 on 2020-01-16 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_auto_20200116_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confidencetracking',
            name='puzzlePiece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confidence', to='collector.PuzzlePiece'),
        ),
        migrations.AlterField(
            model_name='confidentsolution',
            name='puzzlePiece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confidentsolution', to='collector.PuzzlePiece'),
        ),
    ]
