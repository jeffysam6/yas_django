from django.contrib import admin
from places.models import Country, Park, Photo
# Register your models here.

admin.site.register(Country)
admin.site.register(Park)
admin.site.register(Photo)