from django.urls import path
from .views import Keyboard_tester, Single_tool, Tools_list

urlpatterns = [
    path('tools-list/', Tools_list, name='Tools_list'),
    path('keyboard-tester/', Keyboard_tester, name='keyboard_tester'),
    path('tools/<slug:slug>/', Single_tool, name='single_tool'),
]