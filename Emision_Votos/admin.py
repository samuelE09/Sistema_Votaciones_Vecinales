from django.contrib import admin
from .models import Votaciones

# Register your models here.
class Votaciones_Admin(admin.ModelAdmin):
    readonly_fields = ('created','total',)

admin.site.register(Votaciones, Votaciones_Admin)