from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class poststable(models.Model):
	# postId = models.CharField(primary_key=True, max_length=10)
	pass
		

class comments(models.Model):
	# commentId = models.CharField(primary_key=True, max_length=10)
	commentText = models.CharField(max_length=100)
	commentTime = models.DateTimeField(auto_now_add=True)
	postId = models.ForeignKey(poststable, on_delete=models.CASCADE)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.commentText

		

class replys(models.Model):
	# replyId = models.CharField(primary_key=True, max_length=10)
	replyText = models.CharField(max_length=100)
	replyTime = models.DateTimeField(auto_now_add=True)
	commentId = models.ForeignKey(comments, on_delete=models.CASCADE)
	postId = models.ForeignKey(poststable, on_delete=models.CASCADE)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return  self.replyText


class likes(models.Model):
	like = models.BooleanField(default=None)
	postId = models.ForeignKey(poststable, on_delete=models.CASCADE)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.id

		


# def getCommentId(commentText0):
# 	return comments.objects.get(commentText = commentText0).commentId