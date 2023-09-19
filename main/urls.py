from django.urls import path
from main import views

# tugas 2: menjadikan main sebagai app
app_name = 'main'

# url untuk mengakses app main
urlpatterns = [
    path('create-product', views.create_product, name='create_product'),
    path('html', views.show_html, name='show_html'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('', views.show_main, name='show_main'),
]