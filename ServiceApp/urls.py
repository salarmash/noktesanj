from django.urls import path
from . import views

urlpatterns = [
    path("", views.ServiceView.as_view()),
    path("item", views.ItemView.as_view()),
    path("item/<int:pk>", views.SingleItem.as_view())
]
