# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django_extensions.db.fields import CreationDateTimeField


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email, last_login=now)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 创建管理员
    def create_superuser(self, username, email, password, **extra_fields):
        u = self.create_user(username, email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.is_editor = True
        u.save(using=self._db)
        return u

    def create_editor(self, username, email, password, **kwargs):
        u = self.create_user(username, email, password, **kwargs)
        u.is_active = True
        u.is_superuser = True
        u.is_editor = True
        u.save(using=self._db)
        return u


# 接入学校的数据库，学生使用学号登录，使用身份证后六位作为密码
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True, db_index=True, verbose_name=u'用户名')
    email = models.EmailField(max_length=30, verbose_name=u'邮箱')
    is_staff = models.BooleanField(default=False, verbose_name=u'系统管理员')
    is_active = models.BooleanField(default=True, verbose_name=u'可用帐号')
    is_superuser = models.BooleanField(default=False, verbose_name=u'管理员')
    is_editor = models.BooleanField(default=False, verbose_name=u'编辑')
    # 针对管理员负责的类型
    create_time = CreationDateTimeField()

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = u"管理员"
        verbose_name_plural = "管理员"

    def get_username(self):
        return self.username

    def __unicode__(self):
        return self.username + "-" + self.email

    def get_full_name(self):
        return self.username + "-" + self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
