from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count

from .forms import RegistrationForm

def sign_up(request):
    if request.method == 'POST':
        logout(request)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            user = User.objects.filter(username=username).first()
            if user is not None:
                form.add_error('username', 'User already exists!')
            elif password != password_again:
                form.add_error('password_again', 'Passwords mismatch!')
            else:
                user = User.objects.create_user(username, email, password)
                # blog = Blog.objects.create(author=user, title=blog_title)
                login(request, user)
                return redirect(reverse('main_page'))
    else:
        form = RegistrationForm()
    return render(request, 'notetia/Registration.html', {'form': form})


def posts_list(request):
    return render(request,'notetia/index.html')

def main_page(request):

    return HttpResponse(render(request,'notetia/Nodes.html'))

def autorization(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main_page'))
        else:
            error = 'Ошибка!'
    else:
        error = None
    return HttpResponse(render(request, 'notetia/Autorization.html', {'error': error}))



def registration(request):
    return render(request,'notetia/Registration.html')

def main_page(request):
    return render(request,'notetia/Nodes.html')

def content(request):
    return render(request,'notetia/Content.html')