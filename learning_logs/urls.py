"""Defines url patterns for learning_logs."""

from django.urls import path #Needed when mapping URLs to views
from . import views #Imports views from the same directory as urls.py

app_name = 'learning_logs'

urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    #Show all topics.
    path('topics/', views.topics, name='topics'),
    #Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]

"""Each URL maps to a particular view- the view function retrieves and processes
the data needed for that page. It also calls a template, which builds a page that
the browser can read. Using a namespace means we don't have to write out the whole URL"""
