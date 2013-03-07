from django.contrib import admin
from fanpage_tracking.models import Fanpage, DayLikes

class DayLikesInline(admin.TabularInline):
    model = DayLikes
    extra = 3

class FanpageAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name']}),
            (None, {'fields': ['url_id']}),
            ('Date information', {'fields': ['creation_date'],
                'classes': ['collapse']}),
    ]

    inlines = [DayLikesInline]
    list_display = ('name', 'url_id')

admin.site.register(Fanpage, FanpageAdmin)
