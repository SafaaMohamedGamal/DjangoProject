from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import comments, replys, Post, likes
from .forms import commentForm,likeForm
from django.contrib.auth.models import User
import json

def showPosts(request):
    allcomments=[]
    allreplys=[]
    all_posts = Post.objects.all()
    for x in all_posts:
        allcomments += comments.objects.filter(postId=x.id).order_by('commentTime')
        allreplys += replys.objects.filter(postId=x.id).order_by('replyTime')
    context = {'all_posts':all_posts, 'comments': allcomments, 'replys': allreplys}
    return render(request ,'showPosts.html' ,context)

def showOnePost(request, post_id):
    x = Post.objects.get(id = post_id)
    allcomments = comments.objects.filter(postId=x.id).order_by('commentTime')
    allreplys = replys.objects.filter(postId=x.id).order_by('replyTime')
    alllikes = likes.objects.filter(postId=x.id, like="like").count()
    alldislikes = likes.objects.filter(postId=x.id, like="dislike").count()
    urlike = likes.objects.get(postId=x.id, userId=request.user)
    context = {'post':x, 'comments': allcomments, 
        'replys': allreplys, 
        'likescount': alllikes, 
        'dislikescount': alldislikes,
        'urlike':urlike.like}
    return render(request ,'showOnePost.html' ,context)


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



def addComment(request):
    postid = request.GET['post']
    newComment = request.GET['text']
    if newComment:
        x = Post.objects.get(id=postid)
        new_comment = comments.objects.create(postId = x, userId=request.user)
        new_comment.commentText=newComment
        new_comment.save()
        count = str(comments.objects.filter(postId=x).count())
        return HttpResponse(json.dumps({'newComment':newComment, 'count':count}))


def addReply(request):
    postid = request.GET['post']
    commentid = request.GET['comment']
    newReply = request.GET['text']
    if newReply:
        p = Post.objects.get(id=postid)
        c = comments.objects.get(id=commentid, postId=p)
        new_reply = replys.objects.create(postId = p, commentId=c, userId=request.user)
        new_reply.replyText=newReply
        new_reply.save()
        count = str(replys.objects.filter(postId=p, commentId=commentid).count())
        return HttpResponse(json.dumps({'newReply':newReply, 'count':count}))


def addLike(request):
    postid = request.GET['post']
    newLike = request.GET['like']
    p = Post.objects.get(id=postid)
    new_like, create = likes.objects.get_or_create(postId = p, userId=request.user)
    new_like.like=newLike
    new_like.save()
    countlike = str(likes.objects.filter(postId=p, like="like").count())
    countdislike = str(likes.objects.filter(postId=p, like="dislike").count())
    return HttpResponse(json.dumps({'newLike':newLike, 'countlike':countlike, 'countdislike':countdislike}))

