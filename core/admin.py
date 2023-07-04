from django.contrib import admin
from .models import User, Organization, Shelf, ShelfReadings, Group, AlertLogs

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Shelf)
admin.site.register(ShelfReadings)
admin.site.register(Group)
admin.site.register(AlertLogs)
