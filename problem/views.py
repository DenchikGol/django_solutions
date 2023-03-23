from django.shortcuts import render, redirect
from django.views import generic
from .models import Problem, Symptom, Comment
from problem.templatetags.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json

# Create your views here.
def problems(request):
    problem_list = Problem.objects.all()
    user = request.user

    return render(request, "problem/problem_list.html", {'problem_list': problem_list, "user": user})


class SearchResultsView(generic.ListView):
    model = Problem
    template_name = "problem/search_results.html"
    

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Problem.objects.filter(name__icontains=query)
        return object_list    
    

class ProblemDetailView(generic.DetailView):
    model = Problem



class SymptomDetailView(generic.DetailView):
    model = Symptom


def add_comment(request): 
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            id = request.POST.get("id")
            obj = request.POST.get("con_type").split(" | ")
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.object_id = id
            new_comment.content_type = ContentType.objects.get_by_natural_key(obj[0], obj[1])
            new_comment.body = form.cleaned_data["body"]
            new_comment.is_active = True
            new_comment.save()
            form.save_m2m()
            if obj[1] == "problem":
                return redirect(f"problem/{id}")
            else:
                return redirect(f"symptom/{id}")




def add_like(request, pk):
    if request.method == "POST":
        comment_like = Comment.objects.get(id=pk)
        if request.user in comment_like.user_like.all():
            comment_like.like -= 1
            comment_like.user_like.remove(request.user)
            comment_like.save()
        elif request.user in comment_like.user_dislike.all():
            comment_like.like += 1
            comment_like.dislike -= 1
            comment_like.user_dislike.remove(request.user)
            comment_like.user_like.add(request.user)
            comment_like.save()
        else:
            comment_like.like += 1
            comment_like.user_like.add(request.user)
            comment_like.save()
    
    return HttpResponse(status=200)


def add_dislike(request, pk):
    if request.method == "POST":
        comment_like = Comment.objects.get(id=pk)
        if request.user in comment_like.user_like.all():
            comment_like.like -= 1
            comment_like.dislike += 1
            comment_like.user_like.remove(request.user)
            comment_like.user_dislike.add(request.user)
            comment_like.save()
        elif request.user in comment_like.user_dislike.all():
            comment_like.dislike -= 1
            comment_like.user_dislike.remove(request.user)
            comment_like.save()
        else:
            comment_like.dislike += 1
            comment_like.user_dislike.add(request.user)
            comment_like.save()
    
    return HttpResponse(status=200)


def edit_comment(request, pk):
    if request.method == "POST":
        comment = Comment.objects.get(id=pk)
        text = json.loads(request.body)
        comment.body = text.get("body")
        comment.save()

    return HttpResponse(status=200)


def delete_comment(request, pk):
    if request.method == "DELETE":
        comment = Comment.objects.get(id=pk)
        comment.delete()

    return HttpResponse(status=200)
    