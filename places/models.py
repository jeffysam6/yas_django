from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Park(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='parks')

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255, blank=True, null=True)