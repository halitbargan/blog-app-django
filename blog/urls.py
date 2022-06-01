from .views import post_list,post_create,post_update,post_delete
from django.urls import path

urlpatterns = [
    path('', post_list, name='home'),
    path('create/', post_create, name='create'),
    path('update/<int:id>', post_update, name='update'),
    path('delete/<int:id>', post_update, name='delete'),
]