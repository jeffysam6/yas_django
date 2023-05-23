from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from reviews.models import Review
from django.core.cache import cache



@receiver([post_save, post_delete], sender=Review)
def invalidate_photo_cache(sender, instance, **kwargs):
    review = instance
    park_key = review.park.id
    country_key = review.park.country.id
    review_cache_key = f"{Review.__name__}-{park_key}"
    if review_cache_key in cache:
        cache.delete(review_cache_key)
    if country_key in cache:
        cache.delete(country_key)
