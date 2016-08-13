from django.contrib import admin

# Register your models here.
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    fields = ('slug', 'fullname', 'title', 'bio', 'profile_picture')
    readonly_fields = ('slug',)

admin.site.register(Member, MemberAdmin)