from django.contrib import admin
from west.models import Character, Contact, Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email') # list
    search_fields = ('name', 'age')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
