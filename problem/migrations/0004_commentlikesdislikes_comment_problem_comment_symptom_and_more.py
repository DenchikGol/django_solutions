# Generated by Django 4.1.7 on 2023-03-14 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_problem_solution_symptom_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikesDislikes',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.comment')),
            ],
            bases=('problem.comment',),
        ),
        migrations.AddField(
            model_name='comment',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.problem'),
        ),
        migrations.AddField(
            model_name='comment',
            name='symptom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.symptom'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='num_dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='num_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]