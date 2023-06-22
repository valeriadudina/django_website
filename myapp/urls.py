from django.urls import path
from . import views

urlpatterns = [
    path('preference', views.index, name="preference"),
    path('tinder', views.tindef_from, name="tinder_form"),
    path('review/<int:review_id>', views.review_by_id, name='review_by_id'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('map', views.map, name="map"),
    path('insurance', views.insurance, name="insurance"),
    path('tours', views.tours, name="tours"),
    path('about_us', views.about_us, name="about_us"),
    path('count_tour', views.count_tour, name="count_tour"),
    path('game', views.game, name="game"),
path('ways', views.ways, name="ways"),
    path('routes_excursions', views.routes_excursions, name="routes_excursions"),
    path('tinder_review', views.tinder_review, name="tinder_review"),
    path('list_of_things', views.list_of_things, name="list_of_things"),
    path('contact_us', views.contactus_form, name="contact_us"),
    path('popular_directions', views.popular_destinations, name="popular_directions"),
    path('', views.main_page, name="main_page"),
    path('photo_gallery', views.photo_gallery, name="photo_gallery"),
    path('video_gallery', views.video_gallery, name="video_gallery"),
    path('<slug:slug>', views.TourDetailView, name="tour_detail"),

]