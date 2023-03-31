from django.db import models

# Create your models here.
class Votaciones(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    count_favor = models.IntegerField(default=0)
    count_contra = models.IntegerField(default=0)
    count_null = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    
    """ 
    def _get_total(self):
        return self.count_favor + self.count_contra + self.count_null

    total = property(_get_total)
    """
    
    def __str__(self):
        return self.title 

    