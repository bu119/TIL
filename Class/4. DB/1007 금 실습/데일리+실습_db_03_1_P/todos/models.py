from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    # author이 유저 테이블을 참조 해야한다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # T/F는 0 아니면 1로 저장
