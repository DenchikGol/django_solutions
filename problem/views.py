from django.shortcuts import render, redirect
from django.views import generic
from .models import Problem, Symptom, Comment, Comment_check
from .forms import CommentForm
from django.views.decorators.http import require_http_methods


# Create your views here.
def problems(request):
    problem_list = Problem.objects.all()
    comments = Comment.objects.filter(problem=None, symptom=None)
    user = request.user

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if len(new_comment.body) == 0:
                return redirect("problems")
            new_comment.problem = None
            new_comment.symptom = None
            new_comment.save()
            return redirect('problems')
    else:
        form = CommentForm()
        return render(request, "problem/problem_list.html", {'problem_list': problem_list, 'form': form, "comments": comments, "user": user})

class SearchResultsView(generic.ListView):
    model = Problem
    template_name = "problem/search_results.html"
    

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

    