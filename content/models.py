from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=191)
    
    def __str__(self):
        return self.name
    
    
class Articles(models.Model):
    title= models.CharField(max_length=191)
    content=models.TextField()
    publication_date=models.DateField(auto_now_add=True)
    categories=models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title
        
    
       