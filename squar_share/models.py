#-*- coding:utf-8 -*-
from django.db import models

from datetime import datetime #导入datetime 用于处理上传文件的时间段
# Create your models here.

class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"访问次数",default=0)
    code = models.CharField(max_length=8,verbose_name=u"code")
#    Datatime = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    Datatime = models.DateTimeField(default=datetime.now)
    path = models.CharField(max_length=32,verbose_name=u"下载路径")
    name = models.CharField(max_length=32,verbose_name=u"文件名",default="")
    Filesize = models.CharField(max_length=10,verbose_name=u"文件大小")
    PCIP = models.CharField(max_length=32,verbose_name="IP地址",default="")

    class Meta():
        verbose_name="download"
        verbose_name_plural = verbose_name
        db_table = "download"

    def __str__(self):
        return self.name
