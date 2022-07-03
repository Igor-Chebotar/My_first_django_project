from django.contrib import admin

from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'full_url']
    search_fields = ['short_name']
    list_filter = ['short_name']

    class Meta:
        model = URL


admin.site.register(URL, URLAdmin)
