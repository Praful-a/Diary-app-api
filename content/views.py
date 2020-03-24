from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, CreateEntryForm, UpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Entry
# Create your views here.


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are registered ' + username + ' now log in.')
            return redirect('/')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Username OR Password Incorrect!')
    context = {}
    return render(request, 'login.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')


def diary(request):
    entries = Entry.objects.filter(author=request.user).order_by('-date_posted')
    context = {'entries': entries}
    return render(request, 'diary.html', context)


def add(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateEntryForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        author = User.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()

        form = CreateEntryForm()
        return redirect('home')
    context['form'] = form
    return render(request, 'add.html', context)


def must_authenticate(request):
    return render(request, 'must_authenticate.html')


def edit(request, slug):

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(Entry, slug=slug)
    if request.POST:
        form = UpdateForm(request.POST, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            blog_post = obj
            return redirect('home')
    form = UpdateForm(
        initial={
            'title': blog_post.title,
            'text': blog_post.text
        }
    )

    context = {'form': form}
    return render(request, 'edit.html', context)


def delete(request, slug):
    entries = get_object_or_404(Entry, slug=slug)
    if request.method == 'POST':
        entries.delete()
        return redirect('home')
    context = {'entries': entries}
    return render(request, 'delete.html', context)
