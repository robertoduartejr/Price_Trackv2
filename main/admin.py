from django.contrib import admin

# Register your models here.

from .models import CustomUser


class TrackCustomUser(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
    )

    list_filter = (
        'username',
        'email'
    )
    search_fields = (
        'username',
        'email'
    )

admin.site.register(CustomUser, TrackCustomUser) #pra essa parte aparecer no sistema de admin