from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request): 
	posts=Post.objects.all() #pobieranie danych z bazy danych
	return render(request, 'blog/post_list.html', {'posts':posts}) #przekazywanie posts do templatu,ale on jeszcze z tego nie korzysta, wrzycam ją w post list w 
    
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

#return zwraca to, co jest wywołaniem kolejnej funkcji (render)
#patrz urls.py blog