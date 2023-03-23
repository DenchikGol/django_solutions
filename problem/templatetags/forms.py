from problem.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # def __init__(*args, **kwargs):
    #     super().__init__(*args, **kwargs)

    
    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            "body": ""
        }
