from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Link, Client


class ClientInline(admin.TabularInline):
    model = Client
    readonly_fields = ('ua_string', 'creation_date',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ('__str__', 'title', 'request_count', 'creator', )
    search_fields = ('key', 'link', 'title', )
    list_filter = ('creator', )
    inlines = (ClientInline, )

    readonly_fields = (
        'creation_date', 'request_count',
    )


admin.site.register(Link, LinkAdmin)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = (
        'link', 'creation_date', 'device', 'browser', 'os'
    )
    readonly_fields = (
        'link', 'creation_date', 'device', 'browser', 'os', 'ip', 'ua_string',
    )


admin.site.register(Client, ClientAdmin)
