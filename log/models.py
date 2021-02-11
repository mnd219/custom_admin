# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from log.enums import AdminPermissionEnum


class Company(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, permission=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        if not password:
            raise ValueError('Users must have an password')
        if not permission:
            permission=AdminPermissionEnum.CS.name

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            permission=permission,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
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
    companies = models.ManyToManyField(Company)

    objects = UserManager()
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

