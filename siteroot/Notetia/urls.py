from django.urls import path
from .views import *

urlpatterns = [
    path('Autorization/', autorization, name ='login'),
    path('Registration/', sign_up, name = 'signup'),
    path('base/<int:category_id>/new_note', open_page_caeate_note,  name='new_note'),
    path('<int:category_id>/<int:note_id>', change_note,  name='change_note'),
    path('<int:category_id>/<int:note_id>/delete_note', delete_note,  name='delete_note'),
    path('<int:category_id>/<int:note_id>/update_note', update_note,  name='update_note'),
    path('base', get_all_categories, name='categories'),
    path('',posts_list),
    path('base/create_category', create_category, name='create_category'),
    path('base/<int:category_id>/', get_category, name='category_by_id'),
    path('base/<int:category_id>/create_note', create_note, name='create_note')

]