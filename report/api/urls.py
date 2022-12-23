from django.urls import path
from .views import ListNewsApiView, DetailNewApiView, CategoriesApiview, DetailCategoriesApiView

urlpatterns = [
    path('news/', ListNewsApiView.as_view()),
    path('news/<int:pk>/', DetailNewApiView.as_view()),
    path('categories/',CategoriesApiview.as_view()),
    path('categories/<int:pk>/',DetailCategoriesApiView.as_view()),
]
