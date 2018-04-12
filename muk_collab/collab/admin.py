# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from accounts.admin import UserCreationForm
from accounts.models import User
from collab.models import Project, eval_table, Results, My_workables


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('std_id', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('std_id', 'password',)}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff','course','year')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('std_id', 'password1', 'password2', 'course', 'year')}
        ),
    )
    search_fields = ('std_id',)
    ordering = ('std_id',)
    filter_horizontal = ()


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'start_time', 'end_time', 'final_result']
    list_per_page = 50

    def full_name(self, obj):
        return obj.project

    def start_time(self, obj):
        return obj.project.start_time

    def end_time(self, obj):
        return obj.project.end_time

    def std_id(self, obj):
        return obj.project.user.std_id


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'start_time', 'end_time', 'status', 'booked']
    list_filter = ['status', 'booked', 'date']
    list_per_page = 10

    def full_name(self, obj):
        return obj.user

admin.site.register(User, UserAdmin)
admin.site.register(Project,ProjectAdmin)
# admin.site.register(eval_table)
admin.site.register(Results, ResultsAdmin)
# admin.site.register(My_workables)
