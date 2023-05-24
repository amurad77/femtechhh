from django.contrib import admin
from .models import *
# Register your models here.


class InvolvedAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'membership_type','message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')

admin.site.register (Involved, InvolvedAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'message','created_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')

admin.site.register (Contact, ContactAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')

admin.site.register (Team, TeamAdmin)



# admin.site.register (Aulmnis)

admin.site.register (Partners)

admin.site.register (Statitics)

class AlumnisAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Alumnis, AlumnisAdmin)




# class AlumnisInline(admin.TabularInline):
#     model = Alumnis

# class ProgramAdmin(admin.ModelAdmin):
#     inlines = [AlumnisInline]
#     # list_display = ('title', 'mail', 'created_at', 'updated_at')
#     # list_filter = ('mail', 'created_at', 'updated_at')
#     # search_fields = ('mail', 'created_at', 'updated_at')

# admin.site.register (Program, ProgramAdmin)