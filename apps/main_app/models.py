from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name should be at least 3 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email'
        return errors
    def form_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters'
        if postData['gender'] == 'Choose':
            errors['gender'] = 'You must make a selection for "Gender:"'
        if postData['need_transportation'] == 'Choose':
            errors['need_transportation'] = 'You must make a selection for "Need Transportation:"'
        if postData['going_to'] == 'Choose':
            errors['going_to'] = 'You must make a selection for "Going Into:"'
        return errors
    def message_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'First name should be at least 2 characters'
        if len(postData['message']) < 5:
            errors['message'] = 'Message should be at least 5 characters'
        if len(postData['message']) > 255:
            errors['message'] = 'Message length should not exceed 255 characters'
        return errors
    


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 


class SSOT(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    need_transportation = models.CharField(max_length=255)
    going_to = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 

class Winter_Jubilee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    need_transportation = models.CharField(max_length=255)
    going_to = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 

class Message_Board(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 




