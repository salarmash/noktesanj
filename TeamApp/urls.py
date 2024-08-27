from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeamView.as_view()),
    path("<int:pk>", views.SingleView.as_view())
]
