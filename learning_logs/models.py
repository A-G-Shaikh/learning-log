from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#A model tells Django how to work with the data that will be stored in the app.

class Topic(models.Model):
    """A topic that the user is learning about. Inherits from the Model 
    parent class that defines the basic functionality of a model."""
    
    
    text = models.CharField(max_length=200) 
    """Piece of data that's made up of characters or text.
    CharField is used when you want to store a small amount of text.
    Django also has to be told how much space it should reserve"""
    date_added = models.DateTimeField(auto_now_add=True)
    #Will automatically record the current date and time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
        
class Entry(models.Model):
    """Something specific learned about a topic. Each entry needs to be
    associated with a particular topic. This is a many to one relationship because
    many entries will need to be associated with one Topic"""
    
    """A ForeignKey is a reference to another record in the database.
    This connects each entry to a specific topic. Each topic is assigned a key/ID.
    To establish a connection between the 2 pieces of data, it uses the key associated
    with each piece of information"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #Cascading delete - all entries associated with the topic will be deleted.
    text = models.TextField()
    #TexField does not need a size limit, because we don't want to limit the size of entries.
    date_added = models.DateTimeField(auto_now_add=True)
    #Presents all entries in the order they were created and timestamps each entry.
    
    class Meta:
        #Will hold extra info for managing a model.
        verbose_name_plural = 'entries'
        #Without this, Django would refer to multiple entries as 'Entrys'.
    def __str__(self):
        """Return a string representation of the model.
            Which info to show when it refers to individual entries"""
        
        #Return a snippet of the entry for ease of use
        if len(self.text) > 50:
            return self.text[:50] + "..." #Ellipses to clarify it's not entire entry.
        else:
            return self.text
