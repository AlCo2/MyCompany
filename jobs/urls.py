from django.urls import path
from jobs import views


urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]