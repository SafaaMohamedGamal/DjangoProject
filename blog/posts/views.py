from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import comments, replys, Post
from .forms import commentForm, postForm 
from django.db.models import Q
from django.contrib.auth.models import User


#to 5 posts in lamding page
def showPosts(request):
    all_posts = Post.objects.all().order_by('-time_created')[:5]
    allcomments = comments.objects.filter(postId=1).order_by('commentTime')
    allreplys = replys.objects.filter(postId=1).order_by('replyTime')
    context = {'all_posts':all_posts, 'comments': allcomments, 'replys': allreplys}
    return render(request ,'showPosts.html' ,context)

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
    template_name = 'comments.html'
    post = get_object_or_404(Post, id='1')
    comments = post.comments_set.filter(postId='1')
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.postId = post
            new_comment.userId=request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = commentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

