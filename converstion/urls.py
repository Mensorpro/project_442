from django.urls import path
from . import views

app_name = 'converstion'

urlpatterns = [
    path('new/<int:item_pk>/' , views.new_converstion , name = 'new'),
    path('inbox/' , views.inbox , name = 'inbox'),
    path('detail/<int:pk>/' , views.detail , name = 'detail'),
]