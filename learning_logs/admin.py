from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

"""Imports the model we want to register, Topic and uses register() to manage our model
    through the admin site"""
