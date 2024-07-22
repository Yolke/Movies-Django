from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie


def movies(request):   
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("HomePage")

def detail(request, id):
    data = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/')
    else:
        form = MovieForm()
    return render(request, 'movies/add.html', {'form': form})

def delete(request, id):
    movie = get_object_or_404(Movie, pk=id)
    movie.delete()
    return HttpResponseRedirect("/movies/")


