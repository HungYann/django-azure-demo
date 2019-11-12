from django.db import models

class myfood(models.Model):
    beverage = models.CharField(max_length=45)
    def __str__(self):
        return self.beverage