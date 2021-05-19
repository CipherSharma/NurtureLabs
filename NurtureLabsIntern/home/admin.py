from django.contrib import admin
from home.models import Bookings
from home.models import Advisor

class AdvisorAdmin(admin.ModelAdmin):
    list_display=('id','AdvisorName','AdvisorImage')

class BookingsAdmin(admin.ModelAdmin):
    list_display=('id','UserId','AdvisorId','BookingTime')

# Register your models here.
admin.site.register(Advisor,AdvisorAdmin)
admin.site.register(Bookings,BookingsAdmin)

