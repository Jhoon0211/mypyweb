from cart import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('add/<int:product_id>/', views.add,
                        name='product_add'),
]