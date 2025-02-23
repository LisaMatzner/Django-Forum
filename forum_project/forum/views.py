from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, F
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from .models import Thread, Comment, Like
from . import forms


class ThreadListView(ListView):
    model = Thread
    template_name = "threads.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        threads = self.object_list
        thread_info = []
        for thread in threads:
            comments = Comment.objects.filter(thread=thread)

            comment_count = comments.aggregate(comment_count=Count("pk"))["comment_count"]
        
            last_comment = comments.order_by("-date_posted").first()

            thread_info.append(
                {
                    "thread": thread,
                    "comment_count": comment_count,
                    "last_comment": last_comment,
                }
            )

        context["thread_info"] = thread_info
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = "thread.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all() # Get all comments from the parent thread. Customize 'comment_set' with <related_name='comments'> inside Post model: thread = models.ForeignKey(Thread, related_name=...)
        liked_comments = set()
        for comment in context["comments"]:
            if comment.likes.filter(liked_by=self.request.user).exists():
                liked_comments.add(comment.id)

        context["liked_comments"] = liked_comments
        return context
    
    def get_object(self, queryset=None):
        thread = super().get_object(queryset)
        user_session_key = f"viewed_thread_{thread.id}"

        if not self.request.session.get(user_session_key, False):
            thread.views = F("views") + 1
            thread.save()
            self.request.session[user_session_key] = True
        
        return thread

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = "thread_create.html"
    form_class = forms.ThreadCreateForm
    success_url = reverse_lazy("threads")

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = "thread_update.html"
    fields = ["description", "flag"]
    success_url = reverse_lazy("threads")


class ThreadDeleteView(LoginRequiredMixin, DeleteView):
    model = Thread
    template_name = "thread_delete.html"
    success_url = reverse_lazy("threads")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment_create.html"
    fields = ["text"]
    
    def get_success_url(self):
        return reverse_lazy('thread', kwargs={'pk': self.object.thread.pk})


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thread = get_object_or_404(Thread, pk=self.kwargs["pk"])

        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = "comment_update.html"
    fields = ["text"]

    def get_success_url(self):
        comment = self.get_object()
        thread = comment.thread

        return reverse_lazy("thread", kwargs={"pk": thread.pk})
    

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        comment = self.get_object() # Get the comment to be deleted
        thread = comment.thread # Get the parent thread

        return reverse_lazy("thread", kwargs={"pk": thread.pk}) # Redirect to the parent thread
    

class ToggleLikeView(LoginRequiredMixin, View):

    def post(self, request, comment_id):
        user = request.user
        comment = get_object_or_404(Comment, id=comment_id)

        like, created = Like.objects.get_or_create(liked_by=user, comment=comment)

        if not created:
            like.delete()  # Unlike if already liked
            liked = False
        else:
            liked = True  # Like the comment

        return redirect("thread", pk=comment.thread.pk)
        # return JsonResponse({"liked": liked, "like_count": comment.like_count()})
