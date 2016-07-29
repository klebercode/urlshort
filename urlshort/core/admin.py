from django.contrib import admin
from urlshort.core.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('slug_key', 'my_url', 'last_access', 'count',)
    ordering = ('-last_access',)


admin.site.register(Link, LinkAdmin)
