from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.number)

class Permission(models.Model):
    employee = models.ForeignKey(Employee,default='0',related_name='employee')
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,default='none',related_name='category')
    reason = models.TextField()

    def __str__(self):
        return str(self.employee)
