from django.contrib import admin
from .models import Dest
from booking.models import MyModel
# Register your models here.

admin.site.register(Dest)
admin.site.register(MyModel)