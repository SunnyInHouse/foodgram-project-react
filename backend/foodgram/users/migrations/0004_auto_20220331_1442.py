# Generated by Django 3.2.11 on 2022-03-31 14:42

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220329_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ('user',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.RemoveConstraint(
            model_name='subscribe',
            name='уникальность пары подписчик-автор',
        ),
        migrations.RemoveConstraint(
            model_name='subscribe',
            name='запрет подписки на самого себя',
        ),
        migrations.RenameField(
            model_name='subscribe',
            old_name='user_subscriber',
            new_name='user',
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('user', 'user_author'), name='уникальность пары подписчик-автор'),
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('user_author')), _negated=True), name='запрет подписки на самого себя'),
        ),
    ]
