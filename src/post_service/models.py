from django.db import models
from django.contrib.auth import get_user_model

from core.mixins import ModelMixin

# Create your models here.
User = get_user_model()


class District(ModelMixin):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Driver(ModelMixin):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    device_registeration_code = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    last_district = models.ForeignKey(
        District, on_delete=models.PROTECT, null=True, blank=True
    )


class Mission(ModelMixin):
    created_user = models.ForeignKey(User, on_delete=models.PROTECT)
    from_office = models.BooleanField(default=False)
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    customer_full_name = models.CharField(max_length=250)
    customer_phone_number = models.CharField(max_length=11)
    description = models.TextField(null=True, blank=True)
    assigned_driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, null=True, blank=True
    )
    date_time_assigned_to_driver = models.DateTimeField(null=True, blank=True)
    date_time_delivered_to_driver = models.DateTimeField(null=True, blank=True)
    date_time_delivered_to_destination = models.DateTimeField(null=True, blank=True)
