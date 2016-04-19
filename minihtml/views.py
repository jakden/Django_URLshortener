from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.http import HttpResponseRedirect
import random
import string
from django.db import IntegrityError
        # everything else in your view
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'minihtml/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    p = Post.objects.filter(slug=slug)
    return render(request, 'minihtml/post_detail.html', {'p': p})

def post_new(request):
	form = PostForm(request.POST)
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	if form.is_valid():
	    post = form.save(commit=False)
	    post.author = request.user
	    post.published_date = timezone.now()

	    try:
	    	s = (Post.objects.filter(website=post.website).values('slug'))
	    	a = s[0]
	    	post.slug = a.get("slug")

	    except IndexError:

		    result = None
		    while result is None:
			    try:
			    
			    	post.slug = (''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(random.choice(a))))
			    	post.save()

			    except IntegrityError as e:
			    	continue
			    break

	    return render(request, 'minihtml/post_list.html', {'post': post})
	else:
	    return render(request, 'minihtml/post_edit.html', {'form': form})



