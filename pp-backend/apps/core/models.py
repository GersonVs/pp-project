from django.db import models

# Create your models here.
class Item(models.Model):

    name          = models.CharField(max_length=100)                
    description   = models.TextField()     
    img           = models.ImageField(null=True, blank=True)        
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    votes         = models.IntegerField(default=0)   

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
