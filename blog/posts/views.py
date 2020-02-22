from django.shortcuts import render
from django.http import HttpResponse
from .models import comments, replys

def showPosts(request):
	return render(request, 'showPosts.html')

def showPosts(request):
	all_posts = Post.objects.all()
	context = {'all_posts':all_posts }
	return render(request ,'showPosts.html' ,context)


def subscribeCategory(request,user_num,cat_num):
	instance = categories_users_id(categories_id=cat_num, user_id=user_num)
	if(subscribeCategory):
		instance.save()
	else:
		instanse.delete()

def allCategoryPosts(request,cat_num):
	  queryset = Post.objects.filter(category_type=cat_num).order_by('-time_created')

def searchForPost(string):
	queryset = Post.objects.filter(title=string) | Post.objects.filter(tag_post = string)
	ordered_query = queryset.order_by('-time_created')
	

def commentsReplys(request):
	allcomments = comments.objects.filter(postId=1).order_by('commentTime')
	allreplys = replys.objects.filter(postId=1).order_by('replyTime')
	# context = {'commentReply':(allcomments , allreplys)}
	context = {'comments': allcomments, 'replys': allreplys }
	return render(request, 'showPosts.html', context)