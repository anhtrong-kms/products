from django.db import models

# Create your models here.
class chude (models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title.num}\'s chude{self.num}"
class NXB (models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    addtress = models.CharField(max_length=150)
    phone = models.TextField(max_length=15)
    def __str__(self):
        return f"{self.title.num}\'s chude{self.num}"