from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectView.as_view()),
    path("<int:pk>",views.SingleView.as_view()),
    path("category", views.AllCategoryView.as_view()),
    path("category/<int:pk>", views.SingleCategoryView.as_view())
]
