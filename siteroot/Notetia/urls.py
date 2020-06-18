from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list),
    path('Autorization', autorization, name ='login'),
    path('Registration', sign_up, name = 'signup'),
    path('Nodes', main_page, name = 'main_page'),
    path('Content', content)
]