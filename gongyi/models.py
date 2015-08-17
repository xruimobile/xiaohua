# -*- coding:utf-8 -*-
from django.db import models
import subprocess
import datetime
import os

# Create your models here.

class Children(models.Model):
    '''
    children
    '''
    class Meta:
        db_table = 'children'
        verbose_name = '儿童信息'
        verbose_name_plural = '儿童信息'

    child_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='', verbose_name='姓名')
    gender = models.IntegerField(max_length=1, default=0, verbose_name='性别')
    age = models.IntegerField(max_length=3, default=0, verbose_name='年龄')

    school_name = models.CharField(max_length=100, default='', verbose_name='学校')
    grade_name = models.CharField(max_length=100, default='', verbose_name='年级')

    icon = models.CharField(max_length=255, default='', verbose_name='头像')
    #icon = models.ImageField(upload_to='children')
    introduce = models.CharField(max_length=255, default='', verbose_name='个人介绍')

    sound_id = models.IntegerField(max_length=11, default=0)
    sound_url = models.CharField(max_length=255, default='', verbose_name='视频链接')
    sound_photo_url = models.CharField(max_length=255, default='', verbose_name='视频图像')
    photo_array = models.TextField(default='', verbose_name='照片列表')
    status = models.IntegerField(max_length=1, default=1, verbose_name='上线状态', help_text='0是下线,1是上线')

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #
    #     super(Children, self).save(force_insert, force_update, using, update_fields)
    #
    #     timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    #     file_name = str(self.child_id) + '_' + timestamp
    #     comm = 'scp /root/workspace/xiaohua/media/' + self.icon.name \
    #            + ' root@liaomeizhi.com:/home/liaomeizhi_www/static/images/children/' + file_name
    #     try:
    #         out = subprocess.check_output(comm, shell=True)
    #     except:
    #         return u'cant scp'
    #
    #     self.icon.name = 'http://static.liaomeizhi.com/images/children/' + file_name
    #
    #     super(Children, self).save(force_insert, force_update, using, update_fields)



class ChildDream(models.Model):
    '''
    child dream
    '''
    class Meta:
        db_table = 'shall_child_dream_record'
        verbose_name = '心愿'
        verbose_name_plural = '心愿'

    cdid = models.AutoField(primary_key=True)
    child = models.ForeignKey(Children, verbose_name='儿童')
    donate_type = models.IntegerField(max_length=2, default=0, verbose_name='捐赠类型')
    dream = models.CharField(max_length=255, default='', verbose_name='梦想')
    dream_story = models.CharField(max_length=255, default='', verbose_name='梦想故事')
    status = models.IntegerField(max_length=1, default=1, verbose_name='上线状态', help_text='0是下线,1是上线')


