from django.urls import path
from .views import *


urlpatterns = [
    #path('login', log_in, name='login'),
    #path('logout', log_out, name='logout'),
    #path('signup', sign_up, name='signup'),
    #path('', get_all_blogs, name='index'),
    path('<int:blog_id>/', get_blog, name='blog_by_id'),
    #path('<int:blog_id>/create_post', create_post, name='create_post'),
]
