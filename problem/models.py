from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Problem(models.Model):
    name        = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    solution    = models.TextField(blank=True)


    def get_absolute_url(self):
        return reverse("problem_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name
    

class Symptom(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    problem     = models.ForeignKey(Problem, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse("symptom_detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user         = models.ForeignKey(User, on_delete=models.RESTRICT)
    body         = models.TextField(blank=True)
    problem      = models.ForeignKey(Problem, on_delete=models.CASCADE, blank=True, null=True)
    symptom      = models.ForeignKey(Symptom, on_delete=models.CASCADE, blank=True, null=True)
    num_likes    = models.IntegerField(null=True, blank=True, default=0)
    num_dislikes = models.IntegerField(null=True, blank=True, default=0)
    created      = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ("-created",)

    
    def __str__(self):
        if self.problem == 0 and self.symptom != 0:
            return f"Комментарий {self.user} на {self.symptom}"
        elif self.problem != 0 and self.symptom == 0:
            return f"Комментарий {self.user} на {self.problem}"
        else:
            return f"Комментарий {self.user} к списку проблем"
    


class Comment_check(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment  = models.OneToOneField(Comment, on_delete=models.CASCADE)
    likes    = models.BooleanField(default=False)
    dislikes = models.BooleanField(default=False)
