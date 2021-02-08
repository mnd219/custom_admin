# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from user.enums import AdminPermissionEnum

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, permission=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        if not permission:
            permission=AdminPermissionEnum.CS

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            permission=permission,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        email = 'test1@gmail.com'
        user = self.create_user(
            username=username, 
            email=email,
            password=password,
            permission=AdminPermissionEnum.AD.name,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email_address',
        max_length=225,
        unique=True
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    is_active= models.BooleanField(default=True)
    permission = models.CharField(
        max_length=2,
        choices=AdminPermissionEnum.choices()
    )

    objects = MyUserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email
        
    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.permission == AdminPermissionEnum.AD.name

