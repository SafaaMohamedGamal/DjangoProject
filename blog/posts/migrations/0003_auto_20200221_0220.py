# Generated by Django 3.0.3 on 2020-02-21 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200220_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='poststable',
            name='postId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='replys',
            name='replyId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
