from django.views.generic import ListView
from django.db.models import Q, Count
from django.shortcuts import render
from django.contrib.auth import get_user_model
from forum.models import Thread, Comment


class SearchResultsView(ListView):
    template_name = 'search/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        """Filter threads and users based on the search query"""
        query = self.request.GET.get("q", "")
        filter_option = self.request.GET.get("filter", "newest") # default results
        
        # Search for threads
        threads = Thread.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        # Annotate threads with the number of comments
        threads = threads.annotate(comment_count=Count('comment'))

        # apply sorting to threads
        if filter_option == "newest":
            threads = threads.order_by("-date_opened_at")
        elif filter_option == "oldest":
            threads = threads.order_by("date_opened_at")
        elif filter_option == "most_comments":
            threads = threads.order_by("-comment_count")
        elif filter_option == "least_comments":
            threads = threads.order_by("comment_count") 
        elif filter_option == "most_views":
            threads = threads.order_by("-views")
        elif filter_option == "least_views":
            threads = threads.order_by("views")
        return threads

    def get_context_data(self, **kwargs):
        """Add user search results separately."""
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")

        User = get_user_model()

        # Search for users
        context["users"] = User.objects.filter(Q(username__icontains=query) | Q(display_name__icontains=query))


        context["query"] = query  # Pass the search query to the template
        return context