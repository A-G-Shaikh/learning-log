from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry
"""Imports the models we want to register (Topic and Entry) and uses register() to manage our model
    through the admin site"""
    
admin.site.register(Topic)
admin.site.register(Entry)


