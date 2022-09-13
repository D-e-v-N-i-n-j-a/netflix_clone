from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import Movie,Comments
# Create your views here.

@login_required(login_url='login')
def homepage(request):
    movie = Movie.objects.all()
    return render(request,'index.html',{'movie':movie})



@login_required(login_url='login')
def view(request,pk):
    user = auth.get_user(request)
    movie_pk = Movie.objects.get(id=pk)
    
    if request.method =='POST':
        post = request.POST['post']
        data = Comments.objects.create(post=post,user =user,movie=movie_pk)
        data.save()
        print('item successfully saved')
        return HttpResponseRedirect(request.path_info)
     
    
    
    
    
    
    
    
    movie = Movie.objects.filter(id=pk)
    comm = Comments.objects.all()
    allPost = []
    for item in movie:
        title = item
    
    for comments in comm:
        if comments.movie.id == title.id:
            allPost.append(comments)
            
        
    
        
    
    return render(request,'view.html',{'movie':movie,"comment":allPost})
