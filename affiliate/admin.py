from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ('__str__', 'title', 'request_count', 'creator', )
    search_fields = ('key', 'link', 'title', )
    list_filter = ('creator', )

    readonly_fields = (
        'creation_date', 'request_count',
    )


admin.site.register(Link, LinkAdmin)
