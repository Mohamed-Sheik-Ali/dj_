from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField


class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        is_active = kwargs.pop("is_active", False)
        user = self.model(
            email=email,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, is_staff=False, is_active=True, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email,
            password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16, unique=True, null=True)
    country_code = models.CharField(max_length=5, null=True)
    is_active = models.BooleanField(default=True, blank=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.CharField(max_length=500, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["phone"]

    def __str__(self):
        return self.email

class Group(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Shelf(models.Model):
    product_name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True)
    unit_weight = models.FloatField()
    total_units = models.IntegerField()
    send_alert = models.BooleanField(default=False)
    mail_alert = models.BooleanField(default=False)
    sms_alert = models.BooleanField(default=False)
    low_stock_threshold = models.IntegerField()
    high_stock_threshold = models.IntegerField()
    last_update_time = models.DateTimeField()

    def __str__(self):
        return self.product_name


class ShelfReadings(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING)
    readings = JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.shelf_id


class AlertLogs(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    mail_recipients = ArrayField(models.CharField(max_length=255))
    sms_recipients = ArrayField(models.CharField(max_length=255))
    readings = JSONField()
    msg = models.CharField(max_length=322, blank=True, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.msg
