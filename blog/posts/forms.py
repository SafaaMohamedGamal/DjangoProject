from django import forms
from .models import comments ,Post

class commentForm(forms.ModelForm):
	class Meta:
		model = comments
		fields = ('commentText',)

class postForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','content','tag_post','category_type','photo')