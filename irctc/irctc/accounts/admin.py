from django.contrib import admin
from .models import  Booking, Person, LoggedInUser,BookingStatus

# Register your models here.
admin.site.register(Booking)
admin.site.register(Person)
admin.site.register(LoggedInUser)
admin.site.register(BookingStatus)
