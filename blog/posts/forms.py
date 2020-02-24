from django import forms
from .models import comments, likes

class commentForm(forms.ModelForm):
	class Meta:
		model = comments
		fields = ('commentText',)

class likeForm(forms.ModelForm):
	class Meta:
		model = likes
		fields = ('like',)