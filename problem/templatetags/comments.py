from django import template
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from .forms import CommentForm

register = template.Library()

@register.inclusion_tag(filename="add_comment.html")
def add_comment(obj, request):
    form_initial = {"content_type": ContentType.objects.get_for_model(obj), "object_id": obj.pk}
    comments = obj.comments.filter(is_active=True).order_by("-created")
    all_coments = comments.count()

    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    
    form = CommentForm(initial=form_initial)                
    return {
        "comments": comments,
        "all_comment": all_coments,
        "request": request,
        "form": form,
        "obj": obj,
        "content_type": ContentType.objects.get_for_model(obj),
    }

