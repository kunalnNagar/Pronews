from django.shortcuts import render, get_object_or_404, redirect
from main.models import Categories, News
from main.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    cate = Categories.objects.all()[:4]
    run = News.objects.all().order_by('-id')[:1]
    slide = News.objects.all().order_by('-id')[:4]
    news = News.objects.all().order_by("-id")[:6]
    india = News.objects.filter(category__name= "INDIA NEWS")[:4]
    world = News.objects.filter(category__name= "WORLD NEWS")[:4]
    bollywood = News.objects.filter(category__name= "BOLLYWOOD NEWS")[:4]
    sports = News.objects.filter(category__name= "SPORTS NEWS")[:4]
    context = {
        'cate':cate,
        'news':news,
        'slide':slide,
        'run':run,
        'india':india,
        'world':world,
        'bollywood':bollywood,
        'sports':sports,
    }
    return render(request, 'index.html', context)

def details(request,id):
    data = News.objects.filter(id = id)
    top5 = News.objects.all().order_by('-id')[:5]
    news1 = get_object_or_404(News, id=id)
    com = news1.comments.order_by('-create')
    # comdata = News.objects.all()
    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news1
                comment.name = request.user
                comment.save()
                # form.save()
                
                return redirect("details", id=news1.id)
        else:
            messages.error(request, "Please login to comment.")
            return redirect('login')


    return render(request, 'details.html', {'data':data,'top5':top5, "form":form, "com":com})

def india(request):
    india = News.objects.filter(category__name= "INDIA NEWS").order_by('-id')
    return render(request,'india.html',{'india':india})

def world(request):
    world = News.objects.filter(category__name= "WORLD NEWS").order_by('-id')
    return render(request,'world.html',{'world':world})

def bollywood(request):
    bollywood = News.objects.filter(category__name= "BOLLYWOOD NEWS").order_by('-id')
    return render(request,'bollywood.html',{'bollywood':bollywood})

def sports(request):
    sports = News.objects.filter(category__name= "SPORTS NEWS").order_by('-id') 
    return render(request,'sports.html',{'sports':sports})

def search(request):
    query = request.GET['q']
    search = News.objects.filter( title__icontains= query).order_by('-id')
    return render(request, 'search.html', {'query':query, 'search':search})

def all(request):
    all1 = News.objects.all().order_by('-id')
    return render(request, 'all1.html', {'all1':all1})