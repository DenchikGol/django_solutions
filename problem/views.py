from django.shortcuts import render
from django.views import generic
from .models import Problem, Symptom, Comment, Comment_check
from django.views.decorators.http import require_http_methods


# Create your views here.
class ProblemListView(generic.ListView):
    model = Problem



class SearchResultsView(generic.ListView):
    model = Problem
    template_name = "search_results.html"
    

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Problem.objects.filter(name__contains=query)
        return object_list    
    


class ProblemDetailView(generic.DetailView):
    model = Problem
    

class SymptomDetailView(generic.DetailView):
    model = Symptom


@require_http_methods(["GET", "POST"])
class CommentLikesDislikes(Comment):
    def likes_increase(self):
        pass
            


    def likes_decrease(self):
        pass


    def dislikes_increase(self):
        pass


    def dislikes_decrease(self):
        pass

    