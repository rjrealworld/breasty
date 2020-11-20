from django.db import models

class Task(models.Model):
    date=models.DateTimeField(auto_now_add=False)
    task=models.CharField(max_length=230)
    due = models.DateTimeField(auto_now_add=False , blank=True, null=True)
    
    def __str__(self):
        return self.task


