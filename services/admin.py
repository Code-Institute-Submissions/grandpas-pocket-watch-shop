from django.contrib import admin
from .models import AppointmentType, WatchModel, WatchType, AppointmentTime,  \
    Appointment


class AppointmentTypeAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'friendly_name',
        'name',
    )


class AppointmentTimeAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'name',
    )


class WatchModelAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'friendly_name',
        'name',
    )


class WatchTypeAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'friendly_name',
        'name',
    )


class AppointmentAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'name',
        'email',
        'appointment_type',
        'watch_model',
        'watch_type',
        'date',
        'time'
    )
    # Appointments by earliest date
    ordering = ('date',)


admin.site.register(AppointmentType, AppointmentTypeAdmin)
admin.site.register(AppointmentTime, AppointmentTimeAdmin)
admin.site.register(WatchModel, WatchModelAdmin)
admin.site.register(WatchType, WatchTypeAdmin)
admin.site.register(Appointment, AppointmentAdmin)
