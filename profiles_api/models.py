# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Craete a new user profile"""

        if not email:
            raise ValueError('User must have an email address:')


        email = self.normalize_emain(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)


        return user


    def create_super_user(self,email,name,password):
        """craete and save a new super user with teh given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return users





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=256,unique=True)
    name=models.CharField(max_length=256)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    def get_full_name(self):
        """Retrieve full name of teh user"""
        return self.name
    def get_short_name(self):
        """retrieve short name"""
        return self.name
    def __str__(self):
        """return string representation of the user"""
        return self.email
