from django.urls import path
from Operation import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('Edit', views.Edit, name='Edit'),
    path('Update/<str:id>', views.Update, name='Update'),
    path('Delete/<str:id>', views.Delete, name='Delete'),
]