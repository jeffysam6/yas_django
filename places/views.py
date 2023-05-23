from django.shortcuts import render
from places.models import Park, Country
from django.views.generic import TemplateView

from django.core.cache import cache

from places.models import Photo
from reviews.models import Review

class ParkView(TemplateView):
    template_name = 'places/park.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        park_id = kwargs['pk']
        context['park'] = Park.objects.get(pk=park_id)
        photo_cache_key = f"{Photo.__name__}-{park_id}"
        review_cache_key = f"{Review.__name__}-{park_id}"
        
        if review_cache_key in cache:
            park_reviews = cache.get(review_cache_key)
            context["reviews"] = park_reviews
        else:
            park_reviews = [{"rating": review.rating, "comment": review.comment} for review in list(context['park'].reviews.all())]
            context["reviews"] = park_reviews
            cache.set(review_cache_key, park_reviews)
        
        if photo_cache_key in cache:
            photo_cache_key = f"{Photo.__name__}-{park_id}"
            park_photos = cache.get(photo_cache_key)
            context["photos"] = park_photos
        else:
            park_photos = [ {"name": photo.title, "image_url": photo.image.url} for photo in list(context['park'].photos.all())]
            context["photos"] = park_photos
            cache.set(photo_cache_key, park_photos)
            
        return context


class CountryParkView(TemplateView):
    template_name = 'places/country.html'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        country_id = kwargs['pk']
        context['country'] = Country.objects.get(pk=country_id)
        parks = context['country'].parks.all()
        if country_id in cache:
            country_parks = cache.get(country_id)
            context['parks'] = country_parks
        else:
            top_10_parks = []
            for park in parks:
                park_reviews = park.reviews.all()
                park_rating_avg = round(sum([p.rating for p in park_reviews]) / max(len(park_reviews), 1), 1)
                top_10_parks.append((park.name, park_rating_avg))
            top_10_parks.sort(key=lambda x: x[1], reverse=True)
            context['parks'] = top_10_parks[:10]
            cache.set(country_id, context['parks'])

        return context
