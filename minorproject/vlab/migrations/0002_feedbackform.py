# Generated by Django 4.2.5 on 2023-11-18 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vlab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('semester', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])),
                ('rating', models.CharField(choices=[('Excellent', 'excellent'), ('Good', 'good'), ('Average', 'average'), ('Poor', 'poor')], max_length=20)),
                ('suggestions', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
