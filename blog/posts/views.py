from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import comments, replys, Post, likes, forbWords
from .forms import commentForm,likeForm, postForm , wordForm
from django.contrib.auth.models import User
import json
from django.db.models import Q


#to 5 posts in lamding page
def showPosts(request):
    allcomments=[]
    allreplys=[]
    all_posts = Post.objects.all().order_by('-time_created')[:5]
    for x in all_posts:
      alldislikes = likes.objects.filter(postId=x.id, like="dislike").count()
      if alldislikes==10:
        x.delete();

    context = {'all_posts':all_posts}
    return render(request ,'showPosts.html' ,context)

def showOnePost(request, post_id):
    x = Post.objects.get(id = post_id)
    allcomments = comments.objects.filter(postId=x.id).order_by('commentTime')
    allreplys = replys.objects.filter(postId=x.id).order_by('replyTime')
    alllikes = likes.objects.filter(postId=x.id, like="like").count()
    alldislikes = likes.objects.filter(postId=x.id, like="dislike").count()
    badWords = forbWords.objects.all()
    xword = []
    for word in badWords:
        xword.append(word.forbWord)

    if request.user.is_authenticated:
      urlike = likes.objects.filter(postId=x.id, userId=request.user)

      context = {'post':x, 'comments': allcomments, 
          'replys': allreplys, 
          'likescount': alllikes, 
          'dislikescount': alldislikes,
          'urlike':urlike, 'forbWords': xword}

    else:
      context = {'post':x,
          'likescount': alllikes, 
          'dislikescount': alldislikes, 'comments': allcomments, 'forbWords': xword}
    return render(request ,'showOnePost.html' ,context)

#add new post through form
def addPost(request):
  new_post=postForm()
  added_post=None
  if request.method=="POST":
    new_post=postForm(request.POST,request.FILES)
    if new_post.is_valid():
      added_post=new_post.save(commit=False)
      added_post.author=request.user
      added_post.save()
      return HttpResponseRedirect('/posts/')
  return render(request,'new.html',{'new_post':new_post})

# when user choose specific category
def allCategoryPosts(request,cat_num):
      cat_posts = Post.objects.filter(category_type=cat_num).order_by('-time_created')
      context={'cat_posts':cat_posts}
      return render(request ,'CategotyPage.html' ,context)

# when user choose specific category
def allCategoryPosts(request,cat_num):
      cat_posts = Post.objects.filter(category_type=cat_num).order_by('-time_created')
      context={'cat_posts':cat_posts}
      return render(request ,'CategotyPage.html' ,context)

#search for posts with title or tag
def searchForPost(request):
  print(request.GET.get('word'))
  term = request.GET.get('word')
  print(term)
  cat_posts = Post.objects.filter(
    Q(title__icontains=term) |
    Q(tag_post__icontains=term)
    ).order_by('-time_created')
  context={'cat_posts':cat_posts}
  return render(request ,'searchPage.html' ,context)


def subscribeCategory(request,user_num,cat_num):
	instance = categories_users_id(categories_id=cat_num, user_id=user_num)
	if(subscribeCategory):
		instance.save()
	else:
		instanse.delete()




	

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
  if request.user.is_authenticated:
    postid = request.GET['post']
    newLike = request.GET['like']
    p = Post.objects.get(id=postid)
    new_like, create = likes.objects.get_or_create(postId = p, userId=request.user)
    new_like.like=newLike
    new_like.save()
    countlike = str(likes.objects.filter(postId=p, like="like").count())
    countdislike = str(likes.objects.filter(postId=p, like="dislike").count())
    return HttpResponse(json.dumps({'newLike':newLike, 'countlike':countlike, 'countdislike':countdislike}))
  

def adminForbWords(request):
  added_badWords=None
  if request.method=="POST":
    new_badWords=wordForm(request.POST)
    if new_badWords.is_valid():
      added_badWords=new_badWords.save(commit=False)
      added_badWords.save()
      return HttpResponseRedirect('/adminForbWords/')
  else:
    new_badWords=wordForm()

  badWords = forbWords.objects.all()
  context = {'badWords':badWords,
              'form':new_badWords}
  return render(request,'forbWords.html',context)



def editWords(request, word_num):
  w = forbWords.objects.get(id=word_num)
  added_badWords=None
  if request.method=="POST":
    new_badWords=wordForm(request.POST, instance=w)
    if new_badWords.is_valid():
      added_badWords=new_badWords.save(commit=False)
      added_badWords.save()
      return HttpResponseRedirect('/adminForbWords/')
  else:
    new_badWords=wordForm()

  badWords = forbWords.objects.all()
  context = {'badWords':badWords,
              'form':new_badWords}
  return render(request,'forbWords.html',context)


def deleteWords(request, word_num):
  badWords = forbWords.objects.filter(id=word_num)
  badWords.delete()
  return HttpResponseRedirect('/adminForbWords/')


