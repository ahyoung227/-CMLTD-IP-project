# Generated by Django 3.1.3 on 2020-12-02 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculums', '0007_auto_20201202_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='curriculums.curriculum'),
        ),
    ]