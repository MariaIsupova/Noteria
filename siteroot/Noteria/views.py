from django.shortcuts import render
from django.http import HttpResponse
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
from .models import Category, Note
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
    return render(request, 'Noteria/Registration.html', {'form': form})


def posts_list(request):
    return render(request,'Noteria/index.html')

def main_page(request):

    return HttpResponse(render(request,'Noteria/base.html'))

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
    return HttpResponse(render(request, 'Noteria/Autorization.html', {'error': error}))
# Create your views here.
def posts_list(request):
    return render(request,'Noteria/index.html')

def autorization(request):
    return render(request,'Noteria/Autorization.html')

def registration(request):
    return render(request,'Noteria/Registration.html')

def get_category(request, category_id):
    return render_category(request, category_id)


def get_all_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return HttpResponse(render(request, 'user/base.html', context))


def render_category(request, category_id, additional_context={}):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    notes = category.note_set.order_by('-created_at')
    context = {'categories': categories, 'category': category, 'notes': notes, **additional_context}
    return HttpResponse(render(request, 'user/nodes.html', context))

def open_page_caeate_note(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'category': category}
    return HttpResponse(render(request, 'user/create_note.html', context))

def create_category(request):
    name_category = request.POST['new_category']
    category = Category.objects.create(author=request.user, title=name_category)
    return HttpResponseRedirect('/user/%s/' % category.id)
    # return HttpResponseRedirect(reverse('category_by_id', kwargs={'category_id': category_id}))

#@login_required(login_url='/blogger/login')
def create_note(request, category_id):


    category = get_object_or_404(Category, pk=category_id)

    subject = request.POST['note_name']
    text = request.POST['note']

    error_message = None

    if not subject or subject.isspace():
        error_message = 'Поле с названием должно быть заполнено'
    elif not text or text.isspace():
        error_message = 'Поле с тектом не должно быть пустым'

    if error_message:
        context = {'error': error_message, 'subject': subject, 'text': text}
        return render_category(request, category_id, additional_context=context)
    else:
        Note.objects.create(category=category, subject=subject, text=text)
        return HttpResponseRedirect('/user/%s/' % category.id)
        return HttpResponseRedirect(reverse('category_by_id', kwargs={'category_id': category_id}))


def change_note(request, category_id, note_id):
    category = get_object_or_404(Category, pk=category_id)
    note = get_object_or_404(Note, pk=note_id)
    context = {'note': note, 'category': category}

    return HttpResponse(render(request, 'user/create_note.html', context))


def delete_note(request, category_id, note_id):
        note = Note.objects.get(id=note_id)
        note.delete()
        return HttpResponseRedirect('/user/%s/' % category_id)
# Create your views here.
def update_note(request, category_id, note_id):
    note = Note.objects.get(id=note_id)
    subject = request.POST['note_name']
    text = request.POST['note']
    note.subject=subject
    note.text=text
    note.save()
    return HttpResponseRedirect('/user/%s/' % category_id)