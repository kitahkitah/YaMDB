# Generated by Django 2.2.16 on 2022-05-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220510_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmations_code',
            field=models.UUIDField(blank=True, null=True, verbose_name='Код подтверждения для поулчения токена'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=9, verbose_name='Роль пользователя'),
        ),
    ]
