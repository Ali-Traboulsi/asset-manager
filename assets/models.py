import uuid

from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Asset(models.Model):
    name = models.CharField(verbose_name="asset name", max_length=100)
    description = models.TextField(verbose_name="asset description", max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # default representation
    def __str__(self):
        return self.name

    # representation for debugging
    def __repr__(self):
        return f"Asset(name='{self.name}', description='{self.description}', created_at={self.created_at})"


# Employee
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"Employee(username='{self.user.username}', " \
               f"department='{self.department}', " \
               f"position='{self.position}', " \
               f"created_at={self.created_at})"


# Lending
class Lending(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    lend_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_returned(self):
        return self.return_date is not None

    # calculate lending duration
    def lending_duration(self):
        if self.return_date:
            return self.return_date - self.lend_date
        return timezone.now() - self.lend_date

    def is_overdue(self, days=30):
        if self.return_date:
            return False
        return (timezone.now() - self.lend_date).days > days

    def mark_as_returned(self):
        self.return_date = timezone.now()
        self.save()


    def get_employee_name(self):
        return self.employee.user.username

    def __str__(self):
        return f"{self.asset.name} lent to {self.employee.user.username}"
