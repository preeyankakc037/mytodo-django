from django.db import models

# Create your models here.

# creating model for add task 
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_complete=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # very important to add those two lines of as we need to know when this data is created and updated 

    # str represenation of this function 
     
    def __str__(self):
        return self.task