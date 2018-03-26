# Generated by Django 2.0.1 on 2018-01-31 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('title', models.CharField(max_length=4)),
                ('initials', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('cell', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('user_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('OTP', models.BooleanField(default=True)),
                ('status', models.CharField(max_length=1)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choiceText', models.CharField(max_length=200)),
                ('num', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='FreeformItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freeFormType', models.CharField(choices=[('Paragraph', 'Paragraph'), ('Word', 'Word'), ('Integer', 'Integer'), ('Real', 'Real')], default='Paragraph', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelText', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.CharField(max_length=1000)),
                ('questionLabel', models.CharField(max_length=300, unique=True)),
                ('pubDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionGrouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grouping', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=1000)),
                ('label', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question')),
                ('questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstWord', models.CharField(max_length=200)),
                ('secondWord', models.CharField(max_length=200)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topWord', models.CharField(max_length=25)),
                ('bottomWord', models.CharField(max_length=25)),
                ('optional', models.BooleanField(default=False)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.IntegerField()),
                ('answer', models.CharField(max_length=300)),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Label')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question')),
            ],
        ),
        migrations.CreateModel(
            name='RoundDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('startingDate', models.DateTimeField(verbose_name='starting date')),
                ('endingDate', models.DateTimeField(verbose_name='ending date')),
                ('description', models.CharField(max_length=300)),
                ('questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='TeamDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(default='emptyTeam', max_length=200)),
                ('status', models.CharField(choices=[('Not attempted', 'Not attempted'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Not attempted', max_length=20)),
                ('roundDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.RoundDetail')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='roundDetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.RoundDetail'),
        ),
        migrations.AddField(
            model_name='response',
            name='subjectUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='otherUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='questionOrders',
            field=models.ManyToManyField(through='peer_review.QuestionOrder', to='peer_review.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionGrouping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.QuestionGrouping'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.QuestionType'),
        ),
        migrations.AddField(
            model_name='label',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question'),
        ),
        migrations.AddField(
            model_name='freeformitem',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peer_review.Question'),
        ),
    ]
