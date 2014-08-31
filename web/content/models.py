# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from model_utils.managers import PassThroughManager
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class DisplayQuerySet(models.query.QuerySet):
    def display(self):
        return self.filter(status=1).order_by('-create_time')


class Content(models.Model):
    title = models.CharField(max_length=25, verbose_name=u"标题")
    origin = models.CharField(max_length=20, verbose_name=u"来源")
    editor = models.CharField(max_length=10, verbose_name=u"编辑")
    content = UEditorField(u"内容", imagePath="uploadimg/",
                           filePath="uploadfiles/",
                           upload_settings={"imageMaxSize": 1204000}, blank=True, null=True)
    create_time = CreationDateTimeField()
    modify_time = ModificationDateTimeField()

    class Meta:
        abstract = True


class InformationPublish(Content):
    STATUS = {
        (0, u'隐藏'),
        (1, u'显示'),
    }
    status = models.IntegerField(default=1, choices=STATUS, verbose_name=u"状态")
    objects = PassThroughManager.for_queryset_class(DisplayQuerySet)()

    class Meta:
        verbose_name = u"信息发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('message:family_care_content', [self.id])

    get_absolute_url = models.permalink(get_absolute_url)
