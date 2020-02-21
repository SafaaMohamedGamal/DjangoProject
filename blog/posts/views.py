from django.shortcuts import render
from django.http import HttpResponse
from .models import comments, replys

def showPosts(request):
	return render(request, 'showPosts.html')

def commentsReplys(request):
	allcomments = comments.objects.filter(postId=1).order_by('commentTime')
	allreplys = replys.objects.filter(postId=1).order_by('replyTime')
	# context = {'commentReply':(allcomments , allreplys)}
	context = {'comments': allcomments, 'replys': allreplys }
	return render(request, 'showPosts.html', context)