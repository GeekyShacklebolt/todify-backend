# Generated by Django 3.0.8 on 2020-11-03 08:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=512, null=False, verbose_name='Description')),
                ('rating', models.IntegerField(blank=True, default=None, help_text='Star rating 0 to 10', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Rating')),
                ('will_recommend', models.BooleanField(blank=True, default=None, help_text='Designates whether the user would like to recommend the card to others', null=True, verbose_name='Will Recommend')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cards.Card')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
                'ordering': ('-created_at',),
            },
        ),
    ]
