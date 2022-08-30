from django.contrib import admin

# Register your models here.

from .models import Track


class trackAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pub_date',
        'site',
        'ativa',
        'user'
    )

    list_filter = (
        'name',
        'pub_date',
        'site',
        'ativa',
        'user'
    )
    search_fields = (
        'name',
        'site',
        'pub_date',
        'user'
    )

admin.site.register(Track, trackAdmin) #pra essa parte aparecer no sistema de admin