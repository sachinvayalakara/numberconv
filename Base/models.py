from django.db import models

# Create your models here.
class Numbertoword(models.Model):
    number = models.CharField(max_length=50, default='Nothing')
    word = models.CharField(max_length=50, default='Nothing')
    

    class Meta:
        db_table = 'Numbertoword'

    def __int__(self):
        return self.id