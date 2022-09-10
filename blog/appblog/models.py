from django.db import models

class Input(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)
    date = models.DateTimeField('Fecha de Publicacion')
    
class Comment(models.Model):
    input = models.ForeignKey(Input,on_delete=models.CASCADE)
    content_comment = models.CharField(max_length=1000)