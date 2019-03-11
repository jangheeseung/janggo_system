from django.db import models 
import datetime
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=125)
    post_type = models.CharField(max_length=125, default="question")
    content = models.TextField()
    author = models.CharField(max_length=125, null=True)
    password = models.CharField(max_length=15)
    lookup = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.title[:20]

class Comments(models.Model): # 댓글
    content = models.TextField(max_length=500) # 댓글 내용
    author = models.CharField(max_length=125, null=False) # 작성자
    email = models.CharField(max_length=125, null=False) # 이메일
    board_pk = models.ForeignKey(Board, on_delete = models.CASCADE)# 게시물의 pk 값
    posttime = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    def __str__(self):
        return self.author