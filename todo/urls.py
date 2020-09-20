from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('del/<int:item_id>', views.remove),
]
