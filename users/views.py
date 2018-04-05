from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect

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
class PostFormView(generic.TemplateView):
		template_name="form/postForm.html"
		def get(self,request):
			form=PostForm()
			return render(request,self.template_name,{'form':form})
		def post(self,request):
				form=PostForm(request.POST)
				#if form.is_valid():
				post=form.save(commit=False)	
				post.user=request.user.id
				post.save()
				form=PostForm()
				return redirect('home:home')
				args={"form":form}	
				return render(request,self.template_name,args)
class CategoryView(generic.DetailView):
	def get_queryset(self):
			return Post.objects.all()
class categoryListView(generic.ListView):
	template_name="users/category.html"
	context_object_name="category_list"
	def get_queryset(self):
		return Post.objects.order_by('Category')














'''def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'postIt/name.html', {'form': form})        
'''