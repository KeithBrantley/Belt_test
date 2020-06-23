from django.db import models
from datetime import date, datetime
from django.utils.dateparse import parse_date
import bcrypt
import re

# Create your models here.


class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) == 0:
            errors['first_name'] = "Your first name has to be entered"
        elif len(post_data['first_name']) < 2:
            errors['first_name'] = "Your first name has to be longer that 2 characters"
        if len(post_data['last_name']) == 0:
            errors['first_name'] = "Your last name has to be entered"
        elif len(post_data['last_name']) < 2:
            errors['first_name'] = "Your last name has to be longer that 2 characters"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid Email Address"
        elif len(User.objects.filter(email=post_data['email'])) > 0:
            errors['email'] = "This email already exists"
        if len(post_data['password']) < 8:
            errors['password'] = "Your password has to be longer than 8 characters"
        if not (post_data['password'] == post_data['confirm_password']):
            errors['password'] = "The confirm password and password fail to match. Retype password"
        return errors


def login_validator(self, post_data):
    errors ={}
    user = User.objects.filter(email=post_data['email_login'])
    logged_user = user[0]
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(post_data['email_log']):
        errors['email_log'] = "Invalid Email"
    if user:
        if bcrypt.checkpw(pst_data['password_log'].encode(), logged_user.encode()) == False:
            errors['password_log'] = "Incorrect Password"
        else:
            errors['password_log'] = "Incorrect Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Jobs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
