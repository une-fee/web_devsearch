# Generated by Django 4.1.3 on 2022-11-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ration_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='vote_ration',
            new_name='vote_ratio',
        ),
    ]