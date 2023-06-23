from django.contrib import admin

from .models import District, Driver, Mission

from core.mixins import ModelAdminMixin


# Register your models here.
@admin.register(District)
class DistrictModelAdmin(ModelAdminMixin):
    list_display = [
        "id",
        "name",
        "is_active",
        "is_removed",
    ]
    list_filter = [
        "name",
        "created_at",
        "updated_at",
    ]
    ordering = ("-created_at",)
    search_fields = [
        "name",
    ]


@admin.register(Driver)
class DriverModelAdmin(ModelAdminMixin):
    list_display = [
        "id",
        "user",
        "device_registeration_code",
        "is_active",
        "last_district",
        "is_active",
        "is_removed",
    ]
    list_filter = [
        "user",
        "device_registeration_code",
        "is_active",
        "last_district",
        "created_at",
        "updated_at",
    ]
    ordering = ("-created_at",)
    search_fields = [
        "user",
        "device_registeration_code",
        "is_active",
        "last_district",
    ]


@admin.register(Mission)
class MissionModelAdmin(ModelAdminMixin):
    list_display = [
        "id",
        "created_user",
        "from_office",
        "address",
        "district",
        "customer_full_name",
        "customer_phone_number",
        "description",
        "assigned_driver",
        "date_time_assigned_to_driver",
        "date_time_delivered_to_driver",
        "date_time_delivered_to_destination",
        "is_active",
        "is_removed",
    ]
    list_filter = [
        "created_user",
        "from_office",
        "address",
        "district",
        "customer_full_name",
        "customer_phone_number",
        "description",
        "assigned_driver",
        "date_time_assigned_to_driver",
        "date_time_delivered_to_driver",
        "date_time_delivered_to_destination",
        "created_at",
        "updated_at",
    ]
    ordering = ("-created_at",)
    search_fields = [
        "created_user",
        "from_office",
        "address",
        "district",
        "customer_full_name",
        "customer_phone_number",
        "description",
        "assigned_driver",
        "date_time_assigned_to_driver",
        "date_time_delivered_to_driver",
        "date_time_delivered_to_destination",
    ]
