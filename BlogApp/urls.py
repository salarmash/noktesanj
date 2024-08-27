from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllPostView.as_view()),
    path("<int:pk>", views.SinglePost.as_view()),
    path("category/<int:pk>", views.SingleCategoryView.as_view()),
    path("category", views.AllCategoryView.as_view()),
    path("author", views.AllAuthorView.as_view()),
    path("author/<int:pk>", views.SingleAuthorView.as_view()),
]
