from django.urls import path
from main import views

# tugas 2: menjadikan main sebagai app
app_name = 'main'

# url untuk mengakses app main
urlpatterns = [
    # --- tugas 5 ---
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    # --- tugas 4 ---
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('update_amount/<int:product_id>/<str:action>/', views.update_amount, name='update_amount'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    # --- tugas 3 ---
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('', views.show_main, name='show_main'),
]