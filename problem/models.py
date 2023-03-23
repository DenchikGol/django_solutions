from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.

class Problem(models.Model):
    name        = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    solution    = models.TextField(blank=True)
    comments    = GenericRelation("Comment")


    def get_absolute_url(self):
        return reverse("problem_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name
    

class Symptom(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    problem     = models.ForeignKey(Problem, on_delete=models.CASCADE)
    comments    = GenericRelation('Comment')


    def get_absolute_url(self):
        return reverse("symptom_detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.name
 

class Comment(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name="Родительская категория", related_name="children", on_delete=models.CASCADE, editable=False)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Пользователь")
    body = models.TextField(verbose_name="Комментарий")
    like = models.IntegerField(default=0, verbose_name="like")
    dislike = models.IntegerField(default=0, verbose_name="dislike")
    user_like = models.ManyToManyField(User, verbose_name="Кто поставил лайк", related_name="users_like", blank=True)
    user_dislike = models.ManyToManyField(User, verbose_name="Кто поставил дизлайк", related_name="users_dislike", blank=True)
    count_comment = models.IntegerField(default=0, verbose_name="Количество комментариев")
    is_active = models.BooleanField(default=False, verbose_name="Модерация")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"
        ordering = ["-created"]


    def __str__(self):
        return f"{self.content_object}"
    