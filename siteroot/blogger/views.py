from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.db.models import Count

from .models import Blog, Post
# from .forms import LoginForm, RegistrationForm


# def sign_up(request):
#     if request.method == 'POST':
#         logout(request)
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             blog_title = form.cleaned_data['blog_title']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             password_again = form.cleaned_data['password_again']
#             user = User.objects.filter(username=username).first()
#             if user is not None:
#                 form.add_error('username', 'User already exists!')
#             elif password != password_again:
#                 form.add_error('password_again', 'Passwords mismatch!')
#             else:
#                 user = User.objects.create_user(username, email, password)
#                 blog = Blog.objects.create(author=user, title=blog_title)
#                 login(request, user)
#                 return redirect(reverse('blog_by_id', kwargs={'blog_id': blog.id}))
#     else:
#         form = RegistrationForm()
#     return render(request, 'blogger/signup.html', {'form': form})
#
#
# def log_in(request):
#     if request.method == 'POST':
#         logout(request)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 redirect_url = request.GET.get('next')
#                 if redirect_url:
#                     if not user.is_staff:
#                         blog = Blog.objects.filter(author_id=user.id).first()
#                     else:
#                         blog = None
#                     if blog:
#                         redirect_url = reverse('blog_by_id', kwargs={'blog_id': blog.id})
#                     else:
#                         redirect_url = reverse('index')
#                 return redirect(redirect_url)
#             else:
#                 form.add_error(None, 'Invalid credentials!')
#     else:
#         form = LoginForm()
#     return render(request, 'blogger/login.html', {'form': form})
#
#
# def log_out(request):
#     logout(request)
#     redirect_url = request.GET.get('next') or reverse('index')
#     return redirect(redirect_url)
#
#
# def render_blog(request, blog_id, additional_context={}):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     posts = blog.post_set.order_by('-created_at')
#     context = {'blog': blog, 'posts': posts, **additional_context}
#     return HttpResponse(render(request, 'blogger/blog.html', context))


# def get_blog(request, blog_id):
#     return render_blog(request, blog_id)
#
#
# def get_all_blogs(request):
#     blogs = Blog.objects.all().annotate(num_posts=Count('post')).order_by('-num_posts')
#     context = {'blogs': blogs}
#     return HttpResponse(render(request, 'blogger/index.html', context))
def get_blog(request, blog_id):
    blog = Blog.objects.get(id= blog_id)
    return HttpResponse('Блок')

# @login_required(login_url='/blogger/login')
# def create_post(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#
#     if blog.author_id != request.user.id:
#         return HttpResponseForbidden('You are not allowed to post in this blog!')
#
#     subject = request.POST['subject']
#     text = request.POST['text']
#
#     error_message = None
#
#     if not subject or subject.isspace():
#         error_message = 'Please provide non-empty subject!'
#     elif not text or text.isspace():
#         error_message = 'Please provide non-empty text!'
#
#     if error_message:
#         context = {'error': error_message, 'subject': subject, 'text': text}
#         return render_blog(request, blog_id, additional_context=context)
#     else:
#         Post.objects.create(blog=blog, subject=subject, text=text)
#         return HttpResponseRedirect(reverse('blog_by_id', kwargs={'blog_id': blog_id}))
# from django.shortcuts import render

# Create your views here.
