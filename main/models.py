from django.db import models
import datetime
# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null = True , blank=True)
    createdAt = models.DateTimeField( auto_now_add = True , null = True , blank=True )
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    
    def getDescriptions(self):
        return self.description[:30]
    
class TodoItems(models.Model):
   name = models.CharField(max_length=150 , null=True , blank = True )
   createAt = models.DateTimeField(auto_now_add = True )
   task = models.TextField(null = True , blank=True)
   iscompleted = models.BooleanField(default=False )
   todo = models.ForeignKey(Todo , on_delete=models.SET_NULL  , null = True)

   def __str__(self):
        return self.name
