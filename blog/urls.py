from django.urls import path
from .views import blogpost, category_details

urlpatterns = [
    path('<slug:slug>/', blogpost, name='single_blog'),
    path('category/<slug:slug>/', category_details, name='category_details'),
] 