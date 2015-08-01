from django.db import models

# Create your models here.

class Children(models.Model):
    '''
    children
    '''
    class Meta:
        db_table = 'children'

    child_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    gender = models.IntegerField(max_length=1, default=0)
    age = models.IntegerField(max_length=3, default=0)

    school_name = models.CharField(max_length=100, default='')
    grade_name = models.CharField(max_length=100, default='')

    icon = models.CharField(max_length=255, default='')
    introduce = models.CharField(max_length=255, default='')

    sound_id = models.IntegerField(max_length=11, default=0)
    photo_array = models.CharField(max_length=255, default='')
    status = models.IntegerField(max_length=1, default=0)


class ChildDream(models.Model):
    '''
    child dream
    '''
    class Meta:
        db_table = 'shall_child_dream_record'

    cdid = models.AutoField(primary_key=True)
    child_id = models.IntegerField(max_length=11, default=0)
    donate_type = models.IntegerField(max_length=2, default=0)
    dream = models.CharField(max_length=255, default='')
    dream_story = models.CharField(max_length=255, default='')
    status = models.IntegerField(max_length=1, default=1)

