from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) #short strings, has a max length
    description = models.TextField() #longer string, no max
    technology = models.CharField(max_length=20) #short strings, has a max length
    image = models.FilePathField(path="/img") #string but has a path
