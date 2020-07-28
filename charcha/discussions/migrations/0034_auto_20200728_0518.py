# Generated by Django 3.0.7 on 2020-07-28 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

# Migrate many to many field to a one to many field
UPDATE_GROUP_SET_GCHAT_SPACE = """
    UPDATE groups as g
    SET gchat_space_id = ggs.gchat_space_id
    FROM group_gchat_spaces ggs
    WHERE g.id = ggs.group_id
"""
class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0033_groupmember_added_from_gchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='gchat_space',
            field=models.ForeignKey(blank=True, help_text="Charcha will regularly import members from this chat room. By default, each member will have the role 'member'. You can override the role for any member in the group settings screen.", null=True, on_delete=django.db.models.deletion.PROTECT, to='discussions.GchatSpace', verbose_name='Google Chat Room'),
        ),
        migrations.RunSQL(UPDATE_GROUP_SET_GCHAT_SPACE),
        migrations.RemoveField(
            model_name='group',
            name='gchat_spaces',
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, help_text='Additional members to include in this group', related_name='mygroups', through='discussions.GroupMember', to=settings.AUTH_USER_MODEL, verbose_name='Group Members'),
        ),
        migrations.DeleteModel(
            name='GroupGchatSpace',
        ),
    ]
