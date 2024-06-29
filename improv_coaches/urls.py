from django.urls import path
from . import views

urlpatterns = [
  path("", views.main, name="index"),
  path("improv_coaches", views.improv_coaches, name="improv_coaches"),
  path("improv_coaches/details/<int:id>", views.details, name="details"),
  path("testing/", views.testing, name="testing"),
]