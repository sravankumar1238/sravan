from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect, reverse
from .models import Recipe, MyUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/recipe/index/")
        else:
            return render(request, 'recipe/login.html', {'error': 'Invalid credentials'})
    return render(request,'recipe/login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        date_of_birth=request.POST['date_of_birth']
        MyUser.objects.create_user(username=username, email=email, password=password, date_of_birth=date_of_birth)
        return HttpResponseRedirect('/recipe/')
    return render(request, 'recipe/register.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/recipe/")


@login_required(login_url="/recipe/")
def index(request):
    recipes = Recipe.objects.all()
    return render(request,"recipe/index.html", {'recipes':recipes} )


@login_required(login_url="/recipe/")
def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request,'recipe/detail.html', {'food':recipe})


@login_required(login_url="/recipe/")
def edit(request, pk):
    q = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        q.name = request.POST.get("recipe_name")
        q.ingredients = request.POST.get("ingredients")
        q.process = request.POST.get("process")
        q.save()
        return HttpResponseRedirect(reverse('recipe:index'))
    else:
        return render(request, "recipe/edit.html",{'q':q})


@login_required(login_url="/recipe/")
def create(request):
    if request.method == "POST":
        Recipe.objects.create(
            name=request.POST.get("recipe_name"),
            ingredients=request.POST.get("ingredients"),
            process=request.POST.get("process")
        )
        return HttpResponseRedirect(reverse('recipe:index'))
    else:
        return render(request, "recipe/create.html")

