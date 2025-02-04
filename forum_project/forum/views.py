from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count

from .models import Thread, Comment


class ThreadListView(ListView):
    model = Thread
    template_name = "threads.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(thread=self)
        context["comment_count"] = comments.aggregate(
                                    comment_count=Count("pk"))["comment_count"]
        context["last_comment"] = comments.order_by("-date_posted").first()


class ThreadDetailView(DetailView):
    model = Thread
    template_name = "thread.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all() # Get all comments from the parent thread. Customize 'comment_set' with <related_name='comments'> inside Post model: thread = models.ForeignKey(Thread, related_name=...)

class ThreadCreateView(CreateView):
    model = Thread
    template_name = "thread_create.html"
    fields = ["topic", "description", "flag"]


class ThreadUpdateView(UpdateView):
    model = Thread
    template_name = "thread_update.html"
    fields = ["description", "flag"]


class ThreadDeleteView(DeleteView):
    model = Thread
    template_name = "thread_delete"
    success_url = reverse_lazy("threads")


class CommentCreateView(CreateView):
    model = Comment
    template_name = "comment_create"
    fields = ["text"]


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "comment_update"
    fields = ["text"]


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "comment_delete"

    def get_success_url(self):
        comment = self.get_object() # Get the comment to be deleted
        thread = comment.thread # Get the parent thread

        return reverse_lazy("thread_detail", kwargs={"pk": thread.pk}) # Redirect to the parent thread
