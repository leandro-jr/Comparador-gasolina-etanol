from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("advanced_search", views.advanced_search, name="advanced_search"),
    path("load", views.load, name="load"),
    path("contact", views.contact, name="contact"),
    path("contact_input", views.contact_input, name="contact_input"),
    path("faq", views.faq, name="faq"),
    path("car_city", views.car_city, name="car_city"),
    path("car_city2", views.car_city2, name="car_city2"),
    path("car_city3", views.car_city3, name="car_city3"),
    path("car_city4", views.car_city4, name="car_city4"),
    path("car_city5", views.car_city5, name="car_city5"),
    path("car_city6", views.car_city6, name="car_city6"),
    path("search_car_city", views.search_car_city, name="search_car_city"),
    path("get_client_ip", views.get_client_ip, name="get_client_ip")
]
