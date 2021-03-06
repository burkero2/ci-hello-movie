from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import MovieForm


# Create your views here.
def get_movie_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'movie_app/movie_app_home.html', context)

def add_movie(request):
    if request.method=='POST':
        form = MovieForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('get_movie_list')
    form = MovieForm()
    context = {
        'form':form
    }
    return render(request, 'movie_app/movie_app_add.html', context)

def edit_movie(request, movie_id):
    movie = get_object_or_404(Item, id=movie_id)
    
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('get_movie_list')
    form = MovieForm(instance=movie)
    
    context={
        'form':form
    }
    return render(request, 'movie_app/movie_app_edit.html', context)

def toggle_movie(request, movie_id):
    movie = get_object_or_404(Item, id=movie_id)
    movie.watched = not movie.watched
    movie.save()
    return redirect('get_movie_list')

def delete_movie(request, movie_id):
    movie = get_object_or_404(Item, id=movie_id)
    movie.delete()
    return redirect('get_movie_list')