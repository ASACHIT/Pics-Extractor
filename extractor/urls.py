from django.urls import path

from .views import scrape  # scrape views function from views.py

urlpatterns = [path("", scrape, name="extractimg")]
