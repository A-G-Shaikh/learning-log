from django.shortcuts import render
#The render function renders the response based on the data provided by views.
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

"""A view function takes in information from a request, prepares the data
needed to generate a page, and sends the data back to the browser, using 
the template that defines what the page will look like."""

from .models import Topic, Entry
#Always remember to import the model associated with the data you need
from .forms import TopicForm, EntryForm

def index(request):
    """The homepage for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Shows all topics."""
    #Show user only the topics that belong to them.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #Database query for Topic objects, stored in 'topics'.
    context = {'topics': topics}
    #Context - dictionary for the data we need to send to the template.
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) #Query to retrieve the topic
    #Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') #Most recent entries first
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic - needs to handle 2 different situations:
    initial requests for a new_topic page(blank form) and the processing of 
    any data submitted in the form."""
    
    #Test to see whether the request method is GET or POST
    if request.method != 'POST': #GET request only reads the data from the server
        #No data submitted, create a blank form for the user to fill out.
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST)
        #POST request when the user needs to submit information.
        if form.is_valid(): #Only saves if the data is valid + all required fields completed.
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #Redirect the reader back to the topics page.
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            #Reverse gets the URL for the topics page and passes it to the function.
            
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    
@login_required
def new_entry(request, topic_id): #Stores the value it receives from the URL.
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id) 
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST': #Check if request method is POST or GET.
        #No data submitted, create a blank form.
        form = EntryForm()
    else:
        #POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) #Entry not saved in the database yet.
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id) #Get the entry the user wants to edit.
    topic = entry.topic #Get the topic associated with the entry.
    if topic.owner != request.user: #Protect entries from other users.
        raise Http404 #Check if owner of topic matches logged-in user.
    if request.method != 'POST':
        #Initial request; pre-fill form with current entry to see existing data.
        form = EntryForm(instance=entry)
        
    else:
        #POST the data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
            
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    
