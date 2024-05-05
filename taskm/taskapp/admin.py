from django.contrib import admin
from taskapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duedate', 'user')  
    search_fields = ['title', 'user__username']  # Add 'user__username' to search_fields

admin.site.register(Task, TaskAdmin)
