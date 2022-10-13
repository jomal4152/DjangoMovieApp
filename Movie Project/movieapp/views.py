from django.shortcuts import render, redirect
from .models import movie_details
from .forms import MovieForm


# Create your views here.

def movielist(request):
    movies = movie_details.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movieapp/movielist.html', context)


def displaydetails(request, pk):
    movies = movie_details.objects.get(id=pk)
    context = {
        'movies': movies
    }

    return render(request, 'movieapp/displaydetails.html', context)


def addmovie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        moviedetails = movie_details(name=name, description=description, year=year, image=image)
        moviedetails.save()
        return redirect('/')
    return render(request, 'movieapp/addmovie.html')


def update(request, pk):
    movie = movie_details.objects.get(id=pk)
    fm = MovieForm(request.POST or None,request.FILES, instance=movie)
    if fm.is_valid():
        fm.save()
        return redirect('/display/' + str(pk))
    return render(request, 'movieapp/editdetails.html', {'form': fm, 'movie': movie})


def delete(request, pk):
    if request.method == 'POST':
        movie = movie_details.objects.get(id=pk)
        movie.delete()
        return redirect('/')
    return render(request, 'movieapp/delete.html')
