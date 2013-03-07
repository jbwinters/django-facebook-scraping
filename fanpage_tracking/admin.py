from django.contrib import admin
from fanpage_tracking.models import Fanpage, Record

class RecordInline(admin.TabularInline):
    model = Record
    extra = 3

class FanpageAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name']}),
            (None, {'fields': ['url_id']}),
    ]

    inlines = [RecordInline]
    list_display = ('name', 'url_id')

admin.site.register(Fanpage, FanpageAdmin)
