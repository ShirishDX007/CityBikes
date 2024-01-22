from django.contrib import admin
from . models import Listings

class ListingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listings, ListingsAdmin)
