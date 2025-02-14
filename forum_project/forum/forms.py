from django import forms

from .models import Thread, Comment


class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "thread-create-title"}),
            "description": forms.Textarea(attrs={"class": "thread-create-desc"}),
        }
