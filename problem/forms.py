from .models import Comment
from django.forms import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("user", "body", "problem", "symptom")
