from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content", "image_url", "category"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.all()