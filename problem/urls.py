from django.urls import path
from . import views


urlpatterns = [
    path('', views.problems, name="problems"),
    path('problem/<slug:pk>', views.ProblemDetailView.as_view(), name="problem_detail"),
    path("add_comment", views.add_comment),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("symptom/<slug:pk>", views.SymptomDetailView.as_view(), name="symptom_detail"),
    path('add_like/<slug:pk>', views.add_like),
    path("add_dislike/<slug:pk>", views.add_dislike),
    path("comment_edit/<slug:pk>", views.edit_comment),
    path("comment_delete/<slug:pk>", views.delete_comment),
]
