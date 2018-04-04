from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
# Create your views here.
class PostIndexView(generic.ListView):
	"""docstring for ClassName"""
	template_name='postIt/index.html'
	context_object_name='latest_post'
	def get_queryset(self):
		return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class PostDetailView(generic.DetailView):
       def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())
class DatesIndexView(generic.ListView):
	template_name='postIt/Dates.html'
	context_object_name='dates'
	def get_queryset(self):
		return Post.objects.all()

class DatesDetailsView(generic.DetailView):
       def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())