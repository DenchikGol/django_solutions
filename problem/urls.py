from django.urls import path
from . import views


urlpatterns = [
    path('', views.problems, name="problems"),
    path('prbolem/<slug:pk>', views.ProblemDetailView.as_view(), name="problem_detail"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("symptom/<slug:pk>", views.SymptomDetailView.as_view(), name="symptom_detail"),
]
