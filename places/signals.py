from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from places.models import Photo
from django.core.cache import cache



@receiver([post_save, post_delete], sender=Photo)
def invalidate_photo_cache(sender, instance, **kwargs):
    photo = instance
    park_key = photo.park.id
    photo_cache_key = f"{Photo.__name__}-{park_key}"
    park_photos = cache.get(photo_cache_key)
    if park_photos:
        cache.delete(photo_cache_key)
