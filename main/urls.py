from django.urls import path
from main.views import show_main

# tugas 2: menjadikan main sebagai app
app_name = 'main'

# url untuk mengakses app main
urlpatterns = [
    path('', show_main, name='show_main'),
]