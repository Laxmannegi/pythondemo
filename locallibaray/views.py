from django.shortcuts import render
from django.http import HttpResponse
from locallibaray.models import Post
 
#def index(request):
    
 #   return render_to_response('index.html')
	
	
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    ##num_books=Book.objects.all().count()
    ##num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    ##num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Post.objects.count()  # The 'all()' is implied by default.
    model = Post
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_authors':num_authors},
    )
	

from django.views import generic

class PostListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = Post
	#context_object_name = 'post_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'post_list.html'  # Specify your own template name/location