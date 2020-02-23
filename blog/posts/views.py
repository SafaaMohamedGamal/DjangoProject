from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import comments, replys, Post
from .forms import commentForm
from django.contrib.auth.models import User


#to 5 posts in lamding page
def showPosts(request):
    all_posts = Post.objects.all().order_by('-time_created')[:5]
    allcomments = comments.objects.filter(postId=1).order_by('commentTime')
    allreplys = replys.objects.filter(postId=1).order_by('replyTime')
    context = {'all_posts':all_posts, 'comments': allcomments, 'replys': allreplys}
    return render(request ,'showPosts.html' ,context)


def subscribeCategory(request,user_num,cat_num):
	instance = categories_users_id(categories_id=cat_num, user_id=user_num)
	if(subscribeCategory):
		instance.save()
	else:
		instanse.delete()

# when user choose specific category
def allCategoryPosts(request,cat_num):
      cat_posts = Post.objects.filter(category_type=cat_num).order_by('-time_created')
      context={'cat_posts':cat_posts}
      return render(request ,'CategotyPage.html' ,context)


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

