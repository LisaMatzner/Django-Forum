from django.urls import path
from .views import SearchResultsView

urlpatterns = [
    path('results/', SearchResultsView.as_view(), name='search-results'),
]
