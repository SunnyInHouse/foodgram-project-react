# Generated by Django 3.2.11 on 2022-02-04 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20220203_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shoppings', to=settings.AUTH_USER_MODEL, verbose_name='Автор списка покупок'),
        ),
    ]