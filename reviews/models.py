from django.db import models
from places.models import Park

# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    park = models.ForeignKey(Park, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.park.name} - Rating: {self.rating}"