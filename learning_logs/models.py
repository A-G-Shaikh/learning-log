from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#A model tells Django how to work with the data that will be stored in the app.

class Topic(models.Model):
    """A topic that the user is learning about"""
    text = models.CharField(max_length=200) 
    #Piece of data that's made up of characters or text
    date_added = models.DateTimeField(auto_now_add=True)
    #Will record date and time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
        
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #Cascading delete - all entries associated with the topic will be deleted.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #Will hold extra info for managing a model.
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model.
            which info to show when it refers to individual entries"""
        
        if len(self.text) > 50:
            return self.text[:50] + "..." #Ellipses to clarify it's not entire entry.
        else:
            return self.text
