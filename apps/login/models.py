from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class BlogManager(models.Manager):
    def simple_validator(self, postData):
        errors = {}
        re_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors["fname"] = "First name shouldn't be empty."
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name shouldn't be empty."
        if not re_email.match(postData['email']):
            errors["email"] = "Email should be standard email characters."
        if len(postData['pw']) < 8:
            errors['pw'] = "Passwords must be longer."
        elif postData['pw'] != postData['cpw']:
            errors['match'] = "Your password didn't match up."
        if Users.objects.filter(email = postData['email']):
            errors['email'] = "Invalid email."
        if not errors:
            pass1 = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
            Users.objects.create(first_name=postData['fname'], last_name=postData['lname'], email=postData['email'],password=pass1)
        return errors

    def login_validator(self, POSTS):
        errors = {}
        # re_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(POSTS['email']) < 1 or len(POSTS['pw']) < 1:
            errors['empty'] = "Fill out Login"
        if not Users.objects.filter(email = POSTS['email']):
            errors['email'] = "Wrong email/password"
        else:
            passs = Users.objects.get(email=POSTS['email'])
            if not bcrypt.checkpw(POSTS['pw'].encode(), passs.password.encode()):
                errors['passs'] = "Wrong email/password"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager() 