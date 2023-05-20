# YAS Django Challenge

This challenge is designed to test your Django and Python skills.

Requirements
============

- Generate an admin for the models in the `places` application

- The ParkView reads from a Park object and displays photos related to that park. We need to add a cache to the ParkView to reduce the number of queries to the database. For that, create a cache for the photos and add it to the view.   The cache should be invalidated when a new photo is added to the park (you don't need to add a view to add the new photo, just assume it's added via the admin).

- Create a new app called `reviews` that allows users to add reviews to parks. The review should have a rating (1-5) and a comment, it should be associated with a park and should be added via the admin (no need to create a view and template). The reviews should be displayed in the ParkView, same as before, it should be cached and invalidated when a new review is added to the park.

- We need to add a new view that displays the top 10 parks in a country (by average reviews rating). The view should be accessible at `/country/<country_id>/top/`. The view should display the country name and a list of the top 10 parks in that country. The list of parks should be cached and invalidated when a new review is added to the country.

- Delivered as a public fork of this GitHub repository, with a PR with your changes. 

- You can implement whatever cache backend you want, a plus would be to add whatever it needs in the docker-compose file.
