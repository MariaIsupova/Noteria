from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list),
    path('Autorization', autorization, name ='login'),
    path('Registration', sign_up, name = 'signup'),
    path('Nodes', main_page, name = 'main_page'),
    path('<int:category_id>/new_note', open_page_caeate_note,  name='new_note'),
    path('<int:category_id>/<int:note_id>', change_note,  name='change_note'),
    path('<int:category_id>/<int:note_id>/delete_note', delete_note,  name='delete_note'),
    path('<int:category_id>/<int:note_id>/update_note', update_note,  name='update_note'),
    path('', get_all_categories, name='categories'),
    path('create_category', create_category, name='create_category'),
    path('<int:category_id>/', get_category, name='category_by_id'),
    path('<int:category_id>/create_note', create_note, name='create_note')
]