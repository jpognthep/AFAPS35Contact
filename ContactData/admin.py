from django.contrib import admin

# Register your models here.
from .models import TUserData, TProvince 


admin.site.register(TUserData)

admin.site.register(TProvince)
