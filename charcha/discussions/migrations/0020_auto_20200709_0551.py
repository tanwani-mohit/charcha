# Generated by Django 3.0.7 on 2020-07-09 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0019_auto_20200706_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.AddField(
            model_name='post',
            name='accepted_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='discussions.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.IntegerField(choices=[(0, 'Discussion'), (1, 'Question'), (2, 'Feedback'), (3, 'Announcement'), (16, 'Response'), (17, 'Answer')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='sticky',
            field=models.BooleanField(default=False),
        ),
    ]